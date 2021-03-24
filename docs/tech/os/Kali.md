# Kali

## Update & Config

Update

```shell
sudo wget -q -O - https://archive.kali.org/archive-key.asc | apt-key add # Get latest key
sudo dpkg --configure -a
sudo apt update && apt -y full-upgrade && apt -y autoremove && apt -y autoclean
```

Config

```shell
apt install awscli eyewitness freeipmi-tools hcxdumptool hcxtools gcc-mingw-w64 ncat ntpstat python3-dnspython python3-netaddr python3-virtualenv python3-pyftpdlib python3-jwt
apt purge -y network-manager
```

Disable network manager

If you prefer having hardcoded configuration and/or network manager is causing issues you can purge it:

```shell
sudo systemctl stop NetworkManager.service
sudo systemctl disable NetworkManager.service

sudo systemctl stop NetworkManager-wait-online.service
sudo systemctl disable NetworkManager-wait-online.service

sudo systemctl stop NetworkManager-dispatcher.service
sudo systemctl disable NetworkManager-dispatcher.service

sudo systemctl stop network-manager.service
sudo systemctl disable network-manager.service
```

## Further Tools

seclists

```shell
apt -y install seclists
```

Dnscan

```shell
git clone https://github.com/rbsec/dnscan /opt/dnscan
ln -s /opt/dnscan/dnscan.py /usr/local/bin/dnscan.py

Reposcanner

```shell
git clone https://github.com/dionach/reposcanner /opt/reposcanner
ln -s /opt/reposcanner/reposcanner.py /usr/local/bin/reposcanner.py
```

pwdumpstats

```shell
git clone https://github.com/Dionach/pwdumpstats /opt/pwdumpstats
ln -s /opt/pwdumpstats/pwdumpstats.py /usr/local/bin/pwdumpstats.py
```

CODA Pentest Scripts

```shell
git clone https://github.com/codagroup/pentestscripts /opt/pentestscripts
ln -s /opt/pentestscripts/sourcescan.py /usr/local/bin/sourcescan.py
```

Frogger

```shell
git clone https://github.com/commonexploits/vlan-hopping /opt/frogger
ln -s /opt/frogger/froggers.sh /usr/local/bin/froggers.sh
chmod +x /opt/frogger/froggers.sh
```

ScoutSuite

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

jwt2john

```shell
wget --quiet -O /usr/local/bin/jwt2john.py "https://raw.githubusercontent.com/Sjord/jwtcrack/master/jwt2john.py"
sed -i '1s;^;#!/usr/bin/env python\n;' /usr/local/bin/jwt2john.py
chmod +x /usr/local/bin/jwt2john.py
```

Prowler

```shell
pip3 install ansi2html detect-secrets
git clone https://github.com/toniblyx/prowler /opt/prowler
```

## Commands

Search for network devices in Monitor Mode and Access Points

```shell
iwconfig 2>/dev/null | grep "Mode\\:Monitor" | awk '{print $1}'
iwconfig 2>&1 | sed -n -e 's/^.\*Access Point: //p'
```

## Kali in WSL2 with GUI

**Set WSL version 2**

```powershell
(New-Object System.Net.WebClient).DownloadFile("https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi", "wsl_update_x64.msi") 
Start-Process msiexec.exe -Wait -ArgumentList '/I wsl_update_x64.msi /quiet' 
wsl --set-version kali-linux 2
```

**Update Kali**

```bash
sudo apt update
sudo apt install -y kali-linux-large
sudo apt install -y kali-win-kex
kex start
kex --esm --sound
```

**Add option in windows terminal**

Basic Win-KeX in seamless mode with sound:
```json
{
      "guid": "{55ca431a-3a87-5fb3-83cd-11ececc031d2}",
      "hidden": false,
      "name": "Win-KeX",
      "commandline": "wsl -d kali-linux kex --esm --sound"
}
```
