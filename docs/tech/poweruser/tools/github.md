# Github

Info

| What           | Where                           |
|----------------|---------------------------------|
| Official Page  | <https://github.com>            |
| Service Status | <https://www.githubstatus.com/> |
| Docs           | <https://docs.github.com>       |
| Download       | <https://desktop.github.com/>   |
| Windows        | choco install github-desktop    |

## RSS Feed for Commits

Add ".atom" to a given commit link to get an RSS Reader update on a given file/folder or the entire project.

For example:

- Link: <https://github.com/FullByte/FullByte.github.io/commits/master>
- RSS Feed: <https://github.com/FullByte/FullByte.github.io/commits/master.atom>

Add the atom link to your rss feed reader to get notified on updates.

## VScode online

Press "." in any github repo to open the editor.

Add "1s" to "github" to get the VScode GUI of the github repo you selected

Example:

- Standard: <https://github.com/FullByte/FullByte.github.io/>
- VScode: <https://github1s.com/FullByte/FullByte.github.io/>

## SSH Keys

Get a users SSH Key:

<https://github.com/fullbyte.keys>

## Firewall

Get all IPs to whitelist for Github (Actions) from here:

<https://api.github.com/meta>

## Helper

- [Smee](https://smee.io/) receives payloads then sends them to your locally running application
- [Probot](https://probot.github.io/) automates and improves your github workflows with pre-built apps
- Use [gowalker](https://gowalker.org/) to search for code
- Look for popular projects by [number of stars](https://app.tooljet.io/applications/github-star-ranking)
- Use [githistory.xyz](https://githistory.xyz/) e.g. if this is your url: `https://github.com/FullByte/FullByte.github.io/blob/master/mkdocs.yml` replace `com` of github.com with `githistory.xyz` e.g. `https://github.githistory.xyz/FullByte/FullByte.github.io/blob/master/mkdocs.yml` to get a [nice view](https://github.githistory.xyz/FullByte/FullByte.github.io/blob/master/mkdocs.yml).

## Execute Gist/Github Script

You can run remote scripts from e.g. Github (either gists or raw content):

From powershell with github raw file:

**Windows**

``` ps1
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/FullByte/project/master/file.file'))
```

From cmd with gist link:

```cmd
PowerShell -NoProfile -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://gist.githubusercontent.com/FullByte/000000000000000000000000000000000000/raw'))"
```

**Linux**

From bash

``` sh
bash <(curl -Ls https://raw.githubusercontent.com/FullByte/scripts/master/something)
```
