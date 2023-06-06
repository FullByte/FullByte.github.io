# Ubuntu

Ubuntu is an ancient african word, meaning "I can't configure Debian".[^1]

The following is tested and used on Ubunutu 22.04.

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

Some services like Disneyplus do not support linux. Change the useragent string and make sure to be in "desktop mode" when browsing sites like this. A valid useragent is e.g.:

`Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/106.0`

### Regolith

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
