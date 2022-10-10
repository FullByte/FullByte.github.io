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
exiftool -overwrite_original -all:all= -tagsfromfile @ -exif:Orientation file.jpg
```

Remove all EXIF data

``` sh
exiftool -overwrite_original_in_place -all= file.jpg
```
