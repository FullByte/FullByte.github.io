# yt-dlp

Youtube-dl is a command-line program to download videos from YouTube and other video sites. yt-dlp is a youtube-dl fork. Some examples on how to use youtube-dl or yt-dlp to download videos.  In most cases commands for youtube-dl are the same as for yt-dlp. IN case of issues e.g. with "-F" output to give format selection create `yt-dlp.conf` in the same dir as yt-dlp and write `--list-formats-old` in it. If the command line is not appealing to you, try [youtube-dl-gui](https://github.com/oleksis/youtube-dl-gui) which is a cross platform front-end GUI for youtube-dl.

| What    | Where                              |
|---------|------------------------------------|
| Source  | <https://github.com/yt-dlp/yt-dlp> |
| Windows | `choco install yt-dlp`             |
| Linux   | `apt install yt-dlp`          |
| Python  | `pip install yt-dlp`               |

Update

- native: ```yt-dlp -U```
- pip: ```pip install yt-dlp --upgrade```

## Download Video

Get Source formats available:

``` sh
yt-dlp --list-formats 'link'
```

Download as MP4

``` sh
yt-dlp -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" 'link'
```

Download to a specific location in best quality:

``` sh
yt-dlp -f 22 -o 'path' 'link'
```

Download with details:

``` sh
yt-dlp -f best --write-description --write-info-json --write-annotations --write-sub --write-thumbnail 'link'
```

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
yt-dlp --batch-file download.txt -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "${line}"
```

## Download audio only

``` sh
yt-dlp -i --extract-audio --audio-format mp3 --audio-quality 0 'link'
```

This script will download the latest yt-dlp version for windows to the current folder if not available.

``` ps1
Function ytdlpl
{
    Param ($playlist)
    # Download and rename playlist
    yt-dlp -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -i --extract-audio --audio-format mp3 --audio-quality 2 --yes-playlist "$playlist"
    Set-Location -Path ((Get-Location).Path + "\" + (Get-ChildItem | Sort-Object LastWriteTime | Select-Object -last 1).Name)
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '[^a-zA-Z]', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '\s+', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.Name -replace ' .mp3', '.mp3')}
}
```

## Download Playlists

Download a playlist:

``` sh
yt-dlp -best 22 --yes-playlist 'link'
```

Download a playlist with audio only:

``` sh
yt-dlp -f 22 --yes-playlist 'link'
```

## Download Subtitles

Check available subs:

``` sh
yt-dlp --list-subs 'link'
```

Download auto generated subs:

``` sh
yt-dlp --sub-langs "de" --write-auto-subs --skip-download --convert-subs srt -o "youtube-text.%(ext)s" 'link'
```

Download subs in german. Change `--sub-langs "de"` for other languages:

``` sh
yt-dlp --sub-langs "de" --write-subs --skip-download --convert-subs srt -o "youtube-text.%(ext)s" 'link'
```

Remove everything aside from text and remove double lines for better analysis (e.g. for ChatGPT)

Linux:

```sh
sed -E '/^[0-9]+$/d; /^[[:space:]]*$/d; /-->/d;' "youtube-text.srt" | awk '!seen[$0]++' | sed -E 's/\[.*?\]//g' | tr '\n' ' '  | sed -E 's/[[:space:]]+/ /g' > youtube-text_done.txt
```

Windows:

```ps1
$filtered = Get-Content .\youtube-text.de.srt | Where-Object { $_ -notmatch '^[0-9]+$' -and $_ -notmatch '^$' -and $_ -notmatch '-->' } | Where-Object { $_.Trim() -ne "" } | Get-Unique | ForEach-Object { $_ -replace '\[.*?\]', '' }
($filtered -join " " -replace '\s+', ' ') | Set-Content .\youtube-text_clean.txt
```
