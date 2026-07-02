---
date: 2024-01-08
modified: 2024-05-29
description: Stream to chromecast with yt-dlp and vlc
tags:
- Tech
- Tools
---

# VLC

Stream to chromecast with yt-dlp and vlc

```sh
yt-dlp "https://stream.example" -o - | cvlc --sout "#chromecast" --sout-chromecast-ip="10.20.30.40" -
```
