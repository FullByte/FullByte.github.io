# Debian

## Default Source List

Update source list:

``` sh
sudo nano /etc/apt/sources.list
```

Replace source list with this:

```txt
# Debian 13 "Trixie" - main repository
deb http://deb.debian.org/debian trixie main contrib non-free-firmware non-free
deb-src http://deb.debian.org/debian trixie main contrib non-free-firmware non-free

# Security updates
deb http://security.debian.org/debian-security trixie-security main contrib non-free-firmware non-free
deb-src http://security.debian.org/debian-security trixie-security main contrib non-free-firmware non-free

# Updates (bugfixes etc.)
deb http://deb.debian.org/debian trixie-updates main contrib non-free-firmware non-free
deb-src http://deb.debian.org/debian trixie-updates main contrib non-free-firmware non-free
```

Run full update:

``` sh
sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove --purge -y && sudo apt autoclean -y
```
