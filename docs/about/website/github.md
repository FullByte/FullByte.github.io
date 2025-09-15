# Github

All code is hosted on github.

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
