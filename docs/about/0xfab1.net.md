# 0xfab1.net

![Follower](https://img.shields.io/github/followers/Fullbyte.svg?style=social&label=Follow&maxAge=2592000) ![license](https://img.shields.io/github/license/Fullbyte/FullByte.github.io.svg) ![release](https://img.shields.io/github/release/Fullbyte/FullByte.github.io.svg) ![commits](https://img.shields.io/github/commits-since/Fullbyte/FullByte.github.io/1.svg) ![downloads](https://img.shields.io/github/downloads/Fullbyte/FullByte.github.io/total.svg) ![forks](https://img.shields.io/github/forks/Fullbyte/FullByte.github.io.svg) ![stars](https://img.shields.io/github/stars/Fullbyte/FullByte.github.io.svg) ![watchers](https://img.shields.io/github/watchers/Fullbyte/FullByte.github.io.svg) ![issues](https://img.shields.io/github/issues/Fullbyte/FullByte.github.io.svg) ![issues-closed](https://img.shields.io/github/issues-closed/Fullbyte/FullByte.github.io.svg) ![issues-pr](https://img.shields.io/github/issues-pr/Fullbyte/FullByte.github.io.svg) ![issues-pr-closed](https://img.shields.io/github/issues-pr-closed/Fullbyte/FullByte.github.io.svg)

## MkDocs

[MkDocs](https://github.com/MkDocs/MkDocs/) is a great way to host a simple, static website. This website uses [Material for MkDocs](https://github.com/squidfunk/MkDocs-material). Material for MkDocs is a theme for MkDocs, a static site generator geared towards (technical) project documentation.

Use docker or python to quickly create and host a static website:

### Host MkDocs locally with docker

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git # clone repo
cd FullByte.github.io # Go to main folder
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/MkDocs-material # run the container
```

### Serve MkDocs locally with python

Run this once to install all requirements:

``` sh
choco install -y python
python -m pip install --upgrade pip
pip install MkDocs
pip install MkDocs-material
```

Run this in the folder of the MkDocs.yml file to host the MkDocs page:

``` sh
MkDocs serve
```

### Create page

Overriding template blocks: <https://www.mkdocs.org/user-guide/customizing-your-theme/#using-the-theme-custom_dir>

### Extensions

[MkDocs-material](https://squidfunk.github.io/mkdocs-material/) is a great theme and comes integrated with the pymkdown extensions, which lets you add tabbed code blocks, progress bars, task lists, keyboard symbols and more.

Further plugins:

- [MkDocs-minify-plugin](https://github.com/byrnereese/MkDocs-minify-plugin): `pip install MkDocs-minify-plugin`
- [MkDocs-redirects](https://github.com/datarobot/MkDocs-redirects): `pip install MkDocs-redirects`

## Static Website Hosting Services

This website is hosted/built using the following services:

| Service                                                  | Direct Link                                                           | 0xfab1 CNAME                      |
| -------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------- |
| [GitHub Pages](https://pages.github.com/)                | [0xfab1@github](https://fullbyte.github.io)                           | <https://www.0xfab1.net/>         |
| [IPFS](https://ipfs.io/) with [fleek](https://fleek.co/) | [0xfab1@IFPS](http://fb62c5359b88d00d5924.b-cdn.net)                  | <https://ipfs.0xfab1.net/>        |
| [Netlify](https://www.netlify.com/)                      | [0xfab1@netlify](https://0xfab1.netlify.app/)                         | <https://netlify.0xfab1.net>      |
| [Azure](https://azure.microsoft.com)                     | [0xfab1@azure](https://black-flower-0adbf0903.azurestaticapps.net)    | <https://azure.0xfab1.net>        |
| [Digital Ocean](https://m.do.co/c/0ef5c6b3f680)          | [0xfab1@digitalocean](https://oxfab1-3l4ou.ondigitalocean.app/)       | <https://digitalocean.0xfab1.net> |
| [Vercel](https://vercel.com/)                            | [0xfab1@vercel](https://0xfab1.vercel.app/)                           | <https://vercel.0xfab1.net/>      |
| [cloudflare](https://www.cloudflare.com/)                | [0xfab1@cloudflare](https://fullbyte-github-io.pages.dev)             | <https://cloudflare.0xfab1.net/>  |
| [Render](https://render.com/)                            | [0xfab1@render](https://zeroxfab1.onrender.com)                       | <https://render.0xfab1.net>       |
| [Railway](https://railway.app)                           | [0xfab1@railway](https://fullbytegithubio-production.up.railway.app/) | <https://railway.0xfab1.net>      |
| [koyeb](https://app.koyeb.com)                           | [0xfab1@koyeb](https://0xfab1-fullbyte.koyeb.app/)                    | <https://koyeb.0xfab1.net>        |
| [AWS S3](https://aws.amazon.com/s3/)                     | TODO                                                                  | TODO                              |
| [Gitlab Pages](https://about.gitlab.com)                 | TODO                                                                  | TODO                              |

I tried these services but they didn't suit me for my deployment at the time tested*:

- [Heroku](https://www.heroku.com) - php workaround breaks other builds
- [edg.io](https://edg.io/) - annoying DNS and build setup
- [Fly.io](https://fly.io/) - complicated build/requires extra files and github action changes
- [Surge](https://surge.sh/) - complicated build/requires extra files and github action changes
- [Firebase](https://console.firebase.google.com/) - complicated build/requires extra files and github action changes
- [Feta](https://www.deta.sh/) - complicated build/requires extra files and github action changes
- [Hostman](https://hostman.com) - no free option
- [Qovery](https://console.qovery.com) - looks great but didn't get it to work for simple static websites
- [Statically](https://statically.io) - great for one-pagers, not suitable for 0xfab1.net
- [Linode](https://www.linode.com) - no free option

*happy to learn from you how I can use them using a simple, automated deployment method for my static website :)

## Github Pages

To honor [this post](https://rakhim.org/images/honestly-undefined/blogging.jpg) (and ensure the message remains true) I will use my own website as an example and show how I configured the static web app and make it to work the way it does.

I am using [Github Pages](https://pages.github.com/) to host the content, [Mkdocs](https://www.mkdocs.org/) to create the website from markdown files as input and have own [domain](https://0xfab1.net/) for a nicer URL.

### Github Pages Repo

I created a repo named `FullByte.github.io` (Replace "FullByte" with your github username). Enable github pages for this repo in settings page of the repo. You will by default have a page available at [FullByte.github.io](https://FullByte.github.io).

### Custom Domain

[Mkdocs](https://www.mkdocs.org/) specifically uses the branch "gh-pages" by default to build the static website that will be served.

I added a [custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) "0xfab1.net" and added a file in the main folder of my repo called [CNAME](https://github.com/FullByte/FullByte.github.io/blob/master/CNAME) with one line containing my domain "0xfab1.net".

I added the following IPv4 DNS records (`dig 0xfab1.net +noall +answer -t A`):

```dns
0xfab1.net.             0       IN      A       185.199.108.153
0xfab1.net.             0       IN      A       185.199.109.153
0xfab1.net.             0       IN      A       185.199.110.153
0xfab1.net.             0       IN      A       185.199.111.153
```

as well as these IPv6 DNS records (`dig 0xfab1.net +noall +answer -t AAAA`):

```dns
0xfab1.net.             0       IN      AAAA    2606:50c0:8000::153
0xfab1.net.             0       IN      AAAA    2606:50c0:8001::153
0xfab1.net.             0       IN      AAAA    2606:50c0:8002::153
0xfab1.net.             0       IN      AAAA    2606:50c0:8003::153
```

and a CNAME record for www.0xfab1.net (`dig www.0xfab1.net +noall +answer -t CNAME`):

```dns
www.0xfab1.net.         0       IN      CNAME   fullbyte.github.io.
```

### Github Actions

Every time I commit to main I want the page to re-build so that the page is up-to-date. I currently don't use branches but this could be a good method to commit changes that should not yet be published. Once ready to publish, create a pull request of your branch and merge it to main.

My [github action to build the static webpage using mkdocs](https://github.com/FullByte/FullByte.github.io/blob/master/.github/workflows/build-0xfab1.yml) looks as follows and is based on [this documentation](https://www.mkdocs.org/user-guide/deploying-your-docs/):

``` yaml
name: mkdocs gh-deploy

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    name: Build and Deploy Documentation
    runs-on: ubuntu-latest
    steps:
      - name: Checkout main
        uses: actions/checkout@v2

      - name: Set up Python 3.10
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

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
