# Docker Containers

A list of docker containers

## Tutorials

- <https://www.ezzeddinabdullah.com/posts/how-to-clean-text-data-at-the-command-line>

## I2P

Sources:

- <https://geti2p.net/de/download>
- <https://hub.docker.com/r/meeh/i2p.i2p/>

```shell
docker pull meeh/i2p.i2p
```

## Drawio

Sources:

- <https://github.com/fjudith/docker-draw.io>

```shell
docker run -it --rm --name="draw" -p 8080:8080 -p 8443:8443 fjudith/draw.io
```

## NoteCalc

Sources:

- <https://github.com/bbodi/notecalc3>

```shell
git clone https://github.com/bbodi/notecalc3.git
cd notecalc3
docker build . --tag notecalc3
docker run --rm -d -p 5000:5000 notecalc3
```
