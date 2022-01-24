# README

This is the source of my personal but public webpage ```¯\_(ツ)_/¯```

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

## About

Publishing my projects and notes has been great exercise for me. As longs as this works well for me I will continue doing so :) The content may appear random as it deals with basically anything I find interesting and noteworthy ```¯\_(ツ)_/¯```

Thanks for your interest and I appreciate your [pull-request](#contribute) for typos/errors in existing pages!

Visit <https://0xfab1.net> for online view ([HTTPS](https://datatracker.ietf.org/doc/html/rfc2818) with [Let's Encrypt](https://letsencrypt.org/), supports [IPv4](https://datatracker.ietf.org/doc/html/rfc3344) and [IPv6](https://datatracker.ietf.org/doc/html/rfc8200)). This static website is based on [MkDocs](https://github.com/mkdocs/mkdocs/) with [Material](https://github.com/squidfunk/mkdocs-material) and [minify](https://github.com/byrnereese/mkdocs-minify-plugin) and [rss](https://github.com/Guts/mkdocs-rss-plugin) plugin. The website is built using [GitHub Actions](https://github.com/features/actions) and served by [GitHub Pages](https://pages.github.com/) as well as these alternative hosts:

- [0xfab1@github](https://fullbyte.github.io) using [GitHub Pages](https://pages.github.com/) (alternative link: <https://www.0xfab1.net/>)
- [0xfab1@IFPS](http://fb62c5359b88d00d5924.b-cdn.net) using [IPFS](https://ipfs.io/) with [fleek](https://fleek.co/) (alternative link: <https://ipfs.0xfab1.net/>)
- [0xfab1@netlify](https://0xfab1.netlify.app/) using [Netlify](https://www.netlify.com/) (alternative link: <https://netlify.0xfab1.net>)
- [0xfab1@azure](https://black-flower-0adbf0903.azurestaticapps.net) using [Azure](https://azure.microsoft.com) (alternative link: <https://azure.0xfab1.net>)
- [0xfab1@digitalocean](https://oxfab1-3l4ou.ondigitalocean.app/) using [Digital Ocean](https://m.do.co/c/0ef5c6b3f680) (alternative link: <https://digitalocean.0xfab1.net>)
- [0xfab1@vercel](https://0xfab1.vercel.app/) using [Vercel](https://vercel.com/) (alternative link: <https://vercel.0xfab1.net/>)
- [0xfab1@surge](http://surge.0xfab1.net) using [serge.sh](https://surge.sh) (alternative link: <http://surge.0xfab1.net/>)
- [0xfab1@cloudflare](https://fullbyte-github-io.pages.dev) using [cloudflare](https://www.cloudflare.com/) (alternative link: <https://cloudflare.0xfab1.net/>)
- [0xfab1@layer0](https://0xfab1-layer0-0xfab1-net-production.layer0-limelight.link) using [layer0](https://www.layer0.co/) (alternative link: <https://layer0.0xfab1.net/>)

## Build

Run the following code to install and update the required tools using [python](https://www.python.org/) and build as well as serve the website (build is optional).

``` sh title="Install"
pip install --upgrade pip
pip install mkdocs mkdocs-material mkdocs-minify-plugin mkdocs-rss-plugin
```

If all above is already installed, make sure to use the latest version:

``` sh title="Update"
pip install -U mkdocs mkdocs-material mkdocs-minify-plugin mkdocs-rss-plugin
```

Building the site will reveal all possible issues with the current version:

``` sh title="Build"
mkdocs build -v
```

Run this command and navigate to <http://127.0.0.1:8888/> to browse locally.

``` sh title="Serve"
mkdocs serve -a localhost:8888 --dirtyreload --watch-theme -v
```

## Contribute

I appreciate your pull-request for typos/errors in existing pages. If you think something is generally wrong or I missed to link you/someone where appropiate, please let me know!

- Fork the current version.
- Change whatever needs an udpate.
- Test the reuslt by [building](#build) the site with your update.
- If there are no errors, open a pull request and tell what you updated and why.

Thanks for your contribution :)
