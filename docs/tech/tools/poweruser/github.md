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

Press "." in any github repo to open the editor.

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

## Github Pages

To honor [this post](https://rakhim.org/images/honestly-undefined/blogging.jpg) (and ensure the message remains true) I will use my own website as an example and show how I configured the static web app and make it to work the way it does.

I am using [Github Pages](https://pages.github.com/) to host the content, [Mkdocs](https://www.mkdocs.org/) to create the website from markdown files as input and have own [domain](https://0xfab1.net/) for a nicer URL.

### Github Pages Repo

I created a repo named `FullByte.github.io` (Replace "FullByte" with your github username). Enable github pages for this repo in settings page of the repo. You will by default have a page available at [FullByte.github.io](FullByte.github.io).

### Custom Domain

Here is a overview of the Github Pages settings I use:

![Github Pages](_github-pages.png)

[Mkdocs](https://www.mkdocs.org/) specifically uses the branch "gh-pages" by default to build the static website that will be served.

I added a custom domain "0xfab1.net" and added a file in the main folder of my repo called [CNAME](https://github.com/FullByte/FullByte.github.io/blob/master/CNAME) with one line containing my domain "0xfab1.net".

I added the following DNS records to the domain:

```dns
@ 1800 IN A 185.199.108.153
@ 1800 IN A 185.199.109.153
@ 1800 IN A 185.199.110.153
@ 1800 IN A 185.199.111.153
www 10800 IN CNAME fullbyte.github.io.
```

### Github Actions

Every time I commit to main I want the page to re-build so that the page is up-to-date. I currently don't use branches but this could be a good method to commit changes that should not yet be published. Once ready to publish, create a pull request of your branch and merge it to main.

My [github action to build the static webpage using mkdocs](https://github.com/FullByte/FullByte.github.io/blob/master/.github/workflows/main.yml) looks as follows and is based on [this documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/):

```yaml
name: mkdocs gh-deploy

on:
  push:
    branches: [master]
  pull_request:
    branches: [master]

jobs:
  build:
    name: Build and Deploy Documentation
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Master
        uses: actions/checkout@v2

      - name: Set up Python 3.9
        uses: actions/setup-python@v2
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs-material
      - name: Deploy
        run: |
          git pull
          mkdocs gh-deploy
```

Additionally, I am running a [security scan](https://slscan.io/en/latest/integrations/code-scan) on every push and check the URLs I share regularly via cron job triggered github action.

There are many other nice things that could be done here. The main important part is to trigger the markdown to static website generator as github action on new commits so that the site is automatically built whenever you commit new content.
