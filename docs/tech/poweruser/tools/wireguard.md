# Wireguard

Helpful script: <https://raw.githubusercontent.com/angristan/wireguard-install/master/wireguard-install.sh>

## Debian: Install and Configure

Install Wireguard

``` sh
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install –y wireguard
```

Create SSH key-value pair

``` sh
mkdir ~/.wireguard
cd ~/.wireguard
umask 077
wg genkey | tee privatekey | wg pubkey > publickey
cat privatekey
```

Create Wireguard config file

``` sh
sudo nano /etc/wireguard/wg0.conf
```

Add the following content:

``` sh
[Interface]
Address = SERVER-IP
SaveConfig = true
ListenPort = 51820
PrivateKey = KeyWeCreatedAbove

[Peer]
PublicKey = PublicKeyFromClient
AllowedIPs = CLIENT-IP or 0.0.0.0/0
```

Set the VPN server to launch at startup:

``` sh
sudo systemctl enable wg-quick@wg0
```

Start the WireGuard service:

``` sh
sudo wg-quick up wg0
```

start wireguard as service

``` sh
sudo cp wg0.conf /etc/wireguard
sudo systemctl enable systemd-resolved.service
sudo systemctl start systemd-resolved.service
sudo ln -s /usr/bin/resolvectl /usr/local/bin/resolvconf
```

turns on VPN

``` sh
sudo wg-quick up US_NE_WG
```

show status

``` sh
sudo wg show
```

turns off VPN

``` sh
sudo wg-quick down US_NE_WG
```
