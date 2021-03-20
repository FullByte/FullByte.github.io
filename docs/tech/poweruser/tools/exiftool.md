# EXIFtool

Remove EXIF data except orientation information

```shell
exiftool "-overwrite_original" "-all:all=" "-tagsfromfile" "@" "-exif:Orientation" "file.jpg"
```
