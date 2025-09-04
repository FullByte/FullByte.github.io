# HackRF One

Get the lateset tools and software for HackRF here: <https://github.com/greatscottgadgets/hackrf/releases>
To upgrade to this release, you must update libhackrf and hackrf-tools on your host computer.
You must also update firmware on your HackRF.

## Kali

To install the Kali Linux Metapackages "kali-tools-sdr" which contains Software-Defined Radio tools run ```kali-tweaks``` and choose the sdr package.

There is a specific app available for the hackrf:

``` sh
sudo apt install hackrf
```

This package contains a set of command line utilities:

- hackrf_clock: HackRF clock configuration utility
- hackrf_cpldjtag: program CLPD
- hackrf_debug: chip register read/write/config tool
- hackrf_info: probe device and show configuration
- hackrf_operacake: control of operacake board via hackrf
- hackrf_spiflash: read and write flash data from file.
- hackrf_sweep: control frequency sweep of hackrf
- hackrf_transfer: file based transmit and receive sdr

To see if hackrf one can be used run:

``` sh
sudo hackrf_info 
```

## Firmware

The HackRF hardware needs a firmware to run. This package contains a number of firmware images that may be programmed into the HackRF hardware using the ```hackrf_spiflash -w``` command or ```dfu-util```.

``` sh
sudo apt install hackrf-firmware
```

## Regular Firmware Update

To update the firmware on a working HackRF One, use the hackrf_spiflash program.

Get the latest firmware `hackrf_one_usb.bin` (should be in subfolder `firmware-bin`) from the [latest release package](https://github.com/greatscottgadgets/hackrf/releases/latest) and run:

``` sh
hackrf_spiflash -w hackrf_one_usb.bin
```

### Recovering the SPI Flash Firmware for HackRF One r1–r4

DFU boot mode is normally only needed if the firmware is not working properly or has never been installed.

The LPC4330 microcontroller on HackRF is capable of booting from several different code sources. By default, HackRF boots from SPI flash memory (SPIFI). It can also boot HackRF in DFU (USB) boot mode. In DFU boot mode, HackRF will enumerate over USB, wait for code to be delivered using the DFU (Device Firmware Update) standard over USB, and then execute that code from RAM. The SPIFI is normally unused and unaltered in DFU mode.

Make sure ```dfu-util``` is installed:

``` sh
sudo apt-get install dfu-util
```

start the HackRF in DFU boot mode:

- Disconnect the HackRF from the computer
- Press and Hold the DFU (Device Firmware Update) Button
- Hold down the DFU button while powering it on or while pressing and releasing the RESET button.
- Release the DFU button after the 3V3 LED illuminates. The 1V8 LED should remain off. At this point HackRF One is ready to receive firmware over USB.
- Verify DFU Mode: Run ```dfu-util --list``` This should show the device in DFU mode if it’s correctly entered

Get the latest firmware from the [latest release package](https://github.com/greatscottgadgets/hackrf/releases/latest).
You should only use a firmware image with a filename ending in ".dfu" over DFU, not firmware ending in ".bin".
The latest firmware `hackrf_one_usb.dfu` (should be in subfolder `firmware-bin`)

Check if the USB device is visible with ```lsusb```.  Mine showed up as:

``` sh
Bus 003 Device 004: ID 1fc9:000c NXP Semiconductors LPC4330FET180 [ARM Cortex M4 + M0] (device firmware upgrade mode)
```

Run `dfu-util` to get the device ID (in this case: 1fc9:000c):

``` sh
dfu-util 0.11

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2021 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

Found DFU: [1fc9:000c] ver=0100, devnum=4, cfg=1, intf=0, path="3-2", alt=0, name="DFU", serial="ABCD"
```

With the downloaded firmware use dfu-util to flash the firmware. Make sure to use the correct device-id:

``` sh
dfu-util --device 1fc9:000c --alt 0 --download hackrf_one_usb.dfu 
```

Example output:

``` sh
dfu-util 0.11

Copyright 2005-2009 Weston Schmidt, Harald Welte and OpenMoko Inc.
Copyright 2010-2021 Tormod Volden and Stefan Schmidt
This program is Free Software and has ABSOLUTELY NO WARRANTY
Please report bugs to http://sourceforge.net/p/dfu-util/tickets/

dfu-util: Warning: DFU suffix CRC does not match
dfu-util: A valid DFU suffix will be required in a future dfu-util release
Opening DFU capable USB device...
Device ID 1fc9:000c
Device DFU version 0100
Claiming USB DFU Interface...
Setting Alternate Interface #0 ...
Determining device status...
DFU state(2) = dfuIDLE, status(0) = No error condition is present
DFU mode device DFU version 0100
Device returned transfer size 2048
Copying data from PC to DFU device
```

FYI: Checking the device with `lsusb` shows that the device is now known as HackRF:

``` sh
Bus 003 Device 005: ID 1d50:6089 OpenMoko, Inc. Great Scott Gadgets HackRF One SDR
```
