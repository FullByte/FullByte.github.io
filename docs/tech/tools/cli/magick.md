---
date: 2024-12-04
modified: 2024-12-04
description: Convert all images in a given folder from heic to jpg
tags:
- Tech
- Tools
---

# Magick

## Examples

Convert all images in a given folder from heic to jpg

``` cmd
for %i in (*.heic) do magick "%i" "%~ni.jpg"
```

``` bat
for %%i in (*.heic) do magick "%%i" "%%~ni.jpg"
```

``` ps1
Get-ChildItem -Path . -Filter *.heic | ForEach-Object {
    $jpg = $_.BaseName + ".jpg"
    $_ | Copy-Item -Destination $jpg
}
```

``` sh
for file in *.heic; do heif-convert "$file" "${file%.heic}.jpg"; done
```
