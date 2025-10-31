# 0xfab1.net

[![Header](header.svg)](https://0xfab1.net)

Personal website built with MkDocs Material. Contributions welcome!

## Quick Start

**Run with Docker:**

```bash
docker run -it --rm -p 8000:8000 0xfab1/0xfab1.net serve -a 0.0.0.0:8000
```

**Local development:**

```bash
git clone https://github.com/FullByte/FullByte.github.io.git
cd FullByte.github.io
pip install -r requirements.txt
python site_manager.py serve
```

## Site Manager

The `site_manager.py` script provides unified site management:

```bash
# Build the site with image optimization
python site_manager.py build

# Start development server
python site_manager.py serve

# Optimize images (converts JPG/PNG to WebP, excludes SVG)
python site_manager.py optimize

# Generate site statistics
python site_manager.py stats --export json

# Test built site for issues
python site_manager.py test

# Check media file paths
python site_manager.py check

# Clean build artifacts
python site_manager.py clean
```

## Docker

Build and run with HTTPS support:

```bash
# Development
docker build -t site .
docker run -p 8000:8000 site

# Production with SSL
docker run -p 80:80 -p 443:443 \
  -v /path/to/certs:/etc/nginx/ssl \
  site
```

## Contributing

1. Fork this repository
2. Make your changes
3. Test with `python site_manager.py build`
4. Submit a pull request

## Contact

- ![Mastodon](https://img.shields.io/mastodon/follow/109640942794566265?domain=https%3A%2F%2Fsocial.lol&style=social)
- [![Twitter](https://img.shields.io/badge/twitter-%40zerogdoubled-%231da1f2)](https://twitter.com/zerogdoubled)

![qrcode](0xfab1-qrcode.png)
