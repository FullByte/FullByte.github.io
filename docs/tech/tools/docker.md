# Docker

| What          | Where                                                                    |
| ------------- | ------------------------------------------------------------------------ |
| Official Page | <https://www.docker.com/>                                                |
| Docs          | <https://docs.docker.com/get-started/>                                   |
| Download      | <https://desktop.docker.com/win/stable/Docker%20Desktop%20Installer.exe> |
| Windows       | `choco install docker-desktop`                                           |
| Ubuntu        | ``                                                                       |

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
docker image prune -a
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
