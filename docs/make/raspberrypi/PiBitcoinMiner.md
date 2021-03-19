# Raspberry Pi Bitcoin minder using ASIC Chips attached via USB

## Install and configure BFGMiner

### Install bfgminer

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

### Configure bfgminer

```shell
sudo ./bfgminer -S antminer:all -o stratum.bitcoin.cz:3333 -u FullByte.worker1 -p xZ7du2qE --set-device antminer:freq=4F02
```

### Add to autostart

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

### Now with the following command you can access the bfgminer screen:

```shell
sudo screen -r
```

### Kill mining task

```shell
ps aux | grep PiMiner
sudo kill <processID>
ps aux | grep bfgminer
sudo kill <processID>
```

### AntMiner U1 over clocking Settings Frequency

Hash Rate	(GH/s) 	–bmsc-freq Setting
200 		1.6 	0781 (Default)
225 		1.8 		0881
250 		2.0 		0981
275 		2.2 		0A81

## Setup GPIO for visual output on attached LCD board

### Run the following commands

```shell
sudo apt update
sudo apt install git
git clone http://github.com/adafruit/Adafruit-Raspberry-Pi-Python-Code.git
sudo apt install python-dev
sudo apt install python-rpi.gpio
```

**Edit modules**

```shell
sudo nano /etc/modules
i2c-bcm2708
i2c-dev
```

**check for newest version**

```shell
sudo apt install python-smbus
sudo apt install i2c-tools
```

**IF this file exists (/etc/modprobe.d/raspi-blacklist.conf) do...**

Comment out these 2 lines:

```shell
sudo nano /etc/modprobe.d/raspi-blacklist.conf
#blacklist spi-bcm2708
#blacklist i2c-bcm2708
```

**Test connection**

```shell
sudo i2cdetect -y 1
```
