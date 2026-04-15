# Fail2ban

[Fail2ban](https://github.com/fail2ban/fail2ban) is a Daemon to ban hosts that cause multiple authentication errors.

Run this script to install fail2ban:

``` sh
chmod +x setup_fail2ban.sh
./setup_fail2ban.sh
```

`setup_fail2ban.sh` script:

``` sh
#!/bin/bash

set -e

echo "[1/5] Installiere Fail2Ban..."
sudo apt update
sudo apt install -y fail2ban python3-systemd

echo "[2/5] Erstelle /etc/fail2ban/jail.local..."

sudo tee /etc/fail2ban/jail.local > /dev/null << 'EOF'
[DEFAULT]
banaction = iptables-multiport

[sshd]
enabled = true
backend = systemd
maxretry = 3
findtime = 10m
bantime = 1h

[recidive]
enabled = true
logpath = /var/log/fail2ban.log
bantime = 7d
findtime = 1d
maxretry = 5
EOF

echo "[3/5] Starte Fail2Ban neu..."
sudo systemctl enable fail2ban
sudo systemctl restart fail2ban

echo "[4/5] Prüfe Status..."
sudo fail2ban-client status

echo "[5/5] Prüfe sshd Jail..."
sudo fail2ban-client status sshd

echo "Fertig."
```
