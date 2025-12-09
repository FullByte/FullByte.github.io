# Syncthing

| What          | Where                                            |
|---------------|--------------------------------------------------|
| Official Page | [Syncthing](https://syncthing.net/)              |
| Source        | [Source](https://github.com/syncthing/syncthing) |
| Download      | [Download](https://syncthing.net/downloads/)     |

## Install Syncthing

A script to install syncthing on debian

``` sh
#!/bin/bash
set -e

# === VARIABLEN ===
S_USER="syncthinguser"     ## <-- Name des neuen Users für Syncthing
HOME_S="/home/${S_USER}"

# 1) System aktualisieren + notwendige Pakete
apt update
apt upgrade -y
apt install -y gnupg2 curl apt-transport-https ca-certificates

# 2) GPG-Key und Syncthing-Repo hinzufügen
curl -fsSL https://syncthing.net/release-key.gpg \
    | gpg --dearmor -o /usr/share/keyrings/syncthing-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/syncthing-archive-keyring.gpg] https://apt.syncthing.net/ syncthing stable-v2" \
    > /etc/apt/sources.list.d/syncthing.list

# 3) Paket-Liste aktualisieren und Syncthing installieren
apt update
apt install -y syncthing

# 4) System-User anlegen (ohne Login-Shell)
useradd --system --create-home --home-dir "${HOME_S}" --shell /usr/sbin/nologin --user-group "${S_USER}"

# 5) Optional: Home-Verzeichnis sichern / Rechte setzen
mkdir -p "${HOME_S}"
chown -R "${S_USER}:${S_USER}" "${HOME_S}"

# 6) Syncthing systemd-Service aktivieren für neuen User
systemctl enable "syncthing@${S_USER}.service"

# 7) Syncthing starten
systemctl start "syncthing@${S_USER}.service"

echo "=== Erfolg ==="
echo "Syncthing läuft jetzt als Benutzer '${S_USER}'."
echo "Öffne im Browser: http://<server-ip>:8384"
echo "Wenn du externen Zugriff willst, evtl. Firewall anpassen."
```

Config Network

```sh
chsh -s /bin/bash syncthing
su - syncthing
syncthing cli config gui raw-address set 0.0.0.0:8384
syncthing cli config gui raw-use-tls set true
systemctl restart syncthing@syncthing.service
```

Test by accessing Synthing on Port 8384

## Setup nginx

```sh
sudo apt update && sudo apt upgrade -y
sudo apt install nginx -y
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
sudo apt install certbot python3-certbot-nginx -y
```

Create the nginc config: `sudo nano /etc/nginx/sites-available/syncthing`

```nginx
server {
    listen 80;
    server_name share.yolo.omg.lol;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name share.yolo.omg.lol;

    ssl_certificate /etc/letsencrypt/live/share.yolo.omg.lol/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/share.yolo.omg.lol/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8384;
        proxy_set_header Host            $host;
        proxy_set_header X-Real-IP       $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Start nginx

```sh
sudo ln -s /etc/nginx/sites-available/syncthing /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

Config Let’s Encrypt

sudo certbot --nginx -d the.domain.lol

Test certbot

```sh
sudo certbot renew --dry-run --nginx
```

Update certbot certs

```sh
sudo systemctl enable --now certbot.timer
sudo systemctl status certbot.timer
```

Test by accessing Synthing on URL provided (the.domain.lol). Use HTTPS and dont't add the port 8384 (should redirect).
If you get an error (e.g. redirect error) turn off "use HTTPS" in Synthing WebGUI settings.
