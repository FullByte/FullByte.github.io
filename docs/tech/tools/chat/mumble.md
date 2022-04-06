# Mumble

| What          | Where                                                  |
|---------------|--------------------------------------------------------|
| Official Page | <https://www.mumble.info/>                             |
| Source        | <https://github.com/mumble-voip/mumble>                |
| Documentation | <https://www.mumble.info/documentation/mumble-server/> |

## Install on Debian/Ubuntu

``` sh
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mumble-server
sudo apt-get install mumble
sudo dpkg-reconfigure mumble-server
sudo nano /etc/mumble-server.ini
sudo service mumble-server restart
```

Things to change in the `mumble-server.ini`

TODO

Update the firewall (also check host/provider for network settings). If you changed the default port in `mumble-server.ini` change it here as well:

``` sh
sudo ufw allow 64738/tcp
sudo ufw allow 64738/udp
sudo ufw enable
sudo ufw status numbered
```
