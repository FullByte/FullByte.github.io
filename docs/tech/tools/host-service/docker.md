# Docker

| What          | Where                                                                    |
| ------------- | ------------------------------------------------------------------------ |
| Official Page | <https://www.docker.com/>                                                |
| Docs          | <https://docs.docker.com/get-started/>                                   |
| Download      | <https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe> |
| Windows       | `choco install docker-desktop`                                           |

Links:

- More: <https://github.com/hexops/dockerfile>
- Many Images: <https://hub.docker.com/u/linuxserver/>
- how-to-clean-text-data-at-the-command-line <https://www.ezzeddinabdullah.com/posts/how-to-clean-text-data-at-the-command-line>

## Basics

``` txt
                  ##         .
            ## ## ##        ==
         ## ## ## ## ##    ===
     /"""""""""""""""""\___/ ===
~~~ {~~ ~~~~ ~~~ ~~~~ ~~~ ~ /  ===- ~~~
     \______ o           __/
       \    \         __/
        \____\_______/
```

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

run this in Ubuntu WSL

``` sh
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common libssl-dev libffi-dev git wget nano

sudo groupadd docker
sudo usermod -aG docker ${USER}

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update

sudo apt-get install -y docker-ce containerd.io docker-compose
sudo update-alternatives --config iptables
```

Add this to your `~/.profile`

```sh
if grep -q "microsoft" /proc/version > /dev/null 2>&1; then
    if service docker status 2>&1 | grep -q "is not running"; then
        wsl.exe --distribution "${WSL_DISTRO_NAME}" --user root \
            --exec /usr/sbin/service docker start > /dev/null 2>&1
    fi
fi
```

Test Docker in your Ubuntu WSL:

```sh
docker run hello-world
```

In case this didn't work try to restart wsl and try again

```sh
wsl --shutdown
```

To communicate containers don't use localhost, point to: [ubuntu terminal]. This is usually the first IP that appears when running this command:

```sh
ip addr | grep eth0 | grep inet
```

To ensure docker service is running on startup to workaround having to deal with sudo

```sh
wsl.exe -u root service docker status || wsl.exe -u root service docker start
```

To limit ressources create a file in the user's folder `C:\Users\<User>\.wslconfig` and add the following information.

```txt
[wsl2]
memory = 4GB # Limits memory
processors = 2 # Limits virtual processors
```

Save and restart the `LxssManager` service.

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

Start docker service

``` sh
sudo service docker start
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

## Maintainance

Search through all images to find and delete the ones without active references.
The -a tag will keep images that are tagged but not in use. (see [Docs](https://docs.docker.com/engine/reference/commandline/image_prune/) for more)

``` sh
docker image prune -a --volumes
```

Images available locally:

``` sh
docker image ls
```

Remove a specific image:

``` sh
docker image rm IMAGEID
```

Storage used by images locally:

``` sh
sudo du -sh /var/lib/docker/
```

To also remove all stopped containers run:

``` sh
docker container prune
```

And run ```docker image prune -a``` if you want to remove all images linked to stopped containers.


Stop all the containers

``` sh
docker stop $(docker ps -a -q)
```

Remove all the containers

``` sh
docker rm $(docker ps -a -q)
```

## Create Docker Compose Container

Example docker compose file

```sh
FROM nginx
COPY . /usr/share/nginx/html

Build: docker build -t img-static-site-example .
Run: docker run -it -d -p 80:80 img-static-site-example

docker-compose.yml

version: '3'
services:
  web:
    image: img-static-site-example
    build: .
    container_name: my-static-site
    restart: always
    ports:
      - "8080:80"
