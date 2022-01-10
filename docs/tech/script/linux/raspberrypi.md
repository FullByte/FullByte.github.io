# Raspberry Pi

## Config

### Display Rotation

Edit ```/boot/config.txt```

``` sh
display_rotate=0
display_rotate=1 # 90 degress
display_rotate=2 # 180 degrees
display_rotate=3 # 270 degrees
```

### Headless Setup

Enable SSH by placing a file named "ssh" onto the boot partition of the SD card.

``` sh
touch /path/to/sd/card/volume/ssh
```

## Helper

### Find Raspberry Pi in network

Find Pi with an ARP scan filtering for known Pi MAC Addresses

From windows:

```cmd
arp -a | findstr b8-27-eb
```

From linux

``` sh
arp-scan --localnet --interface=eth0 | grep b8:27:eb
arp-scan --localnet --interface=wlan0 | grep b8:27:eb
```