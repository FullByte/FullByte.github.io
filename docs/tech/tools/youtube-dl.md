# youtube-dl

Examples using youtube-dl

## Info

|What|Where|
|-|-|
|Official Page|<https://youtube-dl.org/>|
|Source|<https://github.com/ytdl-org/youtube-dl>|
|Download|<https://github.com/ytdl-org/youtube-dl/releases>|
|Install|choco install youtube-dl|

## YouTube video download

Download to a specific location in best quality:

```shell
youtube-dl -f 22 -o 'path' '<youtube-link>'
```

Download with details:

```shell
youtube-dl -f best --write-description --write-info-json --write-annotations --write-sub --write-thumbnail '<youtube-link>'
```

## Audio only

```shell
youtube-dl -i --extract-audio --audio-format mp3 --audio-quality 0 '<youtube-link>'
```

## YouTube Playlists

Download a playlist:

```shell
youtube-dl -best 22 --yes-playlist '<playlist-link'
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

## Script to download audio of playlist

Run ytdlpl (youtube downloader playlist) and add the playlist you want to download.
This script will download the latest youtube-dl version for windows to the current folder if not available.

```powershell
Function ytdlpl
{
    Param ($playlist)

    # Check and get youtube-dl if required
    $oldPreference = $ErrorActionPreference
    $ErrorActionPreference = ‘stop’
    try {if(Get-Command youtube-dl){Write-Host("Using youtube-dl version " + (Get-Command youtube-dl).Version + " from source: " + (Get-Command youtube-dl).Source)}}
    catch {Write-Host “youtube-dl not found, downloading to current folder... ”; Invoke-WebRequest -Uri "https://youtube-dl.org/downloads/latest/youtube-dl.exe" -OutFile ((Get-Location).Path + "\youtube-dl.exe")}
    $ErrorActionPreference=$oldPreference

    # Download and rename playlist
    youtube-dl.exe -o '%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s' -i --extract-audio --audio-format mp3 --audio-quality 2 --yes-playlist "$playlist"
    Set-Location -Path ((Get-Location).Path + "\" + (Get-ChildItem | Sort-Object LastWriteTime | Select-Object -last 1).Name)
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '[^a-zA-Z]', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.BaseName -replace '\s+', ' ') + '.mp3' }
    Get-ChildItem | Rename-Item -NewName { ($_.Name -replace ' .mp3', '.mp3')}
}
```
