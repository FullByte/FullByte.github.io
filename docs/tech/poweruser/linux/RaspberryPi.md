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

## Find Pi with an ARP scan filtering for known Pi MAC Adresses

Find Pi with an ARP scan filtering for known Pi MAC Adresses

From windows:

arp -a | findstr b8-27-eb

From linux

arp-scan --localnet --interface=eth0 | grep b8:27:eb
arp-scan --localnet --interface=wlan0 | grep b8:27:eb
