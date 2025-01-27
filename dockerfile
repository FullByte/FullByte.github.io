FROM python:3-slim AS builder

RUN adduser --disabled-password mkdocs
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir mkdocs mkdocs-material mkdocs-minify-plugin

WORKDIR /site
COPY docs ./docs
COPY overrides ./overrides
COPY mkdocs.yml .

RUN mkdocs build

FROM nginx:alpine
RUN apk add --no-cache certbot certbot-nginx

# Create directories for Let's Encrypt
RUN mkdir -p /etc/letsencrypt /var/lib/letsencrypt /var/www/certbot

COPY --from=builder /site/site /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
COPY entrypoint.sh /entrypoint.sh

# Make entrypoint executable
RUN chmod +x /entrypoint.sh

EXPOSE 80
EXPOSE 443

VOLUME /etc/letsencrypt
VOLUME /var/lib/letsencrypt
VOLUME /var/www/certbot

ENTRYPOINT ["/entrypoint.sh"]