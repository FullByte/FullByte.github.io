# Jitsi Meet

| What          | Where                                 |
|---------------|---------------------------------------|
| Official Page | <https://meet.jit.si/>                |
| Source        | <https://github.com/jitsi/jitsi-meet> |
| Documentation | <https://jitsi.github.io/handbook/>   |

## Setup Server

- Setup `Ubunutu 20.04 LTS` VM
- Attach a public IP e.g. `10.11.12.13`
- add a DNS entry e.g. `jitsi.example.com`
- Add `10.11.12.13 jitsi.example.com` to `/etc/host`
- Update the server: ```sudo apt-get update && sudo apt-get upgrade```

Add apt-transport-https and enable the universe repository

``` sh
apt install apt-transport-https
sudo apt-add-repository universe
sudo apt update
```

Add Jitsi as repository

``` sh
curl https://download.jitsi.org/jitsi-key.gpg.key | sudo sh -c 'gpg --dearmor > /usr/share/keyrings/jitsi-keyring.gpg'
echo 'deb [signed-by=/usr/share/keyrings/jitsi-keyring.gpg] https://download.jitsi.org stable/' | sudo tee /etc/apt/sources.list.d/jitsi-stable.list > /dev/null
sudo apt update
```

Update the firewall (also check host/provider for network settings)

``` sh
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw allow 10000/udp
sudo ufw allow 22/tcp
sudo ufw allow 3478/udp
sudo ufw allow 5349/tcp
sudo ufw enable
sudo ufw status numbered
```

## Install jitsi

Install Jitsi and enter the FQDN for jitsi (e.g. jitsi.example.com) and add select an option for the certificate

``` sh
sudo apt install jitsi-meet -y
```

If you selected to create a self-signed cert run this:

``` sh
sudo /usr/share/jitsi-meet/scripts/install-letsencrypt-cert.sh
```

You should now be able to open `jitsi.example.com` in your browser and start a meeting.

## Config Jitsi

To allow only valid users to create new meetings config jitsi as follows:

Edit as root `nano /etc/prosody/conf.avail/[your-hostname].cfg.lua` and:

- Change `authentication = "anonymous"` to `authentication = "internal_hashed"`
- Add an addtional VirtualHost entry with guest. + current jitsi FQDN e.g.:

    ``` lua
    VirtualHost "guest.jitsi.example.com"
        authentication = "anonymous"
        c2s_require_encryption = false
    ```

The domain of the guest VirtualHost is internal only. There is no need to update your DNS for `guest.jitsi.example.com`.

Update the [Jitsi Conference Focus](https://github.com/jitsi/jicofo) by editing this file as root `nano /etc/jitsi/meet/[your-hostname]-config.js` and adding `anonymousdomain: 'guest.jitsi.example.com'`

Now add a user and password with ```sudo prosodyctl register [username] jitsi.example.com [password]```

Restart all services and only allowed users are able to create meetings.

``` sh
service prosody restart
service jicofo restart
service jitsi-videobridge2 restart
service nginx restart
```
