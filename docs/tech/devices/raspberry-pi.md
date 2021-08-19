# Raspberry Pi

## Basics

Raspberry Config

```shell
raspi-config
```

Raspberry Config File

```shell
/boot/config.txt
hdmi_force_hotplug=1
hdmi_drive=2
```

### Find Pi with an ARP scan filtering for known Pi MAC Addresses

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

### Desktop

**Widevine** enables to stream content from popular websites such as Netflix, Amazon Prime, Hulu, HBO Go, Disney+, Spotify, Pandora and more, using the default Chromium web browser:

```shell
sudo apt install libwidevinecdm0
```

### Retro Gaming Stations

All are good choices. Pick the one best for your hardware/roms:

- retropie: <https://retropie.org.uk/>
- recalbox: <https://gitlab.com/recalbox/recalbox>
- EmuELEC: <https://github.com/EmuELEC/EmuELEC/>
- batocera: <https://batocera.org/>


## Projects

Some Raspberry Pi projects. I added a year since some projects are old and will not be maintained.

### PiBoy (2021)

WIP

### Setup 7 Inch Car Color Monitor (2016)

First Retro Gaming Pi with Raspberry Pi 1 using analog video output to a 7" Car Color Monitor.

Edit config.txt:

```shell
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

### Bitcoin miner using ASIC Chips attached via USB (2015)

#### Install and configure BFGMiner

Install and build

```shell
git clone https://github.com/luke-jr/bfgminer
cd bfgminer
./autogen.sh
./configure
make
```

For Raspberry Pi:

```shell
sudo nano /boot/cmdline.txt
Add "slub_debug=FP" to the code at the end of the first line (same line)
```

Configure bfgminer

```shell
sudo ./bfgminer -S antminer:all -o stratum.bitcoin.cz:3333 -u FullByte.worker1 -p xZ7du2qE --set-device antminer:freq=4F02
```

Add to autostart

```shell
sudo nano /etc/rc.local
```

Add the following lines at the bottom but above "exit 0" :

```shell
cd /home/pi/PiMiner
sudo python PiMiner.py &

cd /home/pi/bfgminer
#BITCOIN.CZ
#sudo screen -S bfgminer -d -m sudo ./bfgminer -S antminer:all -o stratum.bitcoin.cz$
#CEX.IO
#sudo screen -S bfgminer -d -m sudo ./bfgminer -S antminer:all -o stratum+tcp://nl1.$
#BTC GUILD
sudo screen -S bfgminder -d -m sudo ./bfgminer -S antminer:all -o eu-stratum.bt$
```

Now with the following command you can access the bfgminer screen:

```shell
sudo screen -r
```

Kill mining task

```shell
ps aux | grep PiMiner
sudo kill <processID>
ps aux | grep bfgminer
sudo kill <processID>
```

AntMiner U1 over clocking Settings Frequency

```
Hash Rate	(GH/s) 	–bmsc-freq Setting
200 		1.6 	0781 (Default)
225 		1.8 		0881
250 		2.0 		0981
275 		2.2 		0A81
```

#### Setup GPIO for visual output on attached LCD board

Run the following commands

```shell
sudo apt update
sudo apt install git
git clone http://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
sudo apt install python-dev
sudo apt install python-rpi.gpio
```

Edit modules

```shell
sudo nano /etc/modules
i2c-bcm2708
i2c-dev
```

check for newest version

```shell
sudo apt install python-smbus
sudo apt install i2c-tools
```

IF this file exists (/etc/modprobe.d/raspi-blacklist.conf) do...

Comment out these 2 lines:

```shell
sudo nano /etc/modprobe.d/raspi-blacklist.conf
#blacklist spi-bcm2708
#blacklist i2c-bcm2708
```

Test connection

```shell
sudo i2cdetect -y 1
```
