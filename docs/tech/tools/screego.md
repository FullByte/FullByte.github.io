# screego

| What          | Where                               |
|---------------|-------------------------------------|
| Official Page | <https://screego.net/>              |
| Source        | <https://github.com/screego/server> |

## Docker

Simple deploy

``` ps1
docker run --net=host -e SCREEGO\_EXTERNAL\_IP=YOUREXTERNALIP screego/server
```

Deploy on azure as "screengo125615"

``` ps1
az container create --resource-group rg-screego --name screego --image screego/server:1.7.0 --restart-policy OnFailure --location westeurope --cpu 2 --memory 4 --ports 80 443 3478 5050 --environment-variables SCREEGO\_EXTERNAL\_IP=104.46.44.218 --ip-address Public --dns-name-label screengo125615
```
