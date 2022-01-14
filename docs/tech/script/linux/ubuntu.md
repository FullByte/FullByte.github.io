# Ubuntu

## Config System

Update and clean up:

``` sh
sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove && sudo apt -y autoclean
```

### Add/Remove User

``` sh
adduser <user> # Add user
gpasswd -a <user> <group> # Add user to group
groups <user> # Show groups the user is added to
gpasswd -d <user> <group> # Remove user from group

passwd -l <user> # Lock the  User account
killall -9 -u <user> # Kill all running processes of the User
crontab -r -u <user> # Delete the user's cron jobs
lprm <user> # Delete printer jobs run
userdel -r <user> # Delete/ remove user account and files
```

### Keyboard layout

``` sh
dpkg-reconfigure keyboard-configuration
service keyboard-setup restart
```

### New password

``` sh
passwd
```

### Configure WiFi

``` sh
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
    ssid="WiFi"
    psk="WiFiPassword"
}
sudo wpa_cli reconfigure
```

eventually reboot and/or try this:

``` sh
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
sudo ifconfig wlan0 | grep inet
sudo service networking restart
```

Test Config:

``` sh
wpa_supplicant -i wlan0 -D wext -c /etc/wpa_supplicant/wpa_supplicant.conf -d
```

### Create the boot script

Example script that install updates to ubuntu automatically

The script "bootupdate.sh":

``` sh
#!/bin/bash
sudo apt update && apt -y full-upgrade && apt -y autoremove
exit 0
```

Move "bootupdate.sh" to init.d

``` sh
mv bootupdate.sh /etc/init.d/bootupdate.sh
```

Add script to boot sequente

``` sh
update-rc.d bootupdate.sh start 2
```

### Make Ubuntu Desktop nice

``` sh
# Get Video Codecs
sudo apt install ubuntu-restricted-extras ubuntu-restricted-addons

# Get Compiz and Docky
sudo apt install gnome-session-flashback compiz compiz-core compiz-plugins compiz-plugins-default compiz-plugins-extra compiz-plugins-main compiz-plugins-main-default compiz-plugins-main-dev compizconfig-settings-manager docky

#Gnome Tweak
sudo apt install gnome-tweaks gnome-tweak-tool
```

## Install Tools

### xrdp

``` sh
sudo apt update
sudo apt install tasksel
sudo apt install xrdp # start RDP
sudo systemctl status xrdp #verify
```

### TeamViewer

``` sh
wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
sudo apt install ./teamviewer_amd64.deb
teamviewer
teamviewer --passwd password
teamviewer daemon restart
teamviewer -info
teamviewer license accept
```

### Node.js

``` sh
sudo apt update
sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt -y install nodejs
sudo apt -y  install gcc g++ make
node --version
npm --version
```

### Install Wine

``` sh
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
deb https://dl.winehq.org/wine-builds/debian/ buster main
sudo apt update
sudo apt install --install-recommends winehq-stable
```
