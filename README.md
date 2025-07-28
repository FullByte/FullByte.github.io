# README

[![Header](header.svg)](https://0xfab1.net)

This is the source of my personal, public web page ```¯\_(ツ)_/¯```

Publishing my projects and notes has been great exercise for me.
As long as this works well for me I will continue doing so :)
The content may appear random as it deals with basically anything I find interesting and noteworthy :)

Visit <https://0xfab1.net> for online view.
Built with [Github Actions](https://github.com/features/actions), [Github Pages](https://pages.github.com/), [Let's Encrypt](https://letsencrypt.org/) and [MkDocs](https://github.com/mkdocs/mkdocs/) with [Material](https://github.com/squidfunk/mkdocs-material) theme.

Thanks for your interest and I appreciate your [feedback](#contact) and/or [pull-request(s)](#contribute) for typos/errors in existing pages!

## Stats

| Type   | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Build  | ![GitHub last commit](https://img.shields.io/github/last-commit/FullByte/FullByte.github.io?color=4cae4f&label=last%20update&style=plastic) [![volkswagen status](https://auchenberg.github.io/volkswagen/volkswargen_ci.svg?v=1)](https://github.com/auchenberg/volkswagen)       |
| Uptime | ![uptime](https://badgen.net/uptime-robot/status/m789173114-297aedeb6117b9a7cac6bb7e) ![day](https://badgen.net/uptime-robot/day/m789173114-297aedeb6117b9a7cac6bb7e) ![month](https://badgen.net/uptime-robot/month/m789173114-297aedeb6117b9a7cac6bb7e) ![response](https://badgen.net/uptime-robot/response/m789173114-297aedeb6117b9a7cac6bb7e) |
| Repo   | ![license](https://img.shields.io/github/license/Fullbyte/FullByte.github.io.svg) ![forks](https://img.shields.io/github/forks/Fullbyte/FullByte.github.io.svg) ![stars](https://img.shields.io/github/stars/Fullbyte/FullByte.github.io.svg) ![watchers](https://img.shields.io/github/watchers/Fullbyte/FullByte.github.io.svg)                                                                                                                                                         |
| Issues | ![issues](https://img.shields.io/github/issues/Fullbyte/FullByte.github.io.svg) ![issues-closed](https://img.shields.io/github/issues-closed/Fullbyte/FullByte.github.io.svg) ![issues-pr](https://img.shields.io/github/issues-pr/Fullbyte/FullByte.github.io.svg) ![issues-pr-closed](https://img.shields.io/github/issues-pr-closed/Fullbyte/FullByte.github.io.svg)                                                                                                                   |

## Build and Run

If you want to run the [latest official docker hub build](https://hub.docker.com/repository/docker/0xfab1/0xfab1.net) use this command and view result here: <http://127.0.0.1:8000/>

``` sh
docker run -it --rm -p 8000:8000 0xfab1/0xfab1.net serve -a 0.0.0.0:8000
```

### Python and Mkdocs

Clone this repository with [git](https://git-scm.com/downloads).
To create the page you need [python](https://www.python.org/), and the extension for mkdocs and some mkdocs addons.
View the result here: <http://127.0.0.1:8080/>

``` sh
pip install --upgrade pip
pip install -r requirements.txt --upgrade
git clone https://github.com/FullByte/FullByte.github.io.git 0xfab1.net
cd 0xfab1.net
mkdocs serve -a localhost:8080 --dirtyreload --watch-theme -v
```

### Docker

Alternatively use [docker](https://www.docker.com/) to run a container with all required tools + website enabled. This repository contains a `dockerfile` in the main folder which can be used to build a new container with this command. View the result here: <http://127.0.0.1:8000/>

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git 0xfab1.net
cd 0xfab1.net
docker build -f dockerfile -t 0xfab1 .
docker run -d -p 80:80 -p 443:443 -v ./letsencrypt:/etc/letsencrypt -v ./certbot:/var/www/certbot --name website 0xfab1
```

### Podman

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git 0xfab1.net
cd 0xfab1.net
podman build -f dockerfile -t 0xfab1 .
podman run -d -p 80:80 -p 443:443 -v ./letsencrypt:/etc/letsencrypt:Z -v ./certbot:/var/www/certbot:Z --name website 0xfab1
```

## Contribute

I appreciate your pull-request for typos/errors in existing pages. If you think something is generally wrong or I missed to link you/someone where appropriate, please let me know!

- Fork the current version (e.g. with [github cli](https://cli.github.com/)): ```gh repo fork https://github.com/FullByte/FullByte.github.io.git```)
- Do the changes you want to make and commit the updates to your fork.
- Test the result by [building](#build-and-run) the site with your update(s).
- If there are no errors and you are happy to share the change, open a pull request and briefly tell what you updated and why.

Thank you for your contribution :)

## Contact

![Mastodon](https://img.shields.io/mastodon/follow/109640942794566265?domain=https%3A%2F%2Fsocial.lol&style=social)

[![Twitter](https://img.shields.io/badge/twitter-%40zerogdoubled-%231da1f2)](https://twitter.com/zerogdoubled)

![qrcode](0xfab1-qrcode.png)
