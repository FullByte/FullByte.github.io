# Information Gathering

TODO: WhatWeb

## Network

### Nmap

Scan a network. ([MAN pages](https://nmap.org/book/man.html) and [scripts](https://nmap.org/nsedoc))

Press "v" if you forgot du add "-v" in the scan and need to increase verbosity.

- Simple IP scan: ```nmap -sC -sV $ip```
- Enumerate the SMB shares: ```nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse $ip```

[ncat](https://nmap.org/ncat/): todo

### Dnscan

wordlist-based DNS subdomain scanner

``` sh
sudo apt install python3-dnspython 
sudo git clone https://github.com/rbsec/dnscan /opt/dnscan
sudo pip install -r /opt/dnscan/requirements.txt
sudo ln -s /opt/dnscan/dnscan.py /usr/local/bin/dnscan.py
```

Run example:

``` sh
./dnscan.py -d dev-%%.example.org
```

## Website

### Dirbuster

TODO

### GoBuster

Find dirs that work

- Source: <https://github.com/OJ/gobuster>
- Install: ```sudo apt-get install gobuster```

Example:

``` sh
gobuster dir -w /usr/share/dirbuster/wordlists/directory-list-2.3-medium.txt -u 10.10.112.131
gobuster dir -w /usr/share/SecLists/Discovery/Web-Content/big.txt -u 10.10.225.77
gobuster dir -w /usr/share/wordlists/dirb/common.txt -u 10.10.225.77
```

## Dirbuster

[dirbuster](https://gitlab.com/kalilinux/packages/dirbuster)

When running dirbuster command, you can provide the "-r" option to tell dirbuster to not be recursive, resulting in a faster search.

## Database

## SQLMap

SQLMap

## Social

### Reposcanner

``` sh
sudo apt install python3-git
sudo git clone https://github.com/dionach/reposcanner /opt/reposcanner
ln -s /opt/reposcanner/reposcanner.py /usr/local/bin/reposcanner.py
```

Run example:

``` sh
reposcanner.py -r https://github.com/FullByte/FullByte.github.io
```

### Photon (web crawler)

<https://github.com/s0md3v/Photon>

TODO

## Cloud

### ScoutSuite (AWS, Azure, GCP)

``` sh
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

### Prowler (AWS)

``` sh
pip3 install ansi2html detect-secrets
git clone https://github.com/toniblyx/prowler /opt/prowler
```
