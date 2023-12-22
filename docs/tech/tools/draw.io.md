# Draw.io

| What     | Where                                       |
|----------|---------------------------------------------|
| Source   | <https://github.com/jgraph/drawio>          |
| Download | <https://github.com/jgraph/drawio/releases> |
| Online   | <https://app.diagrams.net/>                 |
| Windows  | `choco install drawio`                        |

## Create and edit SVG in vscode

Create and edit SVG files nativly in VSCoode with Draw.io with a draw.io extension:

1. [Install](vscode:extension/hediet.vscode-drawio) the [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) for [Visual Studio Code](https://code.visualstudio.com/) by [Henning Dieterichs](https://marketplace.visualstudio.com/publishers/hediet)
2. Create a new file called whatever.drawio.svg
3. Open the file in VScode and the draw.io extension should pop-up an enable editing.
4. Link the SVG file to e.g. a markdown or web document

Example file showing the process:

![vscode_drawio](_example.drawio.svg)

## Create a mockup

Draw.io enables quick an easy mockup creation for simple GUI interfaces.
The possiblities are limited but it is an excellent first mockup draft method to figure out what you need.

Add the mockup shapes:

- Open Shapes
- click on "More Shapes"
- Navigate to Software → Mockups
- Add Mockups

Create your first page. Use that design as a template for further pages.
Create a link to other pages for specific buttons.

Export as HTML to demo the mockup online/offline.

## Drawio in VScode

Install using choco: ```choco install vscode-drawio```

## Docker

Simple deploy

``` ps1
docker run -d -p 80:8080 jgraph/drawio
```

Deploy with HTTPS via Lets Encrypt

``` ps1
docker run -it -m1g -e LETS\_ENCRYPT\_ENABLED=true --rm --name="draw" -p 80:80 -p 443:8443 jgraph/drawio
```

Deploy on azure as "drawio-demo"

``` ps1
az container create --resource-group rg-drawio --name drawio --image jgraph/drawio --restart-policy OnFailure --location westeurope --cpu 1 --memory 1 --ports 80 443 --environment-variables LETS\_ENCRYPT\_ENABLED=true PUBLIC\_DNS=drawio-demo.westeurope.azurecontainer.io KEYSTORE\_PASS=password --ip-address Public --dns-name-label drawio-demo

certbot --force-renewal -d drawio-demo.westeurope.azurecontainer.io
```
