FROM python:3-slim AS builder

RUN adduser --disabled-password mkdocs
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir mkdocs mkdocs-material mkdocs-minify-plugin

WORKDIR /site
COPY docs ./docs
COPY overrides ./overrides
COPY mkdocs.yml .

RUN mkdocs build

FROM docker.io/nginx:alpine
RUN apk add --no-cache openssl && \
    mkdir -p /etc/ssl/private && \
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/nginx-selfsigned.key \
    -out /etc/ssl/certs/nginx-selfsigned.crt \
    -subj "/C=DE/ST=NS/L=Home/O=0xfab1/OU=website/CN=localhost"
COPY --from=builder /site/site /usr/share/nginx/html
COPY nginx.conf /etc/nginx/nginx.conf
EXPOSE 8443
CMD ["nginx", "-g", "daemon off;"]
