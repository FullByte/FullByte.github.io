// ------------------------------------------------------
// Includes
// ------------------------------------------------------
#include <time.h>
#include <string.h>
#include <WiFi.h>
#include <mqtt_client.h>
#include <az_core.h>
#include <az_iot.h>
#include <azure_ca.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>

#include "AzIoTSasToken.h"
#include "SerialLogger.h"
#include "iot_configs.h"

// ------------------------------------------------------
// Constants & Macros
// ------------------------------------------------------


static const char* NTP_SERVERS[]                    = {"pool.ntp.org", "time.nist.gov"};
static const long  UNIX_TIME_NOV_13_2017            = 1510592825;

// Timezone definitions
static const int   PST_TIME_ZONE                    = -8; // PST: UTC-8
static const int   PST_DAYLIGHT_SAVINGS_DIFF        = 1;  // Daylight saving
static const long  GMT_OFFSET_SECS                  = PST_TIME_ZONE * 3600;
static const long  GMT_OFFSET_SECS_DST              = (PST_TIME_ZONE + PST_DAYLIGHT_SAVINGS_DIFF) * 3600;

// Telemetry
static const int   SAS_TOKEN_DURATION_IN_MINUTES    = 60;
static const int   MQTT_QOS1                        = 1;
static const int   DO_NOT_RETAIN_MSG                = 0;

// BME280 Sensor
static const uint8_t I2C_ADDRESS                    = 0x76;
Adafruit_BME280     bme;

// ------------------------------------------------------
// Azure IoT and WiFi Configurations
// ------------------------------------------------------
static const char* ssid               = IOT_CONFIG_WIFI_SSID;
static const char* password           = IOT_CONFIG_WIFI_PASSWORD;
static const char* host               = IOT_CONFIG_IOTHUB_FQDN;
static const char* mqtt_broker_uri    = "mqtts://" IOT_CONFIG_IOTHUB_FQDN;
static const char* device_id          = IOT_CONFIG_DEVICE_ID;
static const int   mqtt_port          = AZ_IOT_DEFAULT_MQTT_CONNECT_PORT;

// Buffers for MQTT/IotHub
static char mqtt_client_id[128];
static char mqtt_username[128];
static char mqtt_password[200];
static uint8_t sas_signature_buffer[256];

// Telemetry
static char telemetry_topic[128];
static char telemetry_payload[256];
static uint32_t telemetry_send_count = 0;
static unsigned long next_telemetry_send_time_ms = 0;

// MQTT client and IoT Hub client
static esp_mqtt_client_handle_t mqtt_client;
static az_iot_hub_client client;

#ifndef IOT_CONFIG_USE_X509_CERT
static AzIoTSasToken sasToken(
    &client,
    AZ_SPAN_FROM_STR(IOT_CONFIG_DEVICE_KEY),
    AZ_SPAN_FROM_BUFFER(sas_signature_buffer),
    AZ_SPAN_FROM_BUFFER(mqtt_password));
#endif // IOT_CONFIG_USE_X509_CERT

// ------------------------------------------------------
// Utility Functions
// ------------------------------------------------------
static uint32_t getEpochTimeInSecs()
{
  return static_cast<uint32_t>(time(NULL));
}

static void connectToWiFi()
{
  if (WiFi.status() == WL_CONNECTED)
  {
    return; // Already connected
  }

  Logger.Info("Connecting to WiFi SSID: " + String(ssid));
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  delay(100);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED)
  {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Logger.Info("WiFi connected, IP address: " + WiFi.localIP().toString());
}

static void initializeTime()
{
  Logger.Info("Setting time using SNTP");

  // Use the list of NTP servers
  configTime(GMT_OFFSET_SECS, GMT_OFFSET_SECS_DST, NTP_SERVERS[0], NTP_SERVERS[1]);

  time_t now = time(NULL);
  while (now < UNIX_TIME_NOV_13_2017)
  {
    delay(500);
    Serial.print(".");
    now = time(nullptr);
  }
  Serial.println();
  Logger.Info("Time initialized!");
}