```

Build Container(s)

```sh
docker-compose build
```

Run Container(s)

```sh
docker-compose up -d
```


## Container

A list with some cool containerized applications:

| Application                                                                        | Description                                                                                                  | Run example instance                                                                                                                                                                                                                        |
|------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Mathics](https://hub.docker.com/r/mathicsorg/mathics)                             | Mathics is a general-purpose computer algebra system (CAS). It is an open-source alternative to Mathematica. | ```docker run --rm -it --name mathics-web -p 8000:8000 -v /tmp:/usr/src/app/data mathicsorg/mathics --mode ui```                                                                                                                            |
| [Powershell](https://mcr.microsoft.com/en-us/product/powershell/about)             | PowerShell 7 is a cross-platform automation and configuration tool.                                          | ```docker run -it mcr.microsoft.com/azure-powershell```                                                                                                                                                                                     |
| [Azure Powershell](https://mcr.microsoft.com/en-us/product/azure-powershell/about) | Azure ready commandline                                                                                      | ```docker run -it mcr.microsoft.com/azure-powershell|```                                                                                                                                                                                    |
| [webtop](https://github.com/linuxserver/docker-webtop)                             |                                                                                                              | ```docker run -d --name=webtop -e PUID=1000 -e PGID=1000 -e TZ=Europe/London -p 3000:3000 -v /home --shm-size="1gb" --restart unless-stopped ghcr.io/linuxserver/webtop```                                                                  |
| [drawio](https://github.com/fjudith/docker-draw.io)                                |                                                                                                              | ```docker run -it --rm --name="draw" -p 8080:8080 -p 8443:8443 fjudith/draw.io```                                                                                                                                                           |
| [Archive Box](https://github.com/ArchiveBox/ArchiveBox)                            |                                                                                                              | ```docker run -v $PWD:/data -p 8000:8000 archivebox/archivebox server 0.0.0.0:8000```                                                                                                                                                       |
| [Wireguard](https://github.com/linuxserver/docker-wireguard)                       |                                                                                                              | ```docker pull ghcr.io/linuxserver/wireguard```                                                                                                                                                                                             |
| [IPFS](https://registry.hub.docker.com/r/ipfs/go-ipfs)                             |                                                                                                              | ```docker run -d --name ipfs_host -v $ipfs_staging:/export -v $ipfs_data:/data/ipfs -p 4001:4001 -p 127.0.0.1:8080:8080 -p 127.0.0.1:5001:5001 ipfs/go-ipfs:latest && docker exec ipfs_host ipfs swarm peers && docker logs -f ipfs_host``` |
| [Matrix Synapse](https://registry.hub.docker.com/r/matrixdotorg/synapse/)          |                                                                                                              | ```docker run -it --rm --mount type=volume,src=synapse-data,dst=/data -e SYNAPSE_SERVER_NAME=my.matrix.host -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate```                                                             |
| [Jellyfin](https://github.com/jellyfin/jellyfin)                                   |                                                                                                              | ```mkdir -p /srv/jellyfin/{config,cache} && docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media:/media --net=host jellyfin/jellyfin:latest```                                                             |
| [Nextcloud](https://hub.docker.com/_/nextcloud/)                                   |                                                                                                              | ```docker run -d -p 8080:80 nextcloud```                                                                                                                                                                                                    |
| [Collabora Online](https://www.collaboraoffice.com/code/docker)                    |                                                                                                              | ```docker run -d -p 8080:80 nextcloud```                                                                                                                                                                                                    |
| [Burpsuite](https://portswigger.net/burp)                                          |                                                                                                              | ```docker run -d --name burpsuite -e DISPLAY -v ${HOME}:/home/burpsuite -v /tmp/.X11-unix/:/tmp/.X11-unix/ --p 8080:8080 alexandreoda/burpsuite```                                                                                          |
| [mitmproxy](https://mitmproxy.org/)                                                |                                                                                                              | ```docker run --rm -it -p 8080:8080 mitmproxy/mitmproxy```                                                                                                                                                                                  |
| [pytorch](https://pytorch.org/)                                                    |                                                                                                              | ```docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest```                                                                                                                                                                      |
| [Archivebox](https://archivebox.io/)                                               |                                                                                                              | ```docker run -v ${PWD}/data -it archivebox/archivebox init --setup && docker run -v ${PWD}/data -p 8000:8000 archivebox/archivebox```                                                                                                      |
| [Kali](https://www.kali.org/)                                                      |                                                                                                              | ```docker pull kalilinux/kali-rolling```                                                                                                                                                                                                    |
| [Croc](https://schollz.com/software/croc/)                                         |                                                                                                              | ```docker run -d -p 9009-9013:9009-9013 -e CROC_PASS='YOURPASSWORD' schollz/croc```                                                                                                                                                         |
| [Standard Notes](https://standardnotes.com/)                                       |                                                                                                              | ```docker run -d -p 3001:3001 --env-file=your-env-file standardnotes/web:stable```                                                                                                                                                          |
| [Windows 2000](https://hub.docker.com/r/hectormolinero/qemu-win2000)               |                                                                                                              | ```docker run --detach --name qemu-win2000 --device /dev/kvm --publish 127.0.0.1:3389:3389/tcp --publish 127.0.0.1:5900:5900/tcp --publish 127.0.0.1:6080:6080/tcp docker.io/hectormolinero/qemu-win2000:latest```                          |
| [Katana](https://github.com/projectdiscovery/katana)                               | web crawling and spidering framework                                                                         | ```docker run projectdiscovery/katana:latest -u https://0xfab1.net -system-chrome -headless```                                                                                                                                              |
| thelounge                                                                          |                                                                                                              | ```docker run --detach --name thelounge --publish 9000:9000 --volume ~/.thelounge:/var/opt/thelounge --restart always thelounge/thelounge:latest```                                                                                         |
| nativefier                                                                         |                                                                                                              | ```docker run --rm -v ~/nativefier-apps:/target/ nativefier/nativefier https://0xfab1.net/ /0xfab1.net/```                                                                                                                                  |

More examples:

- Trigger script in Powershell in Docker: ```docker run -it -v C:\Users\username\src:/src mcr.microsoft.com/azure-powershell:3.6.1-ubuntu-18.04 pwsh -file /src/script.ps1```
- Webtop reset password: ```docker exec -it webtop passwd supers3cure```

[NoteCalc](https://github.com/bbodi/notecalc3)

``` sh
git clone https://github.com/bbodi/notecalc3.git
cd notecalc3
docker build . --tag notecalc3
docker run --rm -d -p 5000:5000 notecalc3
```
