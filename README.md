# README

This is the source of my personal but public webpage ¯\\_(ツ)_/¯

[![Header](header.svg)](https://0xfab1.net)

## Stats

- Build Stats: ![mkdocs deploy](https://github.com/FullByte/FullByte.github.io/workflows/mkdocs%20gh-deploy/badge.svg?branch=master)
![website](https://img.shields.io/website-up-down-green-red/http/0xfab1.net.svg) [![volkswagen status](https://auchenberg.github.io/volkswagen/volkswargen_ci.svg?v=1)](https://github.com/auchenberg/volkswagen)
- Uptime: ![uptime](https://badgen.net/uptime-robot/status/m789173114-297aedeb6117b9a7cac6bb7e) ![day](https://badgen.net/uptime-robot/day/m789173114-297aedeb6117b9a7cac6bb7e) ![week](https://badgen.net/uptime-robot/week/m789173114-297aedeb6117b9a7cac6bb7e) ![month](https://badgen.net/uptime-robot/month/m789173114-297aedeb6117b9a7cac6bb7e) ![response](https://badgen.net/uptime-robot/response/m789173114-297aedeb6117b9a7cac6bb7e) ![IPv6](http://ipv6-test.com/button-ipv6-80x15.png)
- Github Stats: ![license](https://img.shields.io/github/license/Fullbyte/FullByte.github.io.svg)
![release](https://img.shields.io/github/release/Fullbyte/FullByte.github.io.svg)
![commits](https://img.shields.io/github/commits-since/Fullbyte/FullByte.github.io/1.svg)
![downloads](https://img.shields.io/github/downloads/Fullbyte/FullByte.github.io/total.svg)
![forks](https://img.shields.io/github/forks/Fullbyte/FullByte.github.io.svg)
![stars](https://img.shields.io/github/stars/Fullbyte/FullByte.github.io.svg)
![watchers](https://img.shields.io/github/watchers/Fullbyte/FullByte.github.io.svg)
- Issues: ![issues](https://img.shields.io/github/issues/Fullbyte/FullByte.github.io.svg)
![issues-closed](https://img.shields.io/github/issues-closed/Fullbyte/FullByte.github.io.svg)
![issues-pr](https://img.shields.io/github/issues-pr/Fullbyte/FullByte.github.io.svg)
![issues-pr-closed](https://img.shields.io/github/issues-pr-closed/Fullbyte/FullByte.github.io.svg)
- Contact: [![Chat on Gitter](https://badges.gitter.im/FullByte.github.io.svg)](https://gitter.im/FullByte/community/)
[![Twitter](https://img.shields.io/badge/twitter-%40zerogdoubled-%231da1f2)](https://twitter.com/zerogdoubled)

## 0xfab1

Documenting and publishing my projects and notes has been great exercise for me. As longs as this works well for me I will continue doing so :) The content may appear random as it deals with basically anything I find interesting and noteworthy. Thanks for your interest and I appreciate your pull-request for typos/errors in existing pages.

Visit:

- <https://0xfab1.net> for online view ([HTTPS](https://datatracker.ietf.org/doc/html/rfc2818) with [Let's Encrypt](https://letsencrypt.org/), supports [IPv4](https://datatracker.ietf.org/doc/html/rfc3344) and [IPv6](https://datatracker.ietf.org/doc/html/rfc8200))
- <https://fullbyte.github.io> in case I (or [my DNS provider](https://www.gandi.net)) messed something up
- <https://ipfs.0xfab1.net/> for access using [IPFS](https://ipfs.io/)
- <https://netlify.0xfab1.net> or <https://0xfab1.netlify.app/> for the [netlify](https://app.netlify.com) hosted version
- <https://azure.0xfab1.net> or <https://black-flower-0adbf0903.azurestaticapps.net> for the azure hosted version

This static website is built using [MkDocs](https://github.com/mkdocs/mkdocs/), [Material](https://github.com/squidfunk/mkdocs-material), [GitHub Pages](https://pages.github.com/) and [GitHub Actions](https://github.com/features/actions).

## Build

Run the following code to install and update the required tools using [python](https://www.python.org/) and build as well as serve the website (build is optional).

```sh
pip install --upgrade pip
pip install mkdocs mkdocs-material mkdocs-minify-plugin
```

If all above is already installed, make sure to use the latest version:

```sh
pip install -U mkdocs mkdocs-material mkdocs-minify-plugin
```

Building the site will reveal all possible issues with the current version:

```sh
mkdocs build
```

Run this command and navigate to <http://127.0.0.1:8000/> to browse locally.

```sh
mkdocs serve
```
