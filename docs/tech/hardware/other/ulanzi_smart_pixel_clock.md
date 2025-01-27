# Ulanzi Smart Pixel Clock

I played with the Ulanzi Smart Pixel Clock and flashed the custom firmware [awtrix3](https://github.com/Blueforcer/awtrix3)

Setup the Smart Pixel Clock e.g. WIFI password, IP of the MQTT broker (the system you will be sending commands from) and update the time zone (e.g. Europe/Berlin = CET-1CEST,M3.5.0,M10.5.0/3()

For details on the MQTT API check [this documentation](https://blueforcer.github.io/awtrix3/#/api).

Here are some examples with curl:

## Control device using Curl

Some basic commands to get started:

```sh
curl -X POST --data '{"color":[0,0,0]}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/indicator1'

curl -X POST --data '{"color":[255,0,0],"blink":1000}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/indicator1'

curl -X POST --data '{"text":"LOL 0xfab1","rainbow":true}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/notify'

curl -X POST --data '{"text":"Hello World"}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/notify'
```

Now some more examples :)

Simple Notification

```sh
curl -X POST --data '{"text":"Hello Awtrix!","duration":10}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/notify'
```

Rainbow Text Notification

```sh
curl -X POST --data '{"text":"Rainbow Notification!","rainbow":true,"duration":15}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/notify'
```

Set Indicator 1 to Red

```sh
curl -X POST --data '{"color":[255,0,0]}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/indicator1'
```

Blink Indicator 2 with Green

```sh
curl -X POST --data '{"color":[0,255,0],"blink":500}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/indicator2'
```

Fade Indicator 3 with Blue

```sh
curl -X POST --data '{"color":[0,0,255],"fade":1000}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/indicator3'
```

Set Mood Light with Warm Temperature

```sh
curl -X POST --data '{"brightness":150,"kelvin":3000}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/moodlight'
```

Set Mood Light with Custom Color

```sh
curl -X POST --data '{"brightness":200,"color":"#FFA500"}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/moodlight'
```

Disable Mood Light

```sh
curl -X POST --data '{}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/moodlight'
```

Turn Off the Matrix

```sh
curl -X POST --data '{"power":false}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/power'
```

Put Device to Sleep for 30 Seconds

```sh
curl -X POST --data '{"sleep":30}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/sleep'
```

Create a Custom App

```sh
curl -X POST --data '{"text":"Custom App Example","icon":1,"duration":10}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/custom?name=myapp'
```

Update the Custom App

```sh
curl -X POST --data '{"text":"Updated App Content!","color":"#00FF00"}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/custom?name=myapp'
```

Remove the Custom App

```sh
curl -X POST --data '{}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/custom?name=myapp'
```

Draw a Circle and Rectangle

```sh
curl -X POST --data '{"draw": [{"dc":[10,10,5,"#FF0000"]}, {"dr":[15,15,10,5,"#00FF00"]}]}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/notify'
```

Play a Predefined Sound

```sh
curl -X POST --data '{"sound":"alarm"}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/sound'
```

Play an RTTTL Sound String

```sh
curl -X POST --data '{"rtttl":"Mario:d=4,o=5,b=140:e6,8e6,8e6,8c6,8e6,8g6"}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/rtttl'
```

Reboot the Device

```sh
curl -X POST -H 'Content-Type: application/json' 'http://1.2.3.4/api/reboot'
```

Perform a Factory Reset

```sh
curl -X POST -H 'Content-Type: application/json' 'http://1.2.3.4/api/erase'
```

Reset Settings

```sh
curl -X POST -H 'Content-Type: application/json' 'http://1.2.3.4/api/resetSettings'
```

Navigate to Next App

```sh
curl -X POST -H 'Content-Type: application/json' 'http://1.2.3.4/api/nextapp'
```

Switch to a Specific App

```sh
curl -X POST --data '{"name":"Time"}' -H 'Content-Type: application/json' 'http://1.2.3.4/api/switch'
```

## Message Tool

I wrote a simple python script to write messages to a selected device:

### Prepare

Install these dependencies in your environment

```sh
pip install pyinstaller tkinter
```

### Script

This is the script named "screenmessage.py":

```sh
import tkinter as tk
import requests

def send_notification():
    message = message_entry.get()
    selected_ip = ip_var.get()
    url = f"http://{selected_ip}/api/notify"
    headers = {"Content-Type": "application/json"}
    data = {"text": message, "duration": 10}

    try:
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            output_label.config(text=f"Success: {response.text}")
        else:
            output_label.config(text=f"Error {response.status_code}: {response.text}")
    except requests.RequestException as e:
        output_label.config(text=f"Request failed: {e}")

def clear_message():
    # Clears the entry field and output label
    message_entry.delete(0, tk.END)
    output_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Notification Sender")

# Create a dropdown menu to select the IP address
ip_var = tk.StringVar(value="1.1.1.1")  # Default IP
ip_options = [
    ("Device1", "1.1.1.1"),
    ("Device2", "1.1.1.2")
]
ip_label = tk.Label(root, text="Select IP Address:")
ip_label.pack(pady=5)

# Dropdown with labeled options
def update_dropdown():
    menu = ip_dropdown['menu']
    menu.delete(0, 'end')
    for name, ip in ip_options:
        menu.add_command(label=f"{name} ({ip})", command=lambda value=ip: ip_var.set(value))
ip_dropdown = tk.OptionMenu(root, ip_var, "")
ip_dropdown.pack(pady=5)
update_dropdown()

# Create a label and an entry field to input the message
message_label = tk.Label(root, text="Enter your message:")
message_label.pack(pady=5)

message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

# Create a button to send the notification
send_button = tk.Button(root, text="Send Notification", command=send_notification, padx=10, pady=5)
send_button.pack(pady=10)

# Create a second button to clear the message
clear_button = tk.Button(root, text="Clear Message", command=clear_message, padx=10, pady=5)
clear_button.pack(pady=10)

# Create a label to display the output
output_label = tk.Label(root, text="", wraplength=400, justify="left")
output_label.pack(pady=10)

# Start the main event loop
root.mainloop()
```

### Build

Run this command to build the executable for windows:

```sh
pyinstaller --onefile --noconsole screenmessage.py
```

The executable will be in the subfolder `dist` named `screenmessage.exe`.
