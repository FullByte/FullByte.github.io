# Docker

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

## Getting started

TODO

## Useful Commands

TODO

## Cool things to run with docker

A list of docker containers

### Tutorials

- <https://www.ezzeddinabdullah.com/posts/how-to-clean-text-data-at-the-command-line>

### I2P

Sources:

- <https://geti2p.net/de/download>
- <https://hub.docker.com/r/meeh/i2p.i2p/>

```shell
docker pull meeh/i2p.i2p
```

### Drawio

Sources:

- <https://github.com/fjudith/docker-draw.io>

```shell
docker run -it --rm --name="draw" -p 8080:8080 -p 8443:8443 fjudith/draw.io
```

### NoteCalc

Sources:

- <https://github.com/bbodi/notecalc3>

```shell
git clone https://github.com/bbodi/notecalc3.git
cd notecalc3
docker build . --tag notecalc3
docker run --rm -d -p 5000:5000 notecalc3
```

### Archive Box

Sources:

- <https://github.com/ArchiveBox/ArchiveBox>
- <https://github.com/ArchiveBox/ArchiveBox/wiki/Docker>
- <https://nixintel.info/osint-tools/make-your-own-internet-archive-with-archive-box/>

```shell
docker run -v $PWD:/data archivebox/archivebox init
docker run -v $PWD:/data archivebox/archivebox add 'https://0xfab1.net'
docker run -v $PWD:/data -it archivebox/archivebox manage createsuperuser
docker run -v $PWD:/data -p 8000:8000 archivebox/archivebox server 0.0.0.0:8000
```

### Wireguard

Sources:

- <https://github.com/linuxserver/docker-wireguard>

```shell
docker pull ghcr.io/linuxserver/wireguard
```

### IPFS

Sources:

- <https://registry.hub.docker.com/r/ipfs/go-ipfs>
- <https://github.com/ipfs/go-ipfs>

```shell
docker pull ipfs/go-ipfs
docker run -d --name ipfs_host -v $ipfs_staging:/export -v $ipfs_data:/data/ipfs -p 4001:4001 -p 127.0.0.1:8080:8080 -p 127.0.0.1:5001:5001 ipfs/go-ipfs:latest
docker exec ipfs_host ipfs swarm peers
docker logs -f ipfs_host
```

### Matrix Synapse

Sources:

- <https://registry.hub.docker.com/r/matrixdotorg/synapse/>

```shell
docker pull matrixdotorg/synapse
docker run -it --rm --mount type=volume,src=synapse-data,dst=/data -e SYNAPSE_SERVER_NAME=my.matrix.host -e SYNAPSE_REPORT_STATS=yes matrixdotorg/synapse:latest generate
```

### Jellyfin

Sources:

- <https://github.com/jellyfin/jellyfin>
- <https://jellyfin.org/>

```bash
docker pull jellyfin/jellyfin:latest
mkdir -p /srv/jellyfin/{config,cache}
docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media:/media --net=host jellyfin/jellyfin:latest
```
