# youtube-dl

Examples using youtube-dl

## YouTube video download

Download to a specific location:

```shell
youtube-dl -o 'path' '<youtube-link>'
```

Download with details:

```shell
youtube-dl --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '<youtube-link>'
```

## YouTube Playlists

Download a playlist:

```shell
youtube-dl -i --prefer-ffmpeg --yes-playlist '<playlist-link'
```

Download a playlist with audio only:

```shell
youtube-dl -f 22 --yes-playlist '<playlist-link'
```

## Get Video Source Information

Get Source formats available:

```shell
youtube-dl --list-formats '<youtube-link>'
```
