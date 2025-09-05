# 0xfab1.net

![Follower](https://img.shields.io/github/followers/Fullbyte.svg?style=social&label=Follow&maxAge=2592000) ![license](https://img.shields.io/github/license/Fullbyte/FullByte.github.io.svg) ![release](https://img.shields.io/github/release/Fullbyte/FullByte.github.io.svg) ![commits](https://img.shields.io/github/commits-since/Fullbyte/FullByte.github.io/1.svg) ![downloads](https://img.shields.io/github/downloads/Fullbyte/FullByte.github.io/total.svg) ![forks](https://img.shields.io/github/forks/Fullbyte/FullByte.github.io.svg) ![stars](https://img.shields.io/github/stars/Fullbyte/FullByte.github.io.svg) ![watchers](https://img.shields.io/github/watchers/Fullbyte/FullByte.github.io.svg) ![issues](https://img.shields.io/github/issues/Fullbyte/FullByte.github.io.svg) ![issues-closed](https://img.shields.io/github/issues-closed/Fullbyte/FullByte.github.io.svg) ![issues-pr](https://img.shields.io/github/issues-pr/Fullbyte/FullByte.github.io.svg) ![issues-pr-closed](https://img.shields.io/github/issues-pr-closed/Fullbyte/FullByte.github.io.svg)

## MkDocs

To honor [this post](https://rakhim.org/images/honestly-undefined/blogging.jpg) (and ensure the message remains true) I will use my own website as an example and show how I configured the static web app and make it work the way it does.

I am using [Github Pages](https://pages.github.com/) to host the content, [Mkdocs](https://www.mkdocs.org/) to create the website from markdown files as input and have my own [domain](https://0xfab1.net/) for a nicer URL.

[MkDocs](https://github.com/MkDocs/MkDocs/) is a great way to host a simple, static website. This website uses [Material for MkDocs](https://github.com/squidfunk/MkDocs-material) which is a theme for MkDocs.

To quickly create and host a static website (or rebuild this website), you have two options:

- Docker
- Python

### Docker

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git # clone repo
cd FullByte.github.io # Go to main folder
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/MkDocs-material # run the container
```

Previous Dockerfile (Legacy)

``` dockerfile
FROM python:3
RUN pip install --upgrade pip
RUN pip install mkdocs mkdocs-material mkdocs-minify-plugin
EXPOSE 8000
WORKDIR /
COPY docs ./docs
COPY overrides ./overrides
COPY mkdocs.yml .
ENTRYPOINT ["mkdocs"]
CMD ["serve", "-a", "0.0.0.0:8000"]
```

Optimized Dockerfile (Current - with Performance Enhancements)

``` dockerfile
FROM python:3-slim AS builder

# Create non-root user
RUN adduser --disabled-password mkdocs

# Install dependencies with cache mount
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir mkdocs mkdocs-material mkdocs-minify-plugin mkdocs-rss-plugin mkdocs-git-revision-date-localized-plugin mkdocs-htmlproofer-plugin pillow cairosvg

WORKDIR /site

# Copy files in order of change frequency (least to most)
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

COPY mkdocs.yml .
COPY overrides ./overrides
COPY image_optimizer.py .
COPY pre_build_hook.py .
COPY docs ./docs

# Run image optimization before build
RUN python image_optimizer.py --mode build --quiet

# Build with cache for MkDocs (with quiet logging)
RUN --mount=type=cache,target=/site/.cache \
    PYTHONWARNINGS=ignore mkdocs build 2>&1 | grep -v '\[git-revision-date-localized-plugin\]' | grep -v 'has no git logs' | grep -v 'First revision timestamp' | grep -v 'RSS-plugin.*Dates could not be retrieved' || true

FROM nginx:alpine
RUN apk add --no-cache certbot certbot-nginx

# Create directories for Let's Encrypt
RUN mkdir -p /etc/letsencrypt /var/lib/letsencrypt /var/www/certbot

# Add Brotli support
RUN apk add --no-cache nginx-mod-http-brotli

COPY --from=builder /site/site /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh

# Make entrypoint executable
RUN chmod +x /entrypoint.sh

EXPOSE 80
EXPOSE 443

VOLUME /etc/letsencrypt
VOLUME /var/lib/letsencrypt

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

ENTRYPOINT ["/entrypoint.sh"]
```

### Python

Run this once to install all requirements:

``` sh
choco install -y python
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Alternative installation (manual):

``` sh
pip install mkdocs
pip install mkdocs-material
pip install mkdocs-minify-plugin
pip install mkdocs-rss-plugin
pip install mkdocs-git-revision-date-localized-plugin
pip install mkdocs-htmlproofer-plugin
pip install pillow
pip install cairosvg
```

Run this in the folder of the mkdocs.yml file to host the MkDocs page:

``` sh
mkdocs serve
```

Or use the optimized build scripts with automatic image optimization:

``` sh
# Python build script (cross-platform)
python build.py --serve

# PowerShell build script (Windows)
.\build.ps1 -Serve

# Manual image optimization
python image_optimizer.py --mode build
```

### Create page

If you do not like the default design of a theme or something is missing or extra that needs to be removed it is possible to overwrite template blocks: <https://www.mkdocs.org/user-guide/customizing-your-theme/#using-the-theme-custom_dir>.

I use method to add some files as well as overwrite a few things. It is generally more work as sometimes there are changes in mkdocs or material that force you to update your overrides as well. To see what I added to my "overrides" folder look here: <https://github.com/FullByte/FullByte.github.io/tree/main/overrides>

### Extensions

[MkDocs-material](https://squidfunk.github.io/mkdocs-material/) is a great theme and comes integrated with the pymkdown extensions, which lets you add tabbed code blocks, progress bars, task lists, keyboard symbols and more.

Currently installed plugins for enhanced functionality:

- **[mkdocs-minify-plugin](https://github.com/byrnereese/mkdocs-minify-plugin)**: Minifies HTML, CSS, and JavaScript for faster loading
- **[mkdocs-rss-plugin](https://github.com/Guts/mkdocs-rss-plugin)**: Generates RSS feeds automatically
- **[mkdocs-git-revision-date-localized-plugin](https://github.com/timvink/mkdocs-git-revision-date-localized-plugin)**: Shows last modification dates
- **[mkdocs-htmlproofer-plugin](https://github.com/manuzhang/mkdocs-htmlproofer-plugin)**: Validates links and HTML structure

Additional useful plugins to consider:

- **[mkdocs-redirects](https://github.com/datarobot/mkdocs-redirects)**: `pip install mkdocs-redirects`
- **[mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin)**: Enhanced navigation control

## Performance Optimizations

This website includes several performance optimizations:

### Image Optimization

- **Automated WebP conversion**: All JPG/PNG images are automatically converted to WebP format during build
- **55.2% size reduction**: From 76MB to 34MB total image size
- **Smart processing**: Only new images are converted, existing optimized images are preserved
- **Format preservation**: Animated GIFs preserved for animation, SVG files converted but originals kept

### Build Optimizations

- **Docker multi-stage builds**: Efficient caching and smaller final images
- **Gzip & Brotli compression**: Enhanced compression in nginx
- **HTTP/2 support**: Server push for critical resources
- **Progressive Web App**: Service worker for offline functionality
- **Build caching**: Faster subsequent builds

### Security Features

- **Content Security Policy**: Comprehensive CSP implementation
- **Security headers**: HSTS, X-Frame-Options, and more
- **SSL/TLS support**: Automated certificate management with Let's Encrypt

## Static Website Hosting Services

This website is hosted/built using the following services:

| Service                                                  | Direct Link                                                     | 0xfab1 CNAME                      |
|----------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------|
| [GitHub Pages](https://pages.github.com/)                | [0xfab1@github](https://fullbyte.github.io)                     | <https://www.0xfab1.net/>         |
| [IPFS](https://ipfs.io/) with [fleek](https://fleek.co/) | [0xfab1@IFPS](http://fb62c5359b88d00d5924.b-cdn.net)            | <https://ipfs.0xfab1.net/>        |
| [Netlify](https://www.netlify.com/)                      | [0xfab1@netlify](https://0xfab1.netlify.app/)                   | <https://netlify.0xfab1.net>      |
| [Azure](https://azure.microsoft.com)                     | Broke (my fault)... need to re-create this                      | <https://azure.0xfab1.net>        |
| [Digital Ocean](https://m.do.co/c/0ef5c6b3f680)          | [0xfab1@digitalocean](https://oxfab1-3l4ou.ondigitalocean.app/) | <https://digitalocean.0xfab1.net> |
| [Vercel](https://vercel.com/)                            | [0xfab1@vercel](https://0xfab1.vercel.app/)                     | <https://vercel.0xfab1.net/>      |
| [cloudflare](https://www.cloudflare.com/)                | [0xfab1@cloudflare](https://fullbyte-github-io.pages.dev)       | <https://cloudflare.0xfab1.net/>  |
| [Render](https://render.com/)                            | [0xfab1@render](https://zeroxfab1.onrender.com)                 | <https://render.0xfab1.net>       |

Services to try:

- [AWS S3](https://aws.amazon.com/s3/)
- [Gitlab Pages](https://about.gitlab.com)
- [Surge](https://surge.sh/)

I tried these services but they didn't suit me for my deployment at the time tested*:

- [Heroku](https://www.heroku.com) - php workaround breaks other builds
- [edg.io](https://edg.io/) - annoying DNS and build setup
- [Fly.io](https://fly.io/) - complicated build/requires extra files and github action changes
- [Firebase](https://console.firebase.google.com/) - complicated build/requires extra files and github action changes
- [Feta](https://www.deta.sh/) - complicated build/requires extra files and github action changes
- [Hostman](https://hostman.com) - no free option
- [Qovery](https://console.qovery.com) - looks great but didn't get it to work for simple static websites
- [Statically](https://statically.io) - great for one-pagers, not suitable for 0xfab1.net
- [Linode](https://www.linode.com) - no free option
- [koyeb](https://app.koyeb.com) - account closed for unknown reason
- [Railway](https://railway.app) - worked fine until beginning of 2023 when the pricing model changed and the basic service was no longer free

*happy to learn from you how I can use them using a simple, automated deployment method for my static website :)

## Github Pages

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

My [github action to build the static webpage using mkdocs](https://github.com/FullByte/FullByte.github.io/blob/master/.github/workflows/build-0xfab1.yml) looks as follows and includes the latest optimizations:

``` yaml
name: Build and Deploy Website

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  release:
    types: [published]
  workflow_dispatch:

jobs:
  build:
    # cancels the deployment for the automatic merge push created when tagging a release
    if: contains(github.ref, 'refs/tags') == false || github.event_name == 'release'
    name: Build and Deploy Website
    runs-on: ubuntu-latest
    steps:
      - name: Checkout main
        uses: actions/checkout@v2

      - name: Set up Python 3.10
        uses: actions/setup-python@v2
        with:
          python-version: '3.10'

      - name: Install mkdocs dependencies
        run: |
          pip install --upgrade pip          
          pip install mkdocs-material
          pip install mkdocs-minify-plugin
          pip install mkdocs-rss-plugin
          pip install mkdocs-git-revision-date-localized-plugin
          pip install mkdocs-htmlproofer-plugin
          pip install pillow
          pip install cairosvg

      - name: Optimize images
        run: |
          python image_optimizer.py --mode build

      - name: Deploy Github Pages
        env:
          PYTHONWARNINGS: ignore
        run: |
          git pull
          mkdocs gh-deploy --no-history 2>&1 | grep -v '\[git-revision-date-localized-plugin\]' | grep -v 'has no git logs' | grep -v 'First revision timestamp' | grep -v 'RSS-plugin.*Dates could not be retrieved' || true
```

There are many other nice things that could be done here. The main important part is to trigger the markdown to static website generator as github action on new commits so that the site is automatically built whenever you commit new content.

## Build Tools

This website includes several automated build tools for enhanced development experience:

### Local Development Scripts

**Python Build Script (`build.py`)**
```bash
# Quick build with optimization
python build.py

# Build and start development server
python build.py --serve

# Skip image optimization (faster builds during development)
python build.py --no-optimize

# Clean build
python build.py --clean
```

**PowerShell Build Script (`build.ps1`)**
```powershell
# Quick build with optimization
.\build.ps1

# Build and serve on custom port
.\build.ps1 -Serve -Port 3000

# Skip optimization for faster development
.\build.ps1 -NoOptimize
```

### Image Optimization Tool

The `image_optimizer.py` script provides comprehensive image optimization:

```bash
# Automatic optimization during build
python image_optimizer.py --mode build

# Show current image inventory
python image_optimizer.py --inventory

# Manual optimization with clean references
python image_optimizer.py --mode all --clean-references
```

**Features:**
- Converts JPG/PNG to WebP automatically
- Updates markdown references to use WebP
- Preserves animated GIFs
- Handles SVG conversion with fallbacks
- 55.2% size reduction achieved

## Current Statistics

### Performance Metrics
- **Total WebP Images**: 544 optimized images
- **Size Reduction**: 55.2% (76MB → 34MB)
- **Build Time**: ~200 seconds (with full optimization)
- **Preserved Files**: 8 animated GIFs maintained for functionality

### Technology Stack
- **Static Site Generator**: MkDocs with Material theme
- **Image Optimization**: Automated WebP conversion pipeline
- **Compression**: Gzip/Brotli support
- **PWA Features**: Service worker, offline functionality
- **Security**: CSP headers, HSTS, secure defaults
- **CI/CD**: GitHub Actions with automated deployment
- **Hosting**: Multi-platform deployment (GitHub Pages, Netlify, Vercel, etc.)

The website is fully optimized for performance, accessibility, and maintainability with automated workflows for content updates and image optimization.
