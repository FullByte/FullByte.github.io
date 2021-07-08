# Kali

Install and config Kali

## Update

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

### Get a GUI

Run ```startx``` if you are on a local machine, in a console and have a GUI installed.

### Kali in WSL2 with GUI

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

### Enable RDP for Azure

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

## Config

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

## Tools

Tools ready to be installed

- Eyewitness (screenshot pws): ```sudo apt install eyewitness```
- FreeIPMI: ```sudo apt install freeipmi-tools```
- hcxtools to convert packets: ```sudo apt install hcxdumptool hcxtools```
- advancement of the original mingw: ```sudo apt install gcc-mingw-w64```
- ncat (nc alt) ```sudo apt install ncat```
- network time synchronisation status: ```sudo apt install ntpstat```
- python3 tools: ```sudo apt install python3-dnspython python3-netaddr python3-virtualenv python3-pyftpdlib python3-jwt python3-git```
- seclists ```sudo apt -y install seclists```

Further Tools

### Dnscan

wordlist-based DNS subdomain scanner

```shell
sudo apt install python3-dnspython 
sudo git clone https://github.com/rbsec/dnscan /opt/dnscan
sudo pip install -r /opt/dnscan/requirements.txt
sudo ln -s /opt/dnscan/dnscan.py /usr/local/bin/dnscan.py
```

Run example:

```shell
./dnscan.py -d dev-%%.example.org
```

### Reposcanner

```shell
sudo apt install python3-git
sudo git clone https://github.com/dionach/reposcanner /opt/reposcanner
ln -s /opt/reposcanner/reposcanner.py /usr/local/bin/reposcanner.py
```

Run example:

```shell
reposcanner.py -r https://github.com/FullByte/FullByte.github.io
```

### pwdumpstats

generate statistics from a pwdump file

```shell
sudo git clone https://github.com/Dionach/pwdumpstats /opt/pwdumpstats
sudo ln -s /opt/pwdumpstats/pwdumpstats.py /usr/local/bin/pwdumpstats.py
```

Run example:

```shell
pwdumpstats.py /usr/share/wordlists/rockyou.txt
```

### CODA Pentest Scripts

```shell
git clone https://github.com/codagroup/pentestscripts /opt/pentestscripts
ln -s /opt/pentestscripts/sourcescan.py /usr/local/bin/sourcescan.py
```

### Frogger

```shell
git clone https://github.com/commonexploits/vlan-hopping /opt/frogger
ln -s /opt/frogger/froggers.sh /usr/local/bin/froggers.sh
chmod +x /opt/frogger/froggers.sh
```

### ScoutSuite

```shell
git clone https://github.com/nccgroup/ScoutSuite /opt/scoutsuite
cd /opt/scoutsuite
virtualenv -p python3 venv
. venv/bin/activate
pip3 install -r requirements.txt
pip3 install azure-cli
cat <<EOT > /usr/local/bin/scout.sh
#!/bin/sh
. /opt/scoutsuite/venv/bin/activate > /dev/null 2>&1 && /opt/scoutsuite/scout.py $@
EOT
chmod +x /usr/local/bin/scout.sh
exit
```

### jwt2john

```shell
wget --quiet -O /usr/local/bin/jwt2john.py "https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py"
sed -i '1s;^;#!/usr/bin/env python\n;' /usr/local/bin/jwt2john.py
chmod +x /usr/local/bin/jwt2john.py
```

### Prowler

```shell
pip3 install ansi2html detect-secrets
git clone https://github.com/toniblyx/prowler /opt/prowler
```
