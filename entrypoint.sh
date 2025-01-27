#!/bin/sh

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