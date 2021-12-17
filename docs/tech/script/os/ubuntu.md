# Ubuntu

## Config System

Update and clean up:

 ```sh
sudo apt update && sudo apt -y upgrade && sudo apt -y autoremove && sudo apt -y autoclean
```

### Add/Remove User

 ```sh
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

 ```sh
dpkg-reconfigure keyboard-configuration
service keyboard-setup restart
```

### New password

 ```sh
passwd
```

### Configure WiFi

 ```sh
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
    ssid="WiFi"
    psk="WiFiPassword"
}
sudo wpa_cli reconfigure
```

eventually reboot and/or try this:

 ```sh
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
sudo ifconfig wlan0 | grep inet
sudo service networking restart
```

Test Config:

 ```sh
wpa_supplicant -i wlan0 -D wext -c /etc/wpa_supplicant/wpa_supplicant.conf -d
```

### Create the boot script

Example script that install updates to ubuntu automatically

The script "bootupdate.sh":

 ```sh
#!/bin/bash
sudo apt update && apt -y full-upgrade && apt -y autoremove
exit 0
```

Move "bootupdate.sh" to init.d

 ```sh
mv bootupdate.sh /etc/init.d/bootupdate.sh
```

Add script to boot sequente

 ```sh
update-rc.d bootupdate.sh start 2
```

### Make Ubuntu Desktop nice

 ```sh
# Get Video Codecs
sudo apt install ubuntu-restricted-extras ubuntu-restricted-addons

# Get Compiz and Docky
sudo apt install gnome-session-flashback compiz compiz-core compiz-plugins compiz-plugins-default compiz-plugins-extra compiz-plugins-main compiz-plugins-main-default compiz-plugins-main-dev compizconfig-settings-manager docky

#Gnome Tweak
sudo apt install gnome-tweaks gnome-tweak-tool
```

## Install Tools

### xrdp

 ```sh
sudo apt update
sudo apt install tasksel
sudo apt install xrdp # start RDP
sudo systemctl status xrdp #verify
```

### TeamViewer

 ```sh
wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb
sudo apt install ./teamviewer_amd64.deb
teamviewer
teamviewer --passwd password
teamviewer daemon restart
teamviewer -info
teamviewer license accept
```

### Node.js

 ```sh
sudo apt update
sudo apt -y install curl dirmngr apt-transport-https lsb-release ca-certificates
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt -y install nodejs
sudo apt -y  install gcc g++ make
node --version
npm --version
```

### Install Wine

 ```sh
sudo dpkg --add-architecture i386
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
deb https://dl.winehq.org/wine-builds/debian/ buster main
sudo apt update
sudo apt install --install-recommends winehq-stable
```

### Linux File System Permissions

- Change owner of file or dir: ```chown user:group blah```
- Change owner of file or dir recersive for all folders below: ```chown -R user:group blah```
- Change file / dir permissions: ```chmod 600 file```

|VALUE|RWX|MEANING|
|---|--|--|
|777|rwxrwxrwx| No restriction, global WRX any user can do anything.|
|755|rwxr-xr-x| Owner has full access, others can read and execute the file.|
|700|rwx------| Owner has full access, no one else has access.|
|666|rw-rw-rw-| All users can read and write but not execute.|
|644|rw-r--r--| Owner can read and write, everyone else can read.|
|600|rw-------| Owner can read and write, everyone else has no access.|

### Linux File System

- **/bin** Common programs, shared by the system, the system administrator and the users.
- **/boot** Boot files, boot loader (grub), kernels, vmlinuz
- **/dev** Contains references to system devices, files with special properties.
- **/etc** Important system config files.
- **/home** Home directories for system users.
- **/lib** Library files, includes files for all kinds of programs needed by the system and the users.
- **/lost+found** Files that were saved during failures are here.
- **/mnt** Standard mount point for external file systems.
- **/media** Mount point for external file systems (on some distros).
- **/net** Standard mount point for entire remote file systems – nfs.
- **/opt** Typically contains extra and third party software.
- **/proc** A virtual file system containing information about system resources.
- **/root** root users home dir.
- **/sbin** Programs for use by the system and the system administrator.
- **/tmp** Temporary space for use by the system, cleaned upon reboot.
- **/usr** Programs, libraries, documentation etc. for all user-related programs.
- **/var** Storage for all variable files and temporary files created by users, such as log files, mail queue, print spooler. Web servers, Databases etc.

### Linux interesting files and directories

Places that are worth a look if you are attempting to privilege escalate / perform post exploitation.

- **/etc/passwd** Contains local Linux users.
- **/etc/shadow** Contains local account password hashes.
- **/etc/group** Contains local account groups.
- **/etc/init.d/** Contains service init script – worth a look to see whats installed.
- **/etc/hostname** System hostname.
- **/etc/network/interfaces** Network interfaces.
- **/etc/resolv.conf** System DNS servers.
- **/etc/profile** System environment variables.
- **~/.ssh/** SSH keys.
- **~/.bash_history** Users bash history log.
- **/var/log/** Linux system log files are typically stored here.
- **/var/adm/** UNIX system log files are typically stored here.
- **/var/log/httpd/access.log** Apache access log file typical path.
- **/etc/fstab** File system mounts.

## Cron Jobs

### Examples

 ```sh
Every Minute    * * * * *
Every Five Minutes    */5 * * * *
Every 10 Minutes    */10 * * * *
Every 15 Minutes    */15 * * * *
Every 30 Minutes    */30 * * * *
Every Hour    0 * * * *
Every Two Hours    0 */2 * * *
Every Six Hours    0 */6 * * *
Every 12 Hours    0 */12 * * *
During the Work Day    */5 9-17 * * *
Every day at Midnight    0 0 * * *
Every Two Weeks    0 0 * * Sun [ $(expr $(date +%W) % 2) -eq 1 ] && /path/to/command
At the Start of Every Month    0 0 1 * *
On January 1st at Midnight    0 0 1 1 *
```
