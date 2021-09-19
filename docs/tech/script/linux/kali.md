# Kali

Install and config Kali

## Basic Config

[Kali's Default Credentials](https://www.kali.org/docs/introduction/default-credentials/)

### Update OS

Set the password for root and switch to root

```shell
sudo passwd root
su root
```

Run this once on old Kali versions and run this as root:

```shell
sudo apt install gcc-8-base
sudo wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add
sudo dpkg --configure -a
```

Switch back to your user e.g. fab1

```shell
su fab1
```

Run an update

```shell
sudo apt update && sudo apt -y full-upgrade && sudo apt -y autoremove && sudo apt -y autoclean
```

Install more tools (alt install ```kali-linux-default``` or ```kali-linux-large```)

```shell
sudo apt-get install kali-linux-everything
```

Options to get current version

```shell
lsb_release -a
cat /etc/os-release
hostnamectl
/proc/version
```

## Add new user

Add new user e.g. 0xfab1 with full privileges:

```shell
sudo useradd -m 0xfab1
sudo passwd 0xfab1
sudo usermod -a -G sudo 0xfab1
sudo chsh -s /bin/bash 0xfab1
su 0xfab1
whoami
```

## Set german keyboard

```shell
setxkbmap -layout de
```

## Enlargen Disk

Use fdisk to enlargen ```/dev/sda``` (e.g. when providing more disk space to the VM)

```shell
df -h # check current space
sudo fdisk /dev/sda # run fdisk to resize the partition
-> u # change the units to sectors
-> p # list the partitions details
-> d # delete the partition
-> n # create a new partition
-> p # create a primary partition
-> 1 # create first partition
-> (default) # starting sector  
-> (default) # ending sector
-> w # Write the partition
sudo resize2fs /dev/sda1
sudo reboot
df -h # verfiy space has increased
```

### WiFi issues

Check the NetworkManager.conf

```shell
sudo nano /etc/NetworkManager/NetworkManager.conf
```

If "managed=false" set this to true

```shell
[ifupdown]
managed=true
```

now save the file and restart the network manager.

```shell
systemctl restart NetworkManager
```

### Monitor Mode

Search for network devices in Monitor Mode and Access Points

```shell
iwconfig 2>/dev/null | grep "Mode\\:Monitor" | awk '{print $1}'
iwconfig 2>&1 | sed -n -e 's/^.\*Access Point: //p'
```

### Get a GUI

Run ```startx``` if you are on a local machine, in a console and have a GUI installed.

#### Kali in WSL2 with GUI

Set WSL version 2

```powershell
(New-Object System.Net.WebClient).DownloadFile("https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi", "wsl_update_x64.msi") 
Start-Process msiexec.exe -Wait -ArgumentList '/I wsl_update_x64.msi /quiet' 
wsl --set-version kali-linux 2
```

Update Kali and install kex

```bash
sudo apt update && sudo apt install -y kali-linux-large
sudo apt install -y kali-win-kex
kex start
kex --esm --sound
```

Add option in windows terminal

Basic Win-KeX in seamless mode with sound:

```json
{
      "guid": "{55ca431a-3a87-5fb3-83cd-11ececc031d2}",
      "hidden": false,
      "name": "Win-KeX",
      "commandline": "wsl -d kali-linux kex --esm --sound"
}
```

#### Enable RDP for Azure

Make sure ssh (22) and rdp (3389) ports are open.

Depending on your setup you can open a port in Azure CLI as follows:

```shell
az vm open-port --resource-group myResourceGroup --name myVM --port 3389
```

Connect via SSH to Kali and run the following commands:

```shell
sudo apt update
sudo apt-get -y install xfce4
sudo apt-get -y install xrdp
sudo systemctl enable xrdp
echo xfce4-session >~/.xsession
sudo service xrdp restart
```

Some notes: (ignore this)

```shell
service xrdp-sesman start
update-rc.d xrdp enable
apt-get remove gnome-core
apt-get install lxde-core lxde kali-defaults kali-root-login desktop-base
```
