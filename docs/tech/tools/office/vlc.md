# VLC

Stream to chromecast with yt-dlp and vlc

```sh
yt-dlp "https://stream.example" -o - | cvlc --sout "#chromecast" --sout-chromecast-ip="10.20.30.40" -
```
