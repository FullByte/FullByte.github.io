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

- PNG to PDF: ```convert prefix-*.png FINAL.pdf```

## GIF

Use ImageMagick to optimize a GIF

``` sh
convert -layers Optimize input.gif output.gif
```

## Resize

``` sh
convert file.jpg -resize 1024 × 768 "folder\file.jpg"
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
