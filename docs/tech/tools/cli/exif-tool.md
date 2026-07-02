---
date: 2023-12-22
modified: 2024-05-29
description: Remove EXIF data except orientation information
tags:
- Tech
- Tools
---

# EXIFtool

| What          | Where                                  |
| ------------- | -------------------------------------- |
| Official Page | <https://exiftool.org>                 |
| Source        | <https://github.com/exiftool/exiftool> |
| Download      | <https://exiftool.org/#running>        |
| Windows       | `choco install exiftool`                 |

## Examples

Remove EXIF data except orientation information

``` sh
exiftool -overwrite_original -all:all= -tagsfromfile @ -exif:Orientation file.jpg
```

Remove all EXIF data

``` sh
exiftool -overwrite_original_in_place -all= file.jpg
```
