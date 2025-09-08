FROM python:3-slim AS builder

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

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
    PYTHONWARNINGS=ignore mkdocs build --quiet

FROM nginx:alpine
RUN apk add --no-cache nginx nginx-mod-http-brotli certbot certbot-nginx openssl

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

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost/ || exit 1
VOLUME /var/www/certbot

ENTRYPOINT ["/entrypoint.sh"]