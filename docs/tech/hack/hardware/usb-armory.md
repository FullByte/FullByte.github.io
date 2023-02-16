# USB Armory

<https://inversepath.com/usbarmory>
<https://github.com/usbarmory/armory-boot>
<https://groups.google.com/g/usbarmory?pli=1>

## Windows 10 Driver Issue

Driver is installed but found as "Serial" "USB device(COM3)" in the device manager
"Update" the driver an use this instead: <http://web1.moddevices.com/shared/mod-duo-rndis.zip>

## Connect to USB armory

A new network device should show up
Change settings of IPv4 to:

``` sh
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
