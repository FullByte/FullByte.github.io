# Print and Scan

For printing and scanning I personally prefer a laser printer with LAN support. There should be no need to install the vendors drivers and extra software; simply go with the OS printer drivers identified for your device.

## Windows

For scanning on windows I prefer [NAPS2](https://www.naps2.com).

Alternatively try [VueScan](https://www.hamrick.com/).

## Linux

### Print

Usually there is no need to install specific drivers to print. Use the [HP print and scan drivers for linux](https://developers.hp.com/hp-linux-imaging-and-printing) if you have issues with your printer. This is required for scanning.

Steps to get HP Printers running on Ubuntu 20.04:

- Download the latest [dhplip rivers](https://sourceforge.net/projects/hplip/files/). Check this [overview](https://developers.hp.com/hp-linux-imaging-and-printing/gethplip) if link is not working.
- Run the script with ```sh hplip-<version>.run``` and go throgh the steps.
- Download the latest [hplip plugin](https://developers.hp.com/hp-linux-imaging-and-printing/plugins)
- Run the script with ```sh hplip-<version>.run```
- Now run the HO Device Manger or your scan tool of choice e.g. SimpleScan or gscan2pdf.

### Scan

Install SimpleScan

``` sh
sudo apt-get install simple-scan

gsettings set org.gnome.SimpleScan jpeg-quality 85
gsettings set org.gnome.SimpleScan brightness -10
gsettings set org.gnome.SimpleScan contrast 25 
```

Install gscan2pdf

``` sh
sudo apt-get install gscan2pdf
sudo apt-get install tesseract-ocr-deu 
```
