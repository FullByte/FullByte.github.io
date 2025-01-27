# Ubuntu

Ubuntu is an ancient african word, meaning "I can't configure Debian".[^1]

The following is tested and used on Ubuntu 22.04.

| Ubuntu Version | Code Name        | Debian Version | Code Name |
|----------------|------------------|----------------|-----------|
| 24.04 LTS      | Noble Numbat     | Debian 13      | Trixie    |
| 22.04 LTS      | Jammy Jellyfish  | Debian 11      | Bullseye  |
| 20.04 LTS      | Focal Fossa      | Debian 10      | Buster    |
| 18.04 LTS      | Bionic Beaver    | Debian 9       | Stretch   |
| 16.04 LTS      | Xenial Xerus     | Debian 8       | Jessie    |
| 14.04 LTS      | Trusty Tahr      | Debian 7       | Wheezy    |
| 12.04 LTS      | Precise Pangolin | Debian 6       | Squeeze   |

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

## Mount WebDAV share

I am using an filerun server on which I enabled ount WebDAV share.

Install `davfs2` and mount the drive e.g. to `/mnt/dav/`

``` sh
sudo apt-get install davfs2
sudo mount -t davfs -o noexec https://filerun.0xfab1.net/remote.php/webdav/ /mnt/dav/
```

Use `umount` to unmount the WebDAV share:

``` sh
sudo umount /mnt/dav
```

Alternativly use fstab to make this process more convenient:

Run this command and make sure to allow unprivileged users to mount WebDAV resources:

``` sh
sudo dpkg-reconfigure davfs2
```

Addtionally, make sure your user is member of the davfs2 group

``` sh
sudo usermod -a -G davfs2 fab1
```

Edit `/etc/fstab` and add a line, for example for `filerun.0xfab1.net`:

``` sh
https://filerun.0xfab1.net/remote.php/webdav/ /mnt/dav davfs _netdev,noauto,user,uid=fab1,gid=fab1 0 0
```

Edit `/etc/davfs2/secrets` and add username and password:

``` sh
/mnt/dav fab1 password
```

Run this command to mount the WebDAV share to `/mnt/dav`

``` sh
sudo mount /mnt/dav
```

## Create the boot script

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

## Install stuff

Download latest deb release and install it

``` sh
sudo apt-get install ./name.deb
```

[^1]: <https://www.urbandictionary.com/define.php?term=ubuntu>

## Firefox

Some services like Disney+ do not support linux. Change the useragent string and make sure to be in "desktop mode" when browsing sites like this. A valid useragent is e.g.:

`Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/106.0`

## Regolith

[Regolith](https://regolith-desktop.com/) runs i3: a popular, fast, and configurable tiling window manager which is great for fast keyboard-driven workflows. Regolith integrates i3 with other desktop components such as i3bar, rofication, gnome-flashback, and ilia to provide a complete desktop interface.

``` sh
wget -qO - https://regolith-desktop.org/regolith.key | \
gpg --dearmor | sudo tee /usr/share/keyrings/regolith-archive-keyring.gpg > /dev/null
echo deb "[arch=amd64 signed-by=/usr/share/keyrings/regolith-archive-keyring.gpg] \
https://regolith-desktop.org/release-ubuntu-jammy-amd64 jammy main" | \
sudo tee /etc/apt/sources.list.d/regolith.list
sudo apt update
sudo apt install regolith-desktop
sudo apt upgrade
sudo shutdown -r now
```

## Errors when updating

Restore the default repositories

Create a directory where we can run our commands:

``` sh
sudo mkdir ~/answer
```

Download the sources.list for Ubuntu 20.04 focal.

``` sh
cd ~/answer/
```

Create a `sources.list` with this content:

```txt
deb http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-updates main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-security main restricted universe multiverse

deb http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu/ focal-backports main restricted universe multiverse

deb http://archive.canonical.com/ubuntu focal partner
deb-src http://archive.canonical.com/ubuntu focal partner
```

Optionally, change the sources.list to match your version:

``` sh
sudo sed -i "s/focal/$(lsb_release -c -s)/" ~/answer/sources.list
```

Backup your current sources.list and replace the sources.list:

``` sh
sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak
sudo mv ~/answer/sources.list /etc/apt/
```

Run apt update:

``` sh
sudo apt update
```

By default, the directory which contains all the PPA files is empty. If after restoring the repositories, you're still facing errors then you need to remove all the PPA files too.

Move the directory containing the PPA files to the ~/answer directory:

``` sh
sudo mv /etc/apt/sources.list.d/ ~/answer 
```

Recreate the directory:

``` sh
sudo mkdir /etc/apt/sources.list.d
```

Run apt update:

``` sh
sudo apt update 
```

Remove the ~/answer directory:

``` sh
sudo rm -r ~/answer
```
