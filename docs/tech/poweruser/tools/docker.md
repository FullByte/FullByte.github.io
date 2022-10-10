# Docker

| What          | Where                                                                    |
|---------------|--------------------------------------------------------------------------|
| Official Page | <https://www.docker.com/>                                                |
| Docs          | <https://docs.docker.com/get-started/>                                   |
| Download      | <https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe> |
| Install       |```choco install docker-desktop```                                       |

Links:

- More: <https://github.com/hexops/dockerfile>
- Many Images: <https://hub.docker.com/u/linuxserver/>
- how-to-clean-text-data-at-the-command-line <https://www.ezzeddinabdullah.com/posts/how-to-clean-text-data-at-the-command-line>

## Basics

### Network issues on Windows

Network issues on Windows with Docker for Windows:

Show IP address allocated by the docker host: ```docker inspect -f "{{ .NetworkSettings.IPAddress }}" <docker-name>```

Required port is reserved

- Check, if your required port is reserved: ```netsh interface ipv4 show excludedportrange protocol=tcp```
- If it your port is in one of the ranges, stop winnat: ```net stop winnat```
- Do stuff that didn't work before
- Prohibit dynamic reservation for your required port (here for example, 50051, as stated in the original question): ```netsh int ipv4 add excludedportrange protocol=tcp startport=50051 numberofports=1```
Restart winnat: ```net start winnat```

Stop IIS:

- Stop IIS: ```iisreset /STOP```

## Activate Docker in WSL2

Make sure WSL is installed and ready:

``` ps1
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
wsl --install
wsl --set-default-version 2
wsl --install Ubuntu
wsl --set-version Ubuntu 2
```

### Install Docker & Docker-compose on Ubuntu

``` sh
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common libssl-dev libffi-dev git wget nano
sudo groupadd docker
sudo usermod -aG docker ${USER}
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update
sudo apt-get install -y docker-ce containerd.io docker-compose
sudo update-alternatives --config iptables # select iptables-legacy
```

Restart WSL to make sure changes apply.

Test if docker is running with ```sudo service docker status```; if not start docker with ```sudo service docker start```. Now run a hello-world container to see if docker is working: ```sudo docker run hello-world```.

### Settings

Run docker on startup

``` sh
wsl.exe -u root service docker status || wsl.exe -u root service docker start
```

To limit the resources of your WSL:

- Enter the user's folder. C:\Users\USER
- Create the file: *.wslconfig*
- Enter the following:
  
    ``` txt
    [wsl2]
    memory = 2GB
    processors = 1
    ```

- Save and restart the *LxssManager* service

## Cool things to run with docker

A list of docker containers

### Powershell in Docker

Run the container

``` sh
docker run -it mcr.microsoft.com/azure-powershell
```

Trigger script in Powershell in Docker

``` sh
docker run -it -v C:\Users\username\src:/src mcr.microsoft.com/azure-powershell:3.6.1-ubuntu-18.04 pwsh -file /src/script.ps1
```

### webtop

Sources:

- <https://github.com/linuxserver/docker-webtop>
- <https://www.linuxserver.io/blog/2021-05-05-meet-webtops-a-linux-desktop-environment-in-your-browser>

``` sh
docker run -d --name=webtop -e PUID=1000 -e PGID=1000 -e TZ=Europe/London -p 3000:3000 -v /home --shm-size="1gb" --restart unless-stopped ghcr.io/linuxserver/webtop
```

If you lose your password you can reset it by execing into the container as root:

``` sh
docker exec -it webtop passwd abc
```

### I2P

Sources:

- <https://geti2p.net/de/download>
- <https://hub.docker.com/r/meeh/i2p.i2p/>

``` sh
docker pull meeh/i2p.i2p
```

### Drawio

Sources:

- <https://github.com/fjudith/docker-draw.io>

``` sh
docker run -it --rm --name="draw" -p 8080:8080 -p 8443:8443 fjudith/draw.io
```

### NoteCalc

Sources:

- <https://github.com/bbodi/notecalc3>

``` sh
git clone https://github.com/bbodi/notecalc3.git
cd notecalc3
docker build . --tag notecalc3
docker run --rm -d -p 5000:5000 notecalc3
```

### Archive Box

Sources:

