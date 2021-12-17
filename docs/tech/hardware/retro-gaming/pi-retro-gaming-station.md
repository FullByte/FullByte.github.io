# Pi Gaming Station

This project is from 2016 so information may be outdated.

## Retro Gaming Stations

All are good choices. Pick the one best for your hardware/roms:

- retropie: <https://retropie.org.uk/>
- recalbox: <https://gitlab.com/recalbox/recalbox>
- EmuELEC: <https://github.com/EmuELEC/EmuELEC/>
- batocera: <https://batocera.org/>

## Raspberry Pi Basics

Raspberry Config

 ```sh
raspi-config
```

Raspberry Config File

 ```sh
/boot/config.txt
hdmi_force_hotplug=1
hdmi_drive=2
```

## Setup 7 Inch Car Color Monitor

First Retro Gaming Pi with Raspberry Pi 1 using analog video output to a 7" Car Color Monitor.

Edit config.txt:

 ```sh
# uncomment the following to adjust overscan. Use positive numbers if console
# goes off screen, and negative if there is too much border
overscan_left=22
overscan_right=38
overscan_top=-22
overscan_bottom=-24

# uncomment to force a console size. By default it will be display's size minus
# overscan.
framebuffer_width=480
framebuffer_height=300

# uncomment if hdmi display is not detected and composite is being output
#hdmi_force_hotplug=1
hdmi_ignore_hotplug=1

# uncomment for composite PAL
sdtv_mode=2
sdtv_aspect=3
```

For more options see <http://elinux.org/RPi_config.txt>
