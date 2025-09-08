#!/bin/sh

# Create dummy certificate if it doesn't exist
if [ ! -f /etc/letsencrypt/live/0xfab1.net/fullchain.pem ]; then
    echo "Creating dummy certificate for 0xfab1.net"
    mkdir -p /etc/letsencrypt/live/0xfab1.net
    openssl req -x509 -nodes -newkey rsa:2048 -days 1 \
        -keyout "/etc/letsencrypt/live/0xfab1.net/privkey.pem" \
        -out "/etc/letsencrypt/live/0xfab1.net/fullchain.pem" \
        -subj "/CN=0xfab1.net"
fi

# Start nginx
nginx -g "daemon off;" &
sleep 8

# Get Cert
certbot --nginx --non-interactive --agree-tos --email admin@0xfab1.net -d 0xfab1.net

# Renew certificates every 12 hours
while :; do
    certbot renew --nginx
    sleep 12h
done