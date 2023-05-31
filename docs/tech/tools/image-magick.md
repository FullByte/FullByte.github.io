# ImageMagick

Info

| What          | Where                                                                              |
|---------------|------------------------------------------------------------------------------------|
| Official Page | <https://imagemagick.org>                                                          |
| Source        | <https://github.com/imagemagick/imagemagick>                                       |
| Download      | <https://imagemagick.org/script/download.php>                                      |
| Install       | `sudo apt install imagemagick` or `choco install imagemagick`                      |
| Examples      | <https://imagemagick.org/script/examples.php> or <https://imagemagick.org/script/> |

## Simple Convert

Convert some PNGs into a PDF:

``` sh
convert prefix-*.png FINAL.pdf
```

Convert all images in a folder from heic to jpg

``` sh
magick mogrify -format jpg *.heic
```

## GIF

Use ImageMagick to optimize a GIF

``` sh
convert -layers Optimize input.gif output.gif
```

## Resize

Resize image to given dimensions

``` sh
convert file.jpg -resize 1024 × 768 "folder\file.jpg"
```

Create a square thumbnail or favicon using ImageMagick

``` sh
convert file.png -background transparent -gravity Center -extent 1:1# -scale 32 file-32px.png
```

## Diff Images

Using ImageMagick with git ([Source](https://github.com/niedzielski/git-diff-img)) to see differences in images:

Set alias "diff-img"

``` sh
git config --global alias.diff-img difftool\ -x\ \''compare -alpha copy "$LOCAL" "$REMOTE" png:- | montage -mode concatenate "$LOCAL" png:- "$REMOTE" png:- | display -title "$BASE: Local | Diff | Remote" png:-'\'
```

or as a script for `~/bin/git-diff-img`

``` sh
#!/usr/bin/env sh
# $@ images
exec git difftool -x '
  compare -alpha copy "$LOCAL" "$REMOTE" png:- |
  montage -mode concatenate "$LOCAL" png:- "$REMOTE" png:- |
  display -title "$BASE: Local | Diff | Remote" png:-
' "$@"
```

Execute against png images only:

``` sh
git diff-img **.png
```
