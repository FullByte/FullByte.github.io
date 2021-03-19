# Github

## Info

|What|Where|
|-|-|
|Official Page|<https://github.com>|
|Docs|<https://docs.github.com>|
|Download|<https://desktop.github.com/>|
|Install|choco install github-desktop|

## RSS Feed for Commits

Add ".atom" to a given commit link to get an RSS Reader update on a given file/folder or the entire project.

For example:

- Link: <https://github.com/FullByte/FullByte.github.io/commits/master>
- RSS Feed: <https://github.com/FullByte/FullByte.github.io/commits/master.atom>

Add the atom link to your rss feed reader to get notified on updates.

## VScode online

Add "1s" to "github" to get the VScode GUI of the github repo you selected

Example:

- Standard: <https://github.com/FullByte/FullByte.github.io/>
- VScode: <https://github1s.com/FullByte/FullByte.github.io/>

## Helper

- Smee receives payloads then sends them to your locally running application: <https://smee.io/>
- Probot automates and improves your github workflows with pre-built apps: <https://probot.github.io/>
- Search for code: <https://gowalker.org/>

## Execute Gist/Github Script

You can run remote scripts from e.g. Github (either gists or raw content):

From powershell with github raw file:

**Windows**

```PowerShell
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/FullByte/project/master/file.file'))
```

From cmd with gist link:

```cmd
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/FullByte/000000000000000000000000000000000000/raw'))"
```

**Linux**

From bash

```bash
bash <(curl -Ls https://raw.githubusercontent.com/FullByte/scripts/master/something)
```
