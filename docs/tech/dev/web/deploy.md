# Deploy

## Surge

[Surge.sh](https://surge.sh/) is a simple, single-command web publishing service to publish HTML, CSS, and JS for free, without leaving the command line.

These are the steps I took to host my site mkdocs based site on [surge.sh](https://surge.sh/).

Install: ```npm install --global surge``` (requires Node.js)
Deploy: ```surge E:\Website\0xfab1.net\site surge.0xfab1.net```

## Heroku

[Heroku](https://heroku.com) is not recommended for simple, static websites with HTML, CSS and JS. Heroku is there to host apps, not static websites.

These are the steps I took to host my site mkdocs based site on [Heroku](https://heroku.com) anyway:

Create the follwing files in your main mkdocs directory, then run the deploy process:

``` sh
echo '{}' > composer.json
echo '{ "formation": { "web": { "size": "free" } } }' > app.json
echo '<?php include_once("index.html"); ?>' > index.php
```

Adding this breaks the build for other hosts as some assume this is a PHP site and interprete the build wrong. For this reason I create the files above in a seperate branch named "heroku" with this command `mkdocs gh-deploy -b heroku`. Below is the github action to deploy 0xfab1.net on github and also prepare a branch build for heroku:

``` yaml
jobs:
  build:
    name: Build and Deploy Website
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Master
        uses: actions/checkout@v2

      - name: Set up Python 3.10
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install mkdocs dependencies
        run: |
          python -m pip install --upgrade pip          
          pip install mkdocs-material
          pip install mkdocs-minify-plugin
          pip install mkdocs-rss-plugin
          pip install mkdocs-video

      - name: Deploy Github Pages
        run: |
          git pull
          mkdocs gh-deploy
          mkdocs gh-deploy -b heroku
```

Now run the deploy on the correct branch and it should work :)

## Layer0

These are the steps I took to host my site mkdocs based site on layer0. [Here is the offical guide](https://docs.layer0.co/guides/mkdocs).

Add package.json and routes.js to you main mkdocs folder:

``` json title="package.json"
{
  "name": "mkdocs",
  "version": "1.0.0",
  "scripts": {
    "build": "python3 -m mkdocs build",
    "server": "python3 -m mkdocs serve",
    "layer0:dev": "layer0 dev",
    "postinstall": "pip3 install mkdocs mkdocs-material mkdocs-minify-plugin mkdocs-rss-plugin mkdocs-video",
    "layer0:build": "npm run build && layer0 build",
    "layer0:deploy": "npm run build && layer0 deploy"
  },
  "dependencies": {},
  "devDependencies": {
    "@layer0/cli": "^4.8.5",
    "@layer0/core": "^4.8.5",
    "@layer0/devtools": "^4.8.5",
    "@layer0/prefetch": "^4.8.5"
  }
}
```

``` js title="routes.js"
import { Router } from '@layer0/core'

const ONE_MINUTE = 60
const FAR_FUTURE = 60 * 60 * 24 * 365 * 10

const router = new Router()

router.match('/:path*', ({ serveStatic, cache }) => {
  cache({
    browser: false,
    edge: {
      maxAgeSeconds: FAR_FUTURE,
    },
  })
  serveStatic('site/:path*')
})

export default router
```

Init (run once) using Node.js [npx](https://nodejs.dev/learn/the-npx-nodejs-package-runner) and [nvm](https://github.com/nvm-sh/nvm):

``` sh
nvm use 14
npx @layer0/cli@latest init --name layer0.0xfab1.net --environment production --origin layer0.0xfab1.net --deploy
```

Deploy page (run for every update) using Node.js [npx](https://nodejs.dev/learn/the-npx-nodejs-package-runner) and [nvm](https://github.com/nvm-sh/nvm):

``` sh
nvm use 14
npm run build
npx @layer0/cli@latest deploy --site=layer0.0xfab1.net --environment=production
```

## Azure Static Website

To build the static site for Azure, I build it on the worker, then use `Azure/static-web-apps-deploy@v1` task to deploy the result.

``` yaml
name: Build and Deploy Website

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]
  workflow_dispatch:

jobs:
  build:
    name: Build and Deploy Website
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Master
        uses: actions/checkout@v2

      - name: Set up Python 3.10
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install mkdocs dependencies
        run: |
          pip install --upgrade pip          
          pip install mkdocs-material
          pip install mkdocs-minify-plugin
          pip install mkdocs-rss-plugin
          pip install mkdocs-video

      - name: Build 0xfab1.net for Azure
        run: |          
          mkdocs build

      - name: Deploy to Azure
        id: builddeploy
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_BLACK_FLOWER_0ADBF0903 }}
          repo_token: ${{ secrets.GITHUB_TOKEN }} 
          action: "upload"
          app_location: "site/"

  close_pull_request_job:
    if: github.event_name == 'pull_request' && github.event.action == 'closed'
    runs-on: ubuntu-latest
    name: Close Pull Request Job
    steps:
      - name: Close Pull Request
        id: closepullrequest
        uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_STATIC_WEB_APPS_API_TOKEN_BLACK_FLOWER_0ADBF0903 }}
          action: "close"
```
