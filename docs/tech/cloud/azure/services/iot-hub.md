# IoT Hub

## Getting started

Install iot extension

```shell
az extension add --name azure-iot
```

add device:

```shell
az iot hub device-identity create -d simDevice -n iothub.azure-devices.net
```

simulate activity:

```shell
az iot device simulate -d simDevice -n iothub.azure-devices.net
```

View Events:

```shell
az iot hub monitor-events --output table -p all -n iothub.azure-devices.net
```

Example message with no properties

```json
{ 'Message Properties': { 'content_encoding': 'utf-8',
                          'content_type': 'text/plain; charset=UTF-8'},
  'Payload': 'lol',
  'Topic': '/devices/simDevice/messages/devicebound'}
```

Example message with one property

```json
{ 'Message Properties': { 'content_encoding': 'utf-8',
                          'content_type': 'text/plain; charset=UTF-8',
                          'key_test': 'value_test'},
  'Payload': 'test',
  'Topic': '/devices/simDevice/messages/devicebound'}
 ```

Example message with multiple properties

```json
{ 'Message Properties': { '1': '1',
                          '2': '2',
                          'content_encoding': 'utf-8',
                          'content_type': 'text/plain; charset=UTF-8',
                          'key_test': 'value_test'},
  'Payload': 'multi test',
  'Topic': '/devices/simDevice/messages/devicebound'}
```

## Ubuntu Demo

Requirements

```py
pip3 install azure-iot-device
```

```py
import time
import random
from azure.iot.device import IoTHubDeviceClient, Message

# Replace with your device's connection string from the IoT Hub device details page (see devices)
CONNECTION_STRING = "HostName=<your-iot-hub-hostname>;DeviceId=<your-device-id>;SharedAccessKey=<your-device-key>"

# Define a telemetry format
MSG_TXT = '{{"temperature": {temperature}, "humidity": {humidity}}}'

def main():
    # Create a device client
    device_client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    # Connect to IoT Hub
    print("Connecting to IoT Hub...")
    device_client.connect()
    print("Connected.")

    try:
        while True:
            # Generate random telemetry data
            temperature = 20.0 + (5.0 * random.random())
            humidity = 60.0 + (10.0 * random.random())

            # Create the message by formatting the JSON payload
            msg_text_formatted = MSG_TXT.format(temperature=temperature, humidity=humidity)
            message = Message(msg_text_formatted)

            # (Optional) Add custom application properties if needed
            # message.custom_properties["sensortype"] = "bme280"

            print("Sending message: {}".format(message))
            device_client.send_message(message)
            print("Message successfully sent.")

            # Wait some time before sending the next message
            time.sleep(5)
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    finally:
        device_client.disconnect()

if __name__ == "__main__":
    main()
```
