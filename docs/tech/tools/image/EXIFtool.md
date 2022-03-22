# EXIFtool

Info

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Examples

Remove EXIF data except orientation information

``` sh
exiftool "-overwrite_original" "-all:all=" "-tagsfromfile" "@" "-exif:Orientation" "file.jpg"
```
