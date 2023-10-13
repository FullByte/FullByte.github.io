# yt-dlp

Youtube-dl is a command-line program to download videos from YouTube and other video sites. yt-dlp is a youtube-dl fork. Some examples on how to use youtube-dl or ytdlpl to download videos.  In most cases commands for youtube-dl are the same as for yt-dlp. IN case of issues e.g. with "-F" output to give format selection create `yt-dlp.conf` in the same dir as yt-dlp and write `--list-formats-old` in it. If the command line is not appealing to you, try [youtube-dl-gui](https://github.com/oleksis/youtube-dl-gui) which is a cross platform front-end GUI for youtube-dl.

| What    | Where                              |
|---------|------------------------------------|
| Source  | <https://github.com/yt-dlp/yt-dlp> |
| Install | `choco install yt-dlp`             |

## Download Video

Download to a specific location in best quality:

``` sh
yt-dlp.exe -f 22 -o 'path' '<youtube-link>'
```

Download with details:

``` sh
yt-dlp.exe -f best --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '<youtube-link>'
```

## Audio only

``` sh
yt-dlp.exe -i --extract-audio --audio-format mp3 --audio-quality 0 '<youtube-link>'
```

## YouTube Playlists

Download a playlist:

``` sh
yt-dlp.exe -best 22 --yes-playlist '<playlist-link'
```

Download a playlist with audio only:

``` sh
yt-dlp.exe -f 22 --yes-playlist '<playlist-link'
```

## Get Video Source Information

Get Source formats available:

``` sh
yt-dlp.exe --list-formats '<youtube-link>'
```

## Download audio of a playlist

This script will download the latest yt-dlp.exe version for windows to the current folder if not available.

``` ps1
Function ytdlpl
{
    Param ($playlist)
    # Download and rename playlist
    yt-dlp.exe -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -i --extract-audio --audio-format mp3 --audio-quality 2 --yes-playlist "$playlist"
    Set-Location -Path ((Get-Location).Path + "\" + (Get-ChildItem | Sort-Object LastWriteTime | Select-Object -last 1).Name)
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '[^a-zA-Z]', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '\s+', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.Name -replace ' .mp3', '.mp3')}
}
```

## Download all videos of a list

To download all videos mentioned on a given website use the following regex to find youtube links:

Regex for videos: `youtube\.com\/watch\?v=[A-Za-z0-9-_]{11}`
Regex for playlists: `youtube\.com\/playlist\?list=[A-Za-z0-9_-]{34}`

We can now curl the given page (example here is <https://cs1000.vercel.app>) and append all found links to `download.txt`

``` sh
curl -s https://cs1000.vercel.app | grep -ioE "youtube\.com\/watch\?v=[A-Za-z0-9]{11}" > download.txt
curl -s https://cs1000.vercel.app | grep -ioE "youtube\.com\/playlist\?list=[A-Za-z0-9_-]{34}" >> download.txt
```

To download all videos and playlists listed in `download.txt` we can now run the following command. This will also put all playlist videos in an own subfolder:

``` sh
yt-dlp.exe --batch-file download.txt -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "${line}"
```
