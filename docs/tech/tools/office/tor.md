# Tor

Tor, short for The Onion Router, is a free, open-source software designed to enable anonymous communication on the internet. The main goal of Tor is to protect users' privacy and provide them with the ability to browse the internet without being tracked or monitored. It does this by routing internet traffic through a series of volunteer-operated servers called nodes, which are distributed worldwide.

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## snowflake-proxy

Run snowflake-proxy as container

```sh
docker-compose up -d snowflake-proxy
```

docker-compose file:

```yaml
version: "3.8"

services:
    snowflake-proxy:
        image: thetorproject/snowflake-proxy:latest
        network_mode: host
        container_name: snowflake-proxy
        pull_policy: always
        restart: unless-stopped
        command: ["-verbose", "-unsafe-logging", "-summary-interval", "1m"]
```
