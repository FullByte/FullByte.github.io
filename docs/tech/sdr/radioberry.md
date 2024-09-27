# Radioberry

## Install Radioberry

Base OS used is Rasperry Pi OS (64 Bit).

I installed these dependancies:

``` sh
sudo apt-get install git libpulse-dev libgtk-3-dev libasound2-dev libcurl4-openssl-dev libusb-1.0-0-dev raspberrypi-kernel-headers device-tree-compiler pigpio

cd /tmp
git clone --depth=1 https://github.com/pa3gsb/Radioberry-2.x.git
cd Radioberry-2.x
git submodule update --init --recursive --depth=1
```

And built and installed the program:

``` sh
make -j$(nproc)
sudo make install FPGATYPE=CL016
```
