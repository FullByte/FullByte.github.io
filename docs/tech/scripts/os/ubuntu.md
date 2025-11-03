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

## New VPS

Some basics config for any new machine for a new virtual private server (e.g. from Azure, AWS, GCP, Hetzner, ...)

### Tools

This is an overview of all tools used:

| Category        | Tool                    | Type        | License / Source |
| --------------- | ----------------------- | ----------- | ---------------- |
| OS & Packages   | apt, systemctl          | Built-in    | Debian/Ubuntu    |
| Firewall        | UFW                     | Open-source | Canonical        |
| SSH             | OpenSSH                 | Open-source | BSD-style        |
| Web Server      | Nginx                   | Open-source | 2-clause BSD     |
| SSL             | Certbot / Let’s Encrypt | Open-source | EFF / ISRG       |
| Runtime         | Node.js / npm           | Open-source | MIT              |
| Process Manager | PM2                     | Open-source | AGPL             |
| Monitoring      | htop / iotop            | Open-source | GPL              |
| Backups         | tar / cron              | Built-in    | GNU              |
| Updates         | unattended-upgrades     | Open-source | Debian           |
| Auditing        | Lynis                   | Open-source | GPLv3            |

### Steps

Read this as a basic setup and security checklist (there is always more that can be done :D ):

Connect to your new server and apply updates:

``` sh
ssh root@vps-ip
apt update && apt upgrade -y
uname -a
cat /etc/os-release
```

Change the root password

``` sh
passwd
```

Create a secondary (unprivileged) user, give it sudo access:

``` sh
adduser myusername
usermod -aG sudo myusername
groups myusername       # myusername : myusername sudo
su - myusername
sudo whoami             # root
```

#### SSH

On your local machine generate SSH keys:

``` sh
ssh-keygen -t ed25519 -C "email@ddress.com"
cat ~/.ssh/id_ed25519.pub
```

On the server (as your new user, not root):

``` sh
mkdir -p ~/.ssh
chmod 700 ~/.ssh
nano ~/.ssh/authorized_keys   # paste your public key here
chmod 600 ~/.ssh/authorized_keys
```

Test login:

``` sh
ssh myusername@vps-ip
```

Edit SSH configuration: `sudo nano /etc/ssh/sshd_config` and add/edit these lines:

``` txt
PasswordAuthentication no
PubkeyAuthentication yes
```

Check if `/etc/ssh/sshd_config.d/50-cloud-init.conf` exists with `sudo nano /etc/ssh/sshd_config.d/50-cloud-init.conf` and add/edit this line:

``` txt
PasswordAuthentication no
```

Test and restart sshd:

``` sh
sudo sshd -t
sudo systemctl restart ssh
sudo systemctl status ssh
```

Disable root login by editing `sudo nano /etc/ssh/sshd_config` and add/edit this line:

``` txt
PermitRootLogin no
```

restart sshd:

``` sh
sudo systemctl restart ssh
```

Test ssh login from a different terminal (result should be "Permission denied"):

``` sh
ssh root@vps-ip
```

#### Firewall

Using UFW (Uncomplicated Firewall):

``` sh
sudo ufw status
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh # Allow SSH before enabling firewall
sudo ufw allow 80/tcp # Allow HTTP
sudo ufw allow 443/tcp # Allow HTTPS
```

Enable firewall and type 'y' when prompted:

``` sh
sudo ufw enable
sudo ufw status verbose
```

Change default SSH port:

``` sh
sudo nano /etc/ssh/sshd_config
```

``` sh
sudo ufw allow 666/tcp         # changed Port 22 to Port 666
sudo ufw delete allow 22/tcp
sudo systemctl restart ssh
```

#### Updates

Activating unattended upgrades to ensure the server stays up-to-date:

``` sh
sudo apt install unattended-upgrades apt-listchanges
```

Run this and select "yes"

``` sh
sudo dpkg-reconfigure unattended-upgrades
```

Edit this file `sudo nano /etc/apt/apt.conf.d/50unattended-upgrades` and uncomment line:

``` txt
"${distro_id}:${distro_codename}-security";
```

As well as consider a reboot window e.g.:

```txt
Unattended-Upgrade::Automatic-Reboot "true";
Unattended-Upgrade::Automatic-Reboot-Time "04:00";
```

Test the unattended upgrades:

``` sh
sudo unattended-upgrades --dry-run
sudo systemctl status unattended-upgrades
```

## Checks

- [ ] SSH key authentication works
- [ ] Password authentication is disabled
- [ ] Root login is blocked
- [ ] Firewall is active and configured
- [ ] Automatic updates working
- [ ] Application runs in production mode
- [ ] SSL certificate valid
- [ ] Backups are being created

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
