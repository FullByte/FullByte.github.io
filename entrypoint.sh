#!/bin/sh
set -e

DOMAIN="${DOMAIN:-}"
EMAIL="${EMAIL:-admin@${DOMAIN}}"
ENABLE_SSL="${ENABLE_SSL:-false}"

# ---------------------------------------------------------------------------
# SSL mode: obtain/renew Let's Encrypt certificates for the given DOMAIN.
# Usage:  docker run -e ENABLE_SSL=true -e DOMAIN=example.com -p 80:80 -p 443:443 ...
# ---------------------------------------------------------------------------
if [ "$ENABLE_SSL" = "true" ] && [ -n "$DOMAIN" ]; then
    echo "SSL mode enabled for ${DOMAIN}"

    # Generate a temporary self-signed cert so nginx can start with SSL
    if [ ! -f "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" ]; then
        echo "Creating temporary self-signed certificate for ${DOMAIN}"
        mkdir -p "/etc/letsencrypt/live/${DOMAIN}"
        openssl req -x509 -nodes -newkey rsa:2048 -days 1 \
            -keyout "/etc/letsencrypt/live/${DOMAIN}/privkey.pem" \
            -out "/etc/letsencrypt/live/${DOMAIN}/fullchain.pem" \
            -subj "/CN=${DOMAIN}" 2>/dev/null
    fi

    # Write an HTTPS server block for this domain
    cat > /etc/nginx/conf.d/ssl.conf <<EOF
server {
    listen 443 ssl http2;
    server_name ${DOMAIN} www.${DOMAIN};

    ssl_certificate     /etc/letsencrypt/live/${DOMAIN}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/${DOMAIN}/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-RSA-AES256-GCM-SHA512:DHE-RSA-AES256-GCM-SHA512:ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-GCM-SHA384;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 10m;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Frame-Options DENY always;
    add_header X-Content-Type-Options nosniff always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    root /usr/share/nginx/html;
    index index.html index.htm;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location = /favicon.ico { log_not_found off; access_log off; }
    location = /robots.txt  { log_not_found off; access_log off; }

    location ~* \.(css|js|png|jpg|jpeg|gif|ico|svg|webp|woff2?)$ {
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
EOF

    # Start nginx in background, then request a real certificate
    nginx -g "daemon off;" &
    NGINX_PID=$!
    sleep 5

    certbot --nginx --non-interactive --agree-tos --email "${EMAIL}" -d "${DOMAIN}" || true

    # Renew certificates every 12 hours
    while :; do
        certbot renew --nginx --quiet || true
        sleep 12h
    done &

    wait $NGINX_PID

# ---------------------------------------------------------------------------
# HTTP-only mode (default): just serve on port 80 — works anywhere.
# Usage:  docker run -p 8080:80 image_name
# ---------------------------------------------------------------------------
else
    echo "Starting in HTTP-only mode on port 80"
    echo "Tip: Set ENABLE_SSL=true and DOMAIN=yourdomain.com for HTTPS"
    exec nginx -g "daemon off;"
fi