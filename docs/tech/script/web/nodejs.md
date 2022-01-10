# Node-js

## NPM

Use [list-scripts](https://www.npmjs.com/package/list-scripts) and [npm-list-scripts](https://www.npmjs.com/package/npm-list-scripts) to get a list of available npm script including what each script does.

``` npm
npm i -g list-scripts npm-list-scripts
```

Use [ncu](https://www.npmjs.com/package/npm-check-updates) to check the packages in your `package.json` file and gives you major and minor package updates info.

``` npm
npm i -g npm-check-updates
```

You can use [loop](https://github.com/Miserlou/Loop) and [speed-test](https://www.npmjs.com/package/speed-test) to monitor your internet speed.

``` sh
loop --every 5s { date +"%T"; speed-test -b -v }
```

Use [npm-scripts-tree](https://www.npmjs.com/package/npm-scripts-tree) to understand the dependencies between scripts calling other scripts.

``` npm
npm i -g npm-scripts-tree
```

With [npkill](https://github.com/voidcosmos/npkill) you can list any node_modules directories in your system and see the space they take up to delete the ones no longer needed.

``` npm
npm i -g npkill
```
