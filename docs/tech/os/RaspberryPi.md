# Raspberry Pi

## Basics

**Raspberry Config**

```shell
raspi-config
```

**Raspberry Config File**

```shell
/boot/config.txt
hdmi_force_hotplug=1
hdmi_drive=2
```

## Find Pi with an ARP scan filtering for known Pi MAC Addresses

Find Pi with an ARP scan filtering for known Pi MAC Addresses

From windows:

```cmd
arp -a | findstr b8-27-eb
```

From linux

```shell
arp-scan --localnet --interface=eth0 | grep b8:27:eb
arp-scan --localnet --interface=wlan0 | grep b8:27:eb
```

## Desktop

**Widevine** enables to stream content from popular websites such as Netflix, Amazon Prime, Hulu, HBO Go, Disney+, Spotify, Pandora and more, using the default Chromium web browser:

```shell
sudo apt install libwidevinecdm0
```

## Retro Gaming Stations

All are good choices. Pick the one best for your hardware/roms:

- retropie: <https://retropie.org.uk/>
- recalbox: <https://gitlab.com/recalbox/recalbox>
- EmuELEC: <https://github.com/EmuELEC/EmuELEC/>
- batocera: <https://batocera.org/>
