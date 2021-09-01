# Container

## Example using an existing docker container hosted on docker (croc)

To run [croc](https://github.com/schollz/croc) locally in docker we can run:

```docker
docker run -d -p 9009-9013:9009-9013 -e CROC_PASS='YOURPASSWORD' schollz/croc
croc --pass YOURPASSWORD --relay "localhost:9009" send file.txt
```

To do the same in [azure](https://portal.azure.com) we need to do the following:

First, login to azure and use the correct subscription:

```az
az login
az account set --subscription xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
```

Now, if not available, we need to create a container registry:

```az
TODO: Create container registry
```

Now we need add the desired existing docker container to our container registry

```az
az acr login --name fab1container --expose-token
docker login fab1container.azurecr.io
az acr update -n fab1container --admin-enabled true

docker pull schollz/croc # ???
docker push fab1container.azurecr.io/croc schollz/croc # ???
docker tag schollz/croc fab1container.azurecr.io/croc # ???

az acr repository list --name fab1container --output table
```

This container within the container registry can then be linked with a container instance.

```az
TODO: Create container instance
```

Now we run the container instance using the desired

```az
docker run -d -p 9009-9013:9009-9013 -e CROC_PASS='long-awesome-password' fab1container.azurecr.io/croc
```

The setup is complete and we should be able to use croc.

Example on how to use croc with the azure hosted relay:

I added a CNAME entry (croc) to my DNS entry `service.0xfab1.net` and added the alias: `xfab1.westeurope.azurecontainer.io` so that i can call the service @ `croc.service.0xfab1.net`.

```sh
croc --relay "croc.service.0xfab1.net:9009" send geohashing.png
```

Sources:

- <https://docs.microsoft.com/de-de/azure/container-registry/container-registry-authentication#admin-account>
- <https://docs.microsoft.com/de-de/azure/container-registry/container-registry-get-started-azure-cli>
