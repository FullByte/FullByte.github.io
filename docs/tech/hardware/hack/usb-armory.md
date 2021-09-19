# USB Armory

Source Image: <https://dev.inversepath.com/download/usbarmory/>

## Windows 10 Driver Issue

Driver is installed but found as "Serial" "USB device(COM3)" in the device manager
"Update" the driver an use this instead: <http://web1.moddevices.com/shared/mod-duo-rndis.zip>
Alternative Guide: <https://github.com/ev3dev/ev3dev/wiki/Setting-Up-Windows-USB-Ethernet-Networking>

## Connect to USB armory

A new network device should show up
Change settings of IPv4 to:

```shell
IP: 10.0.0.10
Subnet: 255.0.0.0
Gateway: 10.0.0.2
```

Run ssh to 10.0.0.1
Default credentials are:

- User: usbamory
- Password: usbamory

Configure USB armory

- add internet access
- run updates
- configure for usage...
