#pragma once

#define IOT_CONFIG_WIFI_SSID ""
#define IOT_CONFIG_WIFI_PASSWORD ""

// Use device key if not using certificates
#ifdef IOT_CONFIG_USE_X509_CERT
    #define IOT_CONFIG_DEVICE_CERT "Device Certificate"
    #define IOT_CONFIG_DEVICE_CERT_PRIVATE_KEY "Device Certificate Private Key"
#endif    
#ifndef IOT_CONFIG_USE_X509_CERT
    #define IOT_CONFIG_DEVICE_KEY ""
#endif

#define IOT_CONFIG_IOTHUB_FQDN ".azure-devices.net"
#define IOT_CONFIG_DEVICE_ID ""

#define AZ_SDK_VERSION_STRING "1.0.0"
#define AZURE_SDK_CLIENT_USER_AGENT "c%2F" AZ_SDK_VERSION_STRING "(ard;esp32)"
#define TELEMETRY_FREQUENCY_MILLISECS 60000