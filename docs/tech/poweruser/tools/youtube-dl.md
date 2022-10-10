# youtube-dl

Some examples on how to use youtube-dl or ytdlpl to download videos.

| What          | Where                                             |
|---------------|---------------------------------------------------|
| Official Page | <https://youtube-dl.org/>                         |
| Source        | <https://github.com/ytdl-org/youtube-dl>          |
| Download      | <https://github.com/ytdl-org/youtube-dl/releases> |
| Install       | choco install youtube-dl                          |

As an alternative it is possible to swap youtube-dl with [yt-dlp](https://github.com/yt-dlp/yt-dlp). This should simply work in most cases. IN case of issues e.g. with "-F" output to give format selection create `yt-dlp.conf` in the same dir as yt-dlp and write `--list-formats-old` in it.

If the commandline is not appealing to you, try [youtube-dl-gui](https://github.com/oleksis/youtube-dl-gui) which is a cross platform front-end GUI for youtube-dl.

## Download Video

Download to a specific location in best quality:

``` sh
youtube-dl -f 22 -o 'path' '<youtube-link>'
```

Download with details:

``` sh
youtube-dl -f best --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '<youtube-link>'
```

## Audio only

``` sh
youtube-dl -i --extract-audio --audio-format mp3 --audio-quality 0 '<youtube-link>'
```

## YouTube Playlists

Download a playlist:

``` sh
youtube-dl -best 22 --yes-playlist '<playlist-link'
```

Download a playlist with audio only:

``` sh
youtube-dl -f 22 --yes-playlist '<playlist-link'
```

## Get Video Source Information

Get Source formats available:

``` sh
youtube-dl --list-formats '<youtube-link>'
```

## Download audio of a playlist

Run ytdlpl (youtube downloader playlist) and add the playlist you want to download.
This script will download the latest youtube-dl version for windows to the current folder if not available.

``` ps1
Function ytdlpl
{
    Param ($playlist)

    # Check and get youtube-dl if required
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = ‘stop’
    try {if(Get-Command youtube-dl){Write-Host("Using youtube-dl version " + (Get-Command youtube-dl).Version + " from source: " + (Get-Command youtube-dl).Source)}}
    catch {Write-Host "youtube-dl not found, downloading to current folder... "; Invoke-WebRequest -Uri "https://youtube-dl.org/downloads/latest/youtube-dl.exe" -OutFile ((Get-Location).Path + "\youtube-dl.exe")}
    $ErrorActionPreference=$oldPreference

    # Download and rename playlist
    youtube-dl.exe -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -i --extract-audio --audio-format mp3 --audio-quality 2 --yes-playlist "$playlist"
    Set-Location -Path ((Get-Location).Path + "\" + (Get-ChildItem | Sort-Object LastWriteTime | Select-Object -last 1).Name)
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '[^a-zA-Z]', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '\s+', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.Name -replace ' .mp3', '.mp3')}
}
```

Alternatively use this script

``` ps1
iex ((New-Object System.Net.WebClient).DownloadString('https://raw.githubusercontent.com/FullByte/scripts/main/powershell/youtubedl/youtube-dl.ps1'))
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

To donwload all videos and playlists listed in `download.txt` we can now run the follwing command. This will also put all playlist videos in an own subfolder:

``` sh
ytdl --batch-file download.txt -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' "${line}"
```
