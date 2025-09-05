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
VOLUME /var/www/certbot

ENTRYPOINT ["/entrypoint.sh"]