static void initializeIoTHubClient()
{
  az_iot_hub_client_options options = az_iot_hub_client_options_default();
  options.user_agent = AZ_SPAN_FROM_STR(AZURE_SDK_CLIENT_USER_AGENT);

  if (az_result_failed(az_iot_hub_client_init(
          &client,
          az_span_create((uint8_t*)host, strlen(host)),
          az_span_create((uint8_t*)device_id, strlen(device_id)),
          &options)))
  {
    Logger.Error("Failed initializing Azure IoT Hub client");
    return;
  }

  size_t client_id_length;
  if (az_result_failed(az_iot_hub_client_get_client_id(
          &client, mqtt_client_id, sizeof(mqtt_client_id) - 1, &client_id_length)))
  {
    Logger.Error("Failed getting client ID");
    return;
  }

  if (az_result_failed(az_iot_hub_client_get_user_name(
          &client, mqtt_username, sizeof(mqtt_username), NULL)))
  {
    Logger.Error("Failed getting MQTT username");
    return;
  }

  Logger.Info("Client ID: " + String(mqtt_client_id));
  Logger.Info("Username: " + String(mqtt_username));
}

static void generateTelemetryPayload()
{
  // Populate the global telemetry_payload buffer
  snprintf(
      telemetry_payload,
      sizeof(telemetry_payload),
      "{ \"msgCount\": %lu, \"Humidity\": %.2f, \"Pressure\": %.2f, \"Temperature\": %.2f }",
      telemetry_send_count++,
      bme.readHumidity(),
      bme.readPressure() / 100.0F,
      bme.readTemperature());
}

static void sendTelemetry()
{
  Logger.Info("Sending telemetry ...");

  if (az_result_failed(az_iot_hub_client_telemetry_get_publish_topic(
          &client, NULL, telemetry_topic, sizeof(telemetry_topic), NULL)))
  {
    Logger.Error("Failed az_iot_hub_client_telemetry_get_publish_topic");
    return;
  }

  // Generate and publish the telemetry payload
  generateTelemetryPayload();
  int msg_id = esp_mqtt_client_publish(
      mqtt_client,
      telemetry_topic,
      telemetry_payload,
      strlen(telemetry_payload),
      MQTT_QOS1,
      DO_NOT_RETAIN_MSG);

  if (msg_id == 0)
  {
    Logger.Error("Failed publishing");
  }
  else
  {
    Logger.Info("Message published successfully. msg_id=" + String(msg_id));
  }
}

// ------------------------------------------------------
// MQTT Event Handler
// ------------------------------------------------------
static void mqtt_event_handler(void* handler_args,
                               esp_event_base_t base,
                               int32_t event_id,
                               void* event_data)
{
  esp_mqtt_event_handle_t event = (esp_mqtt_event_handle_t)event_data;
  switch ((esp_mqtt_event_id_t)event_id)
  {
    case MQTT_EVENT_CONNECTED:
    {
      Logger.Info("MQTT_EVENT_CONNECTED");
      // Subscribe to device-bound messages
      char devicebound_topic[128];
      snprintf(devicebound_topic, sizeof(devicebound_topic), "devices/%s/messages/devicebound/#", device_id);
      esp_mqtt_client_subscribe(mqtt_client, devicebound_topic, MQTT_QOS1);
      Logger.Info("Subscribed to topic: " + String(devicebound_topic));
      break;
    }
    case MQTT_EVENT_DISCONNECTED:
      Logger.Error("MQTT_EVENT_DISCONNECTED");
      break;
    case MQTT_EVENT_SUBSCRIBED:
      Logger.Info("MQTT_EVENT_SUBSCRIBED, msg_id: " + String(event->msg_id));
      break;
    case MQTT_EVENT_UNSUBSCRIBED:
      Logger.Info("MQTT_EVENT_UNSUBSCRIBED, msg_id: " + String(event->msg_id));
      break;
    case MQTT_EVENT_PUBLISHED:
      Logger.Info("MQTT_EVENT_PUBLISHED, msg_id: " + String(event->msg_id));
      break;
    case MQTT_EVENT_DATA:
    {
      Logger.Info("MQTT_EVENT_DATA");
      Logger.Info("Topic: " + String(event->topic, event->topic_len));
      Logger.Info("Data: " + String(event->data, event->data_len));
      break;
    }
    case MQTT_EVENT_ERROR:
    {
      Logger.Error("MQTT_EVENT_ERROR");
      if (event->error_handle->error_type == MQTT_ERROR_TYPE_ESP_TLS)
      {
        Logger.Error("Last ESP-TLS error code: 0x" + String(event->error_handle->esp_tls_last_esp_err, HEX));
        Logger.Error("TLS stack error code: 0x" + String(event->error_handle->esp_tls_stack_err, HEX));
      }
      else if (event->error_handle->error_type == MQTT_ERROR_TYPE_CONNECTION_REFUSED)
      {
        Logger.Error("Connection refused error: 0x" + String(event->error_handle->connect_return_code, HEX));
      }
      else
      {
        Logger.Error("Unknown error type: " + String(event->error_handle->error_type));
      }
      break;
    }
    case MQTT_EVENT_BEFORE_CONNECT:
      Logger.Info("MQTT_EVENT_BEFORE_CONNECT");
      break;
    default:
      Logger.Error("Unhandled MQTT event id: " + String(event_id));
      break;
  }
}

