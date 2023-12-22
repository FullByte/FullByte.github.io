# Croc

| What          | Where                                     |
|---------------|-------------------------------------------|
| Source        | <https://github.com/schollz/croc>         |
| Official Page | <https://schollz.com/tinker/croc6/>       |
| Windows       | `choco install croc`                      |
| Ubuntu        | `curl https://getcroc.schollz.com | bash` |

``` sh
croc --pass YOURPASSWORD --relay "localhost:9009" send file.txt
```

## Docker

Simple deploy

``` ps1
docker run -d -p 9009-9013:9009-9013 -e CROC_PASS='YOURPASSWORD' schollz/croc
```

Deploy on Azure

``` ps1
az container create --resource-group rg-croc --name croc --image schollz/croc --restart-policy OnFailure --location westeurope --cpu 1 --memory 1 --ports 9009 9010 9011 9012 9013 --environment-variables CROC_PASS=YOURPASSWORD --ip-address Public --dns-name-label croc231231
```

## Usage

Example how to use croc when running an own instance:

``` ps1
croc --pass YOURPASSWORD --relay "croc.service.0xfab1.net:9009" send file-or-folder.name
```
