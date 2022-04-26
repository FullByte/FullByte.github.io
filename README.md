# README

[![Header](header.svg)](https://0xfab1.net)

This is the source of my personal, public web page ```¯\_(ツ)_/¯```

Publishing my projects and notes has been great exercise for me. As longs as this works well for me I will continue doing so :) The content may appear random as it deals with basically anything I find interesting and noteworthy :)

Thanks for your interest and I appreciate your [pull-request](#contribute) for typos/errors in existing pages!

## Stats

| Status Type  | Status                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Build Stats  | ![GitHub last commit](https://img.shields.io/github/last-commit/FullByte/FullByte.github.io?color=4cae4f&label=last%20update&style=plastic) ![mkdocs deploy](https://github.com/FullByte/FullByte.github.io/workflows/mkdocs%20gh-deploy/badge.svg?branch=master) ![website](https://img.shields.io/website-up-down-green-red/http/0xfab1.net.svg) [![volkswagen status](https://auchenberg.github.io/volkswagen/volkswargen_ci.svg?v=1)](https://github.com/auchenberg/volkswagen)                                                                                                                       |
| Uptime       | ![uptime](https://badgen.net/uptime-robot/status/m789173114-297aedeb6117b9a7cac6bb7e) ![day](https://badgen.net/uptime-robot/day/m789173114-297aedeb6117b9a7cac6bb7e) ![week](https://badgen.net/uptime-robot/week/m789173114-297aedeb6117b9a7cac6bb7e) ![month](https://badgen.net/uptime-robot/month/m789173114-297aedeb6117b9a7cac6bb7e) ![response](https://badgen.net/uptime-robot/response/m789173114-297aedeb6117b9a7cac6bb7e) ![IPv6](http://ipv6-test.com/button-ipv6-80x15.png)                                                                                                                 |
| Github Stats | ![license](https://img.shields.io/github/license/Fullbyte/FullByte.github.io.svg) ![release](https://img.shields.io/github/release/Fullbyte/FullByte.github.io.svg) ![commits](https://img.shields.io/github/commits-since/Fullbyte/FullByte.github.io/1.svg) ![downloads](https://img.shields.io/github/downloads/Fullbyte/FullByte.github.io/total.svg) ![forks](https://img.shields.io/github/forks/Fullbyte/FullByte.github.io.svg) ![stars](https://img.shields.io/github/stars/Fullbyte/FullByte.github.io.svg) ![watchers](https://img.shields.io/github/watchers/Fullbyte/FullByte.github.io.svg) |
| Issues       | ![issues](https://img.shields.io/github/issues/Fullbyte/FullByte.github.io.svg) ![issues-closed](https://img.shields.io/github/issues-closed/Fullbyte/FullByte.github.io.svg) ![issues-pr](https://img.shields.io/github/issues-pr/Fullbyte/FullByte.github.io.svg) ![issues-pr-closed](https://img.shields.io/github/issues-pr-closed/Fullbyte/FullByte.github.io.svg)                                                                                                                                                                                                                                |

## Hosting

Visit <https://0xfab1.net> for online view ([HTTPS](https://datatracker.ietf.org/doc/html/rfc2818) with [Let's Encrypt](https://letsencrypt.org/), supports [IPv4](https://datatracker.ietf.org/doc/html/rfc3344) and [IPv6](https://datatracker.ietf.org/doc/html/rfc8200)). This static website is based on [MkDocs](https://github.com/mkdocs/mkdocs/) with [Material](https://github.com/squidfunk/mkdocs-material) and [minify](https://github.com/byrnereese/mkdocs-minify-plugin). The website is built using [GitHub Actions](https://github.com/features/actions) and served by [GitHub Pages](https://pages.github.com/) as well as these alternative hosts:

| Service                                                  | Link                                                                               | 0xfab1 CNAME                      |
|----------------------------------------------------------|------------------------------------------------------------------------------------|-----------------------------------|
| [GitHub Pages](https://pages.github.com/)                | [0xfab1@github](https://fullbyte.github.io)                                        | <https://www.0xfab1.net/>         |
| [IPFS](https://ipfs.io/) with [fleek](https://fleek.co/) | [0xfab1@IFPS](http://fb62c5359b88d00d5924.b-cdn.net)                               | <https://ipfs.0xfab1.net/>        |
| [Netlify](https://www.netlify.com/)                      | [0xfab1@netlify](https://0xfab1.netlify.app/)                                      | <https://netlify.0xfab1.net>      |
| [Azure](https://azure.microsoft.com)                     | [0xfab1@azure](https://black-flower-0adbf0903.azurestaticapps.net)                 | <https://azure.0xfab1.net>        |
| [Digital Ocean](https://m.do.co/c/0ef5c6b3f680)          | [0xfab1@digitalocean](https://oxfab1-3l4ou.ondigitalocean.app/)                    | <https://digitalocean.0xfab1.net> |
| [Vercel](https://vercel.com/)                            | [0xfab1@vercel](https://0xfab1.vercel.app/)                                        | <https://vercel.0xfab1.net/>      |
| [serge.sh](https://surge.sh)                             | [0xfab1@surge](http://surge.0xfab1.net)                                            | <http://surge.0xfab1.net/>        |
| [cloudflare](https://www.cloudflare.com/)                | [0xfab1@cloudflare](https://fullbyte-github-io.pages.dev)                          | <https://cloudflare.0xfab1.net/>  |
| [layer0](https://www.layer0.co/)                         | [0xfab1@layer0](https://0xfab1-layer0-0xfab1-net-production.layer0-limelight.link) | <https://layer0.0xfab1.net/>      |

If you want to run the [latest official docker hub build](https://hub.docker.com/repository/docker/0xfab1/0xfab1.net), use this command and view result here: <http://127.0.0.1:8000/>

``` sh
docker run -it --rm -p 8000:8000 0xfab1/0xfab1.net serve -a 0.0.0.0:8000
```

## Build and Run

Clone this repository with [git](https://git-scm.com/downloads). Alternativly fork this repository first (e.g. with [github cli](https://cli.github.com/)) if you want to change anything you want to later push back to this repository (see [Contribute](#contribute) ): ```gh repo fork https://github.com/FullByte/FullByte.github.io.git```

### Python and Mkdocs

To create the page you need [python](https://www.python.org/), mkdocs and some mkdocs addons:

``` sh
pip install --upgrade pip
pip install mkdocs mkdocs-material mkdocs-minify-plugin
git clone https://github.com/FullByte/FullByte.github.io.git 0xfab1.net
cd 0xfab1.net
mkdocs serve -a localhost:8000 --dirtyreload --watch-theme -v
```

View result here: <http://127.0.0.1:8000/>

### Docker

Alternativly Use [docker](https://www.docker.com/) to run a container with all required tools + website enabled. This repository contains a `dockerfile` in the main folder which can be used to build a new container with this command:

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git 0xfab1.net
cd 0xfab1.net
docker build . -t yourbuild
docker run -it --rm -p 8000:8000 yourbuild serve -a 0.0.0.0:8000
```

View result here: <http://127.0.0.1:8000/>

## Contribute

I appreciate your pull-request for typos/errors in existing pages. If you think something is generally wrong or I missed to link you/someone where appropiate, please let me know!

- Fork the current version (e.g. ```gh repo fork https://github.com/FullByte/FullByte.github.io.git```)
- Change whatever needs an udpate.
- Test the reuslt by [building](#build) the site with your update.
- If there are no errors, open a pull request and tell what you updated and why.

Thank you for your contribution :)

## Contact

[![Chat on Gitter](https://badges.gitter.im/FullByte.github.io.svg)](https://gitter.im/FullByte/community/)

[![Twitter](https://img.shields.io/badge/twitter-%40zerogdoubled-%231da1f2)](https://twitter.com/zerogdoubled)

![qrcode](0xfab1-qrcode.png)
