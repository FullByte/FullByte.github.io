# Factorio Headless Server on Proxmox (LXC)

*Guest contribution by [HiSch](https://github.com/HiSch)*

This guide will walk you through creating a Proxmox LXC container and setting up a **Factorio headless server** inside it.


***

## 1. Create a New Proxmox LXC Container

1. **Download a CT template**
    - In Proxmox, select your **host** → go to **local (hostname)** → click **CT Templates**.
    - Click **Templates** and download one.
    - For this guide, we’ll use:
**`debian-12`**
2. **Create a new container**
    - Right-click your Proxmox host → **Create CT**.
    - **Hostname**: choose a name (e.g. `factorio`).
    - **Password**: set root password. → **Next**
3. **Storage \& Template**
    - Pick your storage.
    - Select the `debian-12` CT template. → **Next**
4. **Disk Size**
    - Recommended: `20 GB`.
5. **CPU**
    - 2 Cores should be fine (unless you expect very heavy loads).
6. **Memory**
    - `4096 MB RAM` + `4096 MB Swap` is a good start.
    - You can always change later in Proxmox.
7. **Network**
    - Enable DHCP (default works for most setups).
    - Advanced users can configure a custom network.
8. **DNS Settings**
    - Default is fine.
9. **Finish**
    - Click **Finish** → wait for container creation.

***

## 2. Initial Container Setup

1. Click your new **LXC container** → **Console/Shell**.
2. Log in as `root` (default).
3. Update and install required dependencies:

```bash
apt update
apt install wget tar rsync -y
```

4. Create a new user for Factorio:

```bash
adduser factorio
```

Set a password when prompted.

***

## 3. Install Factorio Headless

1. Log in as the new user:

```bash
su - factorio
```

2. Download Factorio server files:

```bash
wget https://factorio.com/get-download/stable/headless/linux64 -O ~/factorio_headless.tar.xz
```

3. Extract and prepare files:

```bash
tar -xvf ~/factorio_headless.tar.xz -C ~/
rsync -au ~/factorio/ ~/server/
rm ~/factorio_headless.tar.xz
rm -R ~/factorio/
```

4. Setup server config:

```bash
cp ~/server/data/server-settings.example.json ~/server/data/server-settings.json
nano ~/server/data/server-settings.json
```

(Edit settings as needed: server name, visibility, etc.)
5. Create your first map save:

```bash
~/server/bin/x64/factorio --create ~/server/my-save.zip
```

6. Logout back to `root`:

```bash
exit
```


***

## 4. Setup Systemd Service

As **root**, create a new `systemd` service:

```bash
sudo tee /etc/systemd/system/factorio.service > /dev/null << 'EOL'
[Unit]
Description=Factorio Headless Server
After=network.target

[Service]
Type=simple
User=factorio
WorkingDirectory=/home/factorio/server
ExecStart=/home/factorio/server/bin/x64/factorio --start-server /home/factorio/server/my-save.zip --server-settings /home/factorio/server/data/server-settings.json
Restart=always

[Install]
WantedBy=multi-user.target
EOL
```

Reload `systemd`:

```bash
systemctl daemon-reload
systemctl start factorio
systemctl enable factorio
```


***

## 5. Done

Your Factorio headless server should now be running automatically on boot.

- To check status:

```bash
systemctl status factorio
```

- To stop/start:

```bash
systemctl stop factorio
systemctl start factorio
```


***

You now have a dedicated **Factorio server** running inside a Proxmox LXC container!

# Port Forwarding for Factorio Server

By default, Factorio uses port **34197/UDP**.
If you want people outside your LAN to join your server, you need to make this port reachable from the internet.

## Port Forward on Your Router

On your home router/firewall:

1. Log in to your router admin panel.
2. Look for **Port Forwarding / NAT / Virtual Server** settings.
3. Add a new rule:
    - **Port**: `34197`
    - **Protocol**: `UDP`
    - **Destination IP**: IP address of your Factorio container (e.g., `192.168.1.50`).
    - **Forward To Port**: `34197`

Save and restart your router if necessary.

***

## Test External Connectivity

1. From outside your network (ask a friend, or use mobile hotspot):
    - Open Factorio → Multiplayer → Connect to your **public IP**.
    - Public IP can be found by searching *“what is my IP”* on Google.
2. Make sure your local firewall (Proxmox host or container) is not blocking UDP traffic on port `34197`.

***

## Optional: Register with the Official Server List

Inside your `~/server/data/server-settings.json`, you can configure:

- `"name": "My Awesome Factorio Server"`
- `"description": "Hosted on Proxmox LXC"`
- `"visibility": "public"`

This will let your server appear in the official Factorio multiplayer browser.
(Requires that port forwarding is working correctly.)

***

After completing this, you should be able to join by entering your **public IP (and port 34197)** in Factorio multiplayer.


# Updating Factorio Server Automatically

Factorio releases updates often, so it’s a good idea to automate the update process. Below are steps to create a simple script that updates your server daily at 4 AM.

***

## Create the Update Script

Log in as **root** in your Proxmox LXC container and create the script:

```bash
nano /root/update.sh
```

Paste the following contents:

```bash
#!/bin/bash

# Stop Factorio server before updating
service factorio stop

# Download latest Factorio headless version
sudo -u factorio wget https://factorio.com/get-download/stable/headless/linux64 -O /home/factorio/factorio_headless.tar.xz

# Extract files to the factorio home directory
sudo -u factorio tar -xvf /home/factorio/factorio_headless.tar.xz -C /home/factorio/

# Sync new files into server directory (preserves saves & configs)
sudo -u factorio rsync -au /home/factorio/factorio/ /home/factorio/server/

# Start the server again
service factorio start

# Cleanup temporary files
rm /home/factorio/factorio_headless.tar.xz
rm -R /home/factorio/factorio/
```

Save and exit (`CTRL+O`, then `CTRL+X`).

***

## Make the Script Executable

```bash
chmod +x /root/update.sh
```


***

## Schedule Daily Automatic Updates

Edit root’s **crontab**:

```bash
crontab -e
```

Add this line at the bottom to run the update daily at 4:00 AM:

```cron
0 4 * * * /root/update.sh > /dev/null 2>&1
```

- `0 4 * * *` → every day at **4:00 AM**
- `> /dev/null 2>&1` → silences script output

Save and exit the crontab editor.

***

## Verify Cron Setup

You can list cron jobs with:

```bash
crontab -l
```
