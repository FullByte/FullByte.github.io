# Raspberry Pi

## Display Rotation

Edit ```/boot/config.txt```

``` sh
display_rotate=0
display_rotate=1 # 90 degress
display_rotate=2 # 180 degrees
display_rotate=3 # 270 degrees
```

## Headless Setup

Enable SSH by placing a file named "ssh" onto the boot partition of the SD card.

``` sh
touch /path/to/sd/card/volume/ssh
```
