# Build

**Quick Development Setup:**

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git # clone repo
cd FullByte.github.io # Go to main folder
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material # run the container
```

**Production Deployment:**

``` sh
git clone https://github.com/FullByte/FullByte.github.io.git
cd FullByte.github.io
docker build -t 0xfab1-site .
docker run -d -p 80:80 -p 443:443 -v letsencrypt:/etc/letsencrypt 0xfab1-site
```

## MkDocs

To honor [this post](https://rakhim.org/images/honestly-undefined/blogging.jpg) (and ensure the message remains true) I will use my own website as an example and show how I configured the static web app and make it work the way it does.

I am using [Github Pages](https://pages.github.com/) to host the content, [Mkdocs](https://www.mkdocs.org/) to create the website from markdown files as input and have my own [domain](https://0xfab1.net/) for a nicer URL.

[MkDocs](https://github.com/MkDocs/MkDocs/) is a great way to host a simple, static website. This website uses [Material for MkDocs](https://github.com/squidfunk/MkDocs-material) which is a theme for MkDocs.

To quickly create and host a static website (or rebuild this website), you have two options:

- Docker
- Python

### Modify pages

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

### Performance Optimizations

This website includes several performance optimizations:

#### Image Optimization

- **Automated WebP conversion**: All JPG/PNG images are automatically converted to WebP format during build
- **55.2% size reduction**: From 76MB to 34MB total image size
- **Smart processing**: Only new images are converted, existing optimized images are preserved
- **Format preservation**: Animated GIFs preserved for animation, SVG files converted but originals kept

#### Build Optimizations

- **Docker multi-stage builds**: Efficient caching and smaller final images
- **Gzip & Brotli compression**: Enhanced compression in nginx
- **HTTP/2 support**: Server push for critical resources
- **Progressive Web App**: Service worker for offline functionality
- **Build caching**: Faster subsequent builds

#### Security Features

- **Content Security Policy**: Comprehensive CSP implementation
- **Security headers**: HSTS, X-Frame-Options, and more
- **SSL/TLS support**: Automated certificate management with Let's Encrypt

## Docker

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

Current Dockerfile (Production-Ready with SSL/TLS Support)

``` dockerfile
FROM python:3-slim AS builder

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN adduser --disabled-password --gecos "" mkdocs

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir mkdocs mkdocs-material mkdocs-minify-plugin mkdocs-rss-plugin mkdocs-git-revision-date-localized-plugin mkdocs-htmlproofer-plugin pillow cairosvg

WORKDIR /site

# Copy files in order of change frequency (least to most)
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY mkdocs.yml .
COPY overrides ./overrides
COPY site_manager.py .
COPY pre_build_hook.py .
COPY docs ./docs

# Build (site_manager handles image optimization then mkdocs build)
RUN python site_manager.py build --quiet

FROM nginx:alpine
RUN apk add --no-cache certbot certbot-nginx openssl curl

# Create directories for Let's Encrypt
RUN mkdir -p /etc/letsencrypt /var/lib/letsencrypt /var/www/certbot

COPY --from=builder /site/site /usr/share/nginx/html
RUN chown -R nginx:nginx /usr/share/nginx/html && \
    chown -R nginx:nginx /var/www/certbot

COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh

# Make entrypoint executable
RUN chmod +x /entrypoint.sh

EXPOSE 80
EXPOSE 443

VOLUME /etc/letsencrypt
VOLUME /var/lib/letsencrypt
VOLUME /var/www/certbot

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1

ENTRYPOINT ["/entrypoint.sh"]
```

## Python

Run this once to install all requirements:

``` sh
choco install -y python
python -m pip install --upgrade pip
pip install -r requirements.txt
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

# Manual image optimization (use site_manager)
# - Full build (includes image optimization):
python site_manager.py build
# - Only optimize images (convert, update refs, cleanup):
python site_manager.py optimize --mode all
```
