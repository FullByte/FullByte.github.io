# EXIFtool

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

## Usage

Remove EXIF data except orientation information

```shell
exiftool "-overwrite_original" "-all:all=" "-tagsfromfile" "@" "-exif:Orientation" "file.jpg"
```