- <https://github.com/ArchiveBox/ArchiveBox>
- <https://github.com/ArchiveBox/ArchiveBox/wiki/Docker>
- <https://nixintel.info/osint-tools/make-your-own-internet-archive-with-archive-box/>

``` sh
docker run -v $PWD:/data archivebox/archivebox init
docker run -v $PWD:/data archivebox/archivebox add 'https://0xfab1.net'
docker run -v $PWD:/data -it archivebox/archivebox manage createsuperuser
docker run -v $PWD:/data -p 8000:8000 archivebox/archivebox server 0.0.0.0:8000
```

### Wireguard

Sources:

- <https://github.com/linuxserver/docker-wireguard>

``` sh
docker pull ghcr.io/linuxserver/wireguard
```

### IPFS

Sources:

- <https://registry.hub.docker.com/r/ipfs/go-ipfs>
- <https://github.com/ipfs/go-ipfs>

``` sh
docker pull ipfs/go-ipfs
docker run -d --name ipfs_host -v $ipfs_staging:/export -v $ipfs_data:/data/ipfs -p 4001:4001 -p 127.0.0.1:8080:8080 -p 127.0.0.1:5001:5001 ipfs/go-ipfs:latest
docker exec ipfs_host ipfs swarm peers
docker logs -f ipfs_host
```

### Matrix Synapse

Sources:

- <https://registry.hub.docker.com/r/matrixdotorg/synapse/>

``` sh
docker pull matrixdotorg/synapse
docker run -it --rm --mount type=volume,src=synapse-data,dst=/data -e SYNAPSE_SERVER_NAME=my.matrix.host -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate
```

### Jellyfin

Sources:

- <https://github.com/jellyfin/jellyfin>
- <https://jellyfin.org/>

``` sh
docker pull jellyfin/jellyfin:latest
mkdir -p /srv/jellyfin/{config,cache}
docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media:/media --net=host jellyfin/jellyfin:latest
```

### Nextcloud

Sources:

- <https://hub.docker.com/_/nextcloud/>
- <https://nextcloud.com>

``` sh
docker run -d -p 8080:80 nextcloud
```

### Collabora Online

Sources:

- <https://nextcloud.com/collaboraonline/>
- <https://www.collaboraoffice.com/code/docker/>
- <https://github.com/CollaboraOnline/online>
- <https://collaboraonline.github.io/>

``` sh
docker run -d -p 8080:80 nextcloud
```

### Burpsuite

``` sh
docker run -d --name burpsuite -e DISPLAY -v ${HOME}:/home/burpsuite -v /tmp/.X11-unix/:/tmp/.X11-unix/ --p 8080:8080 alexandreoda/burpsuite
```

### mitmproxy

``` sh
docker run --rm -it -p 8080:8080 mitmproxy/mitmproxy
```

### pytorch

``` sh
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```

### Archivebox

``` sh
docker run -v ${PWD}/data -it archivebox/archivebox init --setup
docker run -v ${PWD}/data -p 8000:8000 archivebox/archivebox
```

### Kali

``` sh
docker pull kalilinux/kali-rolling
```

### Croc

``` sh
docker run -d -p 9009-9013:9009-9013 -e CROC_PASS='YOURPASSWORD' schollz/croc
croc --pass YOURPASSWORD --relay "localhost:9009" send file.txt
```

### Standard Notes

``` sh
docker run -d -p 3001:3001 --env-file=your-env-file standardnotes/web:stable
```

### Windows 2000

A Docker image for Windows 2000 Advanced Server with SP4. ([docker](https://hub.docker.com/r/hectormolinero/qemu-win2000) [github](https://github.com/hectorm/docker-qemu-win2000))

``` sh
docker run --detach --name qemu-win2000 --device /dev/kvm --publish 127.0.0.1:3389:3389/tcp --publish 127.0.0.1:5900:5900/tcp --publish 127.0.0.1:6080:6080/tcp docker.io/hectormolinero/qemu-win2000:latest
```

The instance can be accessed from:

- RDP (3389/TCP): any RDP client, login with Administrator / password.
- VNC (5900/TCP): any VNC client, without credentials.
- noVNC (6080/TCP): <http://127.0.0.1:6080/vnc.html>
- Shell: docker exec -it qemu-win2000 vmshell
