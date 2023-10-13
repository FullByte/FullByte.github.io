# usbipd

| What    | Where                                                               |
|---------|---------------------------------------------------------------------|
| Source  | <https://github.com/microsoft/winget-cli>                           |
| Docs    | <https://learn.microsoft.com/de-de/windows/package-manager/winget/> |
| Install | `winget install usbipd`                                             |

## Setup

### Prerequisites on Windows

- Make sure your WSL is up to date: ```wsl --update```
- Show currently available WSL distros: ```wsl --list --verbose```
- Set default: ```wsl --setdefault Ubuntu-20.04```
- And make sure the chosen WSL distro is running

### Prerequisites for WSL

``` sh
sudo apt install build-essential flex bison libssl-dev libelf-dev libncurses-dev autoconf libudev-dev libtool linux-tools-virtual hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip `ls /usr/lib/linux-tools/*/usbip | tail -n1` 20
```

on Windows, attach USB Device to WSL :

- Get USB devices with: ```usbipd wsl list```
- Select correct device and add it to WSL: ```usbipd wsl attach -b=<BUSID> --auto-attach```

Now in WSL view and test USB device:

- View USB devices: ```lsusb -t```
- Make USB device writeable (Change username and USB1 according to your setup): ```sudo chown fab1 /dev/ttyUSB1```
- Test if writing to USB works: ```echo Test > /dev/ttypUSB1```
