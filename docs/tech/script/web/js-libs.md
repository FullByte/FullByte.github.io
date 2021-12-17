# JS Libraries

## Node.js

### Install and Update Node.js, NPM and yarn

Use [chocolatey](https://chocolatey.org/) to install [node.js](https://nodejs.org) which includes [NPM](https://www.npmjs.com/) and install [yarn](https://classic.yarnpkg.com/en/) using npm once node.js is installed:

``` ps11
choco -y install nodejs
npm install --global yarn
```

Update node.js, NPM and yarn:

``` ps11
choco -y update nodejs
npm cache clean -f
npm install -g npm@latest
npm audit fix
yarn set version stable
```

## d3.js

https://threejs.org/

## Three.js

https://d3js.org/
