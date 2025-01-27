# Node-js

## Versions

Use [NVM](https://github.com/nvm-sh/nvm) to switch between versions.

``` sh
nvm use 16
Now using node v16.9.1 (npm v7.21.1)
node -v
v16.9.1
nvm use 14
Now using node v14.18.0 (npm v6.14.15)
node -v
v14.18.0
```

## Install and Update

Use [chocolatey](https://chocolatey.org/) to install [node.js](https://nodejs.org) which includes [NPM](https://www.npmjs.com/) and install [yarn](https://classic.yarnpkg.com/en/) using npm once node.js is installed:

``` ps1
choco -y install nodejs
npm install --global yarn
```

Update node.js, NPM and yarn:

``` ps1
choco -y update nodejs
npm cache clean -f
npm install -g npm@latest
npm audit fix
yarn set version stable
```

## NPM

Use [list-scripts](https://www.npmjs.com/package/list-scripts) and [npm-list-scripts](https://www.npmjs.com/package/npm-list-scripts) to get a list of available npm script including what each script does.

``` sh
npm i -g list-scripts npm-list-scripts
```

Use [ncu](https://www.npmjs.com/package/npm-check-updates) to check the packages in your `package.json` file and gives you major and minor package updates info.

``` sh
npm i -g npm-check-updates
```

You can use [loop](https://github.com/Miserlou/Loop) and [speed-test](https://www.npmjs.com/package/speed-test) to monitor your internet speed.

``` sh
loop --every 5s { date +"%T"; speed-test -b -v }
```

Use [npm-scripts-tree](https://www.npmjs.com/package/npm-scripts-tree) to understand the dependencies between scripts calling other scripts.

``` sh
npm i -g npm-scripts-tree
```

With [npkill](https://github.com/voidcosmos/npkill) you can list any node_modules directories in your system and see the space they take up to delete the ones no longer needed.

``` sh
npm i -g npkill
```
