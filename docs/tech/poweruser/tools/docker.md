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