// ------------------------------------------------------
// MQTT Initialization
// ------------------------------------------------------
static int initializeMqttClient()
{
#ifndef IOT_CONFIG_USE_X509_CERT
  if (sasToken.Generate(SAS_TOKEN_DURATION_IN_MINUTES) != 0)
  {
    Logger.Error("Failed generating SAS token");
    return 1;
  }
#endif

  esp_mqtt_client_config_t mqtt_config;
  memset(&mqtt_config, 0, sizeof(mqtt_config));

  mqtt_config.broker.address.uri = mqtt_broker_uri;
  mqtt_config.broker.address.port = mqtt_port;
  mqtt_config.credentials.client_id = mqtt_client_id;
  mqtt_config.credentials.username  = mqtt_username;

#ifdef IOT_CONFIG_USE_X509_CERT
  Logger.Info("MQTT client using X509 Certificate authentication");
  mqtt_config.credentials.authentication.certificate = IOT_CONFIG_DEVICE_CERT;
  mqtt_config.credentials.authentication.key         = IOT_CONFIG_DEVICE_CERT_PRIVATE_KEY;
#else
  mqtt_config.credentials.authentication.password = (const char*)az_span_ptr(sasToken.Get());
#endif

  mqtt_config.session.keepalive              = 30;
  mqtt_config.session.disable_clean_session  = 0;
  mqtt_config.network.disable_auto_reconnect = false;
  mqtt_config.broker.verification.certificate = (const char*)ca_pem;

  mqtt_client = esp_mqtt_client_init(&mqtt_config);
  if (mqtt_client == NULL)
  {
    Logger.Error("Failed creating MQTT client");
    return 1;
  }

  // Register event handler
  esp_err_t err = esp_mqtt_client_register_event(
      mqtt_client, (esp_mqtt_event_id_t)ESP_EVENT_ANY_ID, mqtt_event_handler, mqtt_client);
  if (err != ESP_OK)
  {
    Logger.Error("Failed registering MQTT event handler");
    return 1;
  }

  // Start the client
  esp_err_t start_result = esp_mqtt_client_start(mqtt_client);
  if (start_result != ESP_OK)
  {
    Logger.Error("Could not start MQTT client; error code: " + String(start_result));
    return 1;
  }

  Logger.Info("MQTT client started");
  return 0;
}

// ------------------------------------------------------
// Connection Establishment
// ------------------------------------------------------
static void establishConnection()
{
  connectToWiFi();
  initializeTime();
  initializeIoTHubClient();
  (void)initializeMqttClient();
}

// ------------------------------------------------------
// Arduino Setup/Loop
// ------------------------------------------------------
void setup()
{
  Serial.begin(115200);

  // Connect to Azure IoT
  establishConnection();

  // Init BME280 sensor
  Wire.begin();
  if (!bme.begin(I2C_ADDRESS))
  {
    Serial.println("Could not find a valid BME280 sensor!");
    while (true)
      ;
  }
  Serial.println("BME280 sensor initialized.");
}

void loop()
{
  // Ensure WiFi is connected
  if (WiFi.status() != WL_CONNECTED)
  {
    connectToWiFi();
  }
#ifndef IOT_CONFIG_USE_X509_CERT
  // If SAS token is expired, regenerate and re-init MQTT
  else if (sasToken.IsExpired())
  {
    Logger.Info("SAS token expired; reconnecting with a new one.");
    esp_mqtt_client_destroy(mqtt_client);
    initializeMqttClient();
  }
#endif
  else if (millis() > next_telemetry_send_time_ms)
  {
    sendTelemetry();
    next_telemetry_send_time_ms = millis() + TELEMETRY_FREQUENCY_MILLISECS;
  }
}
