# Convert Files

## EXIFtool

Info

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

### Usage

Remove EXIF data except orientation information

``` sh
exiftool "-overwrite_original" "-all:all=" "-tagsfromfile" "@" "-exif:Orientation" "file.jpg"
```

## Pandoc

Info

| What          | Where                 |
|---------------|-----------------------|
| Official Page | <https://pandoc.org/> |
| Source        |                       |
| Download      |                       |
| Install       |                       |

Additional tools:

- miktex for pdf conversion from LaTeX <https://miktex.org/>

### Markdown

Convert markdowns files passed as arguments into different formats and saves them into a separate folder

```cmd
set list=docx html rst odt rtf epub pdf
for %%x in (%*) do (
    mkdir output   
    mkdir output\\%%~nx
    for %%e in (%list%) do ( 
        mkdir output\\_%%e 
        pandoc %%x -o output/_%%e/%%~nx.%%e
        pandoc %%x -o output/%%~nx/%%~nx.%%e
    )
    mkdir output\\_md
    copy %%x output\_md\
    copy %%x output\%%~nx\
)
```

#### Slideshow

Slidshow using revealjs

``` sh
pandoc -s -t revealjs slides.md -o slides.html
```

Slidshow using slidy

``` sh
pandoc -s -t slidy slides.md -o slides.html
```

## FFmpeg

FFmpeg is a great tool and here are some examples.

Info

| What          | Where                                   |
|---------------|-----------------------------------------|
| Official Page | <https://ffmpeg.org/>                   |
| Source        | <https://github.com/FFmpeg/FFmpeg>      |
| Download      | <https://ffmpeg.org/download.html>      |
| Docs          | <https://ffmpeg.org/documentation.html> |
| Windows       | ```choco install ffmpeg```              |
| Linux         | ```apt install ffmpeg```                |

Helper:

- FFmpeg Command Generator <https://www.mrfdev.com/ffmpeg-command-generator>

Links:

- ffmpeg libav tutorial: <https://github.com/leandromoreira/ffmpeg-libav-tutorial>

### File Information

**Get codec details**

Get codec details of a given video file e.g. "video.mp4":

``` sh
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 video.mp4
```

**Overwrite the video title**

Change the title of input.mp4 to "My Title"

``` sh
ffmpeg -i input.mp4 -map_metadata -1 -metadata title="My Title" -c:v copy -c:a copy output.mp4
```

### Download video streams

Locate the playlist file, e.g. using Chrome > F12 > Network > Filter: m3u8
Download and concatenate the video fragments:

``` sh
ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i "playlist.m3u8" -c copy -bsf:a aac_adtstoasc output.mp4
```

### Time Lapse Helper

This example will shorten a given video to create a time lapse video. The video quality in this example will be reduced to VGA and reduce image quality. If the video is to slow/fast change the value for `thumbnail=100`.

``` sh
ffmpeg -i input.mp4 -vf "scale=vga,thumbnail=100,split[a][b],[b]palettegen=reserve_transparent=0:stats_mode=single[b];[a][b]paletteuse=new=1,settb=1/25,setpts=N" output.mp4
```

**Extract frames for timelapse**

``` sh
ffmpeg -i videoname.mp4 -vf fps=1/5 videoname%05d.jpg
```

Change the value `fps=1/5` to whatever works best (fps=1/5 = every 5 secounds one picture)

**Extract frames from a video as image file**

Extract all frames

``` sh
ffmpeg -i input.mp4 -vf -vsync 0 output%d.png
```

Extract all frames in a given timeframe e.g.: between 3 and 5 seconds as well as 55 and 60 seconds:

``` sh
ffmpeg -i input.mp4 -vf select='between(t,3,5)+between(t,55,60)' -vsync 0 output%d.png
```

Extract only one frame per second:

``` sh
ffmpeg -i in.mp4 -fps=1 -vsync 0 out%d.png
```

Extract only one frame

``` sh
ffmpeg -i input.mp4 -ss 00:00:10.000 -vframes 1 thumbnail.jpg
```

**Create Time Lapse Video using pictures**

This example will create a video based on pictures as input. In this case the files are from a GoPro so all pictures start with a "G" followed by seven digits e.g. G0011565.jpg. The starting number of the series of pictures is 11021 in my example. Change the value for "start_number", the filename prefix (in this case "G") and the length of the number (currently 7) to match your requirements.

``` sh
ffmpeg -framerate 30 -start_number 11021 -i "E:\path\G%07d.jpg" -c:v libx264 "E:\path\output.mp4"
```

### Add Subtitles

Add the subtitles to the video file (not just overlay).

Run``` sh``` to see if "--enable-libass" is listed under section "configuration:". If not you need to get libass/enable libass.

Convert the subtitles to .ass format, then use them for a video filter:

``` sh
ffmpeg -i sub.srt sub.ass
ffmpeg -i video_nosub.mp4 -vf ass=sub.ass video_withsub.mp4
```

### Manupulate Sound

**Overwrite sound with silence**

To replace all audio with silence between 30 sec and 1min and 30 sec (=90 sec):

``` sh
ffmpeg -i input.mp4 -vcodec copy -af "volume=enable='between(t,30,90)':volume=0" output.mp4
```

**Add audio file to video**

Mux video.mp4 and audio.mp4 to output.mp4. The -shortest option will cause the output duration to match the duration of the shortest input stream.

``` sh
ffmpeg -i video.mp4 -i audio.mp4 -c copy -map 0:0 -map 1:1 -shortest output.mp4
```

**Delay audio**

In this example by 3.14 seconds

``` sh
ffmpeg -i input.mp4 -itsoffset 3.14 -i in.mp4 -map 0:v -map 1:a -vcodec copy -acodec copy output.mp4
```

### Manipulate Video

**Stack Videos in a Grid**

2 Videos Horizontally

``` sh
ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex hstack=inputs=2 horizontal-stacked-output.mp4
```

2 Videos Vertically

``` sh
ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex vstack=inputs=2 vertical-stack-output.mp4
```

Videos of Different Lengths

``` sh
ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex hstack=inputs=2:shortest=1 shortest-output.mp4
```

2×2 Grid of Videos

``` sh
ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 -i input3.mp4 -filter_complex "[0:v][1:v]hstack=inputs=2[top]; [2:v][3:v]hstack=inputs=2[bottom]; [top][bottom]vstack=inputs=2[v]" -map "[v]" output.mp4
```

``` sh
ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 -i input3.mp4 -i input4.mp4 -i input5.mp4 -filter_complex "[0:v][1:v][2:v]hstack=inputs=3[top]; [3:v][4:v][5:v]hstack=inputs=3[bottom]; [top][bottom]vstack=inputs=2[v]" -map "[v]" output.mp4
```

**Trim video**

Without re-encoding:

``` sh
ffmpeg -ss [start] -i input.mp4 -t [duration] -c copy output.mp4
```

Without re-encoding:

``` sh
ffmpeg -ss [start] -i input.mp4 -t [duration] -c:v libx264 -c:a aac -strict experimental -b:a 128k output.mp4
```



**Delay audio/video**

To fix audio/video sync you can delay either video or audio:

Delay video by 3.14 seconds:

``` sh
ffmpeg -i input.mp4 -itsoffset 3.14 -i in.mp4 -map 1:v -map 0:a -vcodec copy -acodec copy output.mp4
```

**Rotate a video**

For a 90 degrees rotation use one of the following options:

0 = 90CounterCLockwise and Vertical Flip (default)
1 = 90Clockwise
2 = 90CounterClockwise
3 = 90Clockwise and Vertical Flip

``` sh
ffmpeg -i input.mp4 -vf "transpose=1" output.mp4
```

For 180 degrees run this command:

``` sh
ffmpeg -i input.mp4 -vf "transpose=2,transpose=2 output.mp4"
```

### Convert Video

To compress an avi file you can use H.264 on the output file named e.g. "input.avi" and create a smaller version of the video named "output.mkv"
More details: <https://trac.ffmpeg.org/wiki/Encode/H.264>

``` sh
ffmpeg -i input.avi -c:v libx264 -preset slow -crf 15 output.mkv
```

**Convert Video optimized for Messenger**

This works well for Whatsapp, Signal, Threema, Telegram, etc...
Make sure not to reach current allowed max files size.

With sound:

``` sh
ffmpeg -i input.mp4 -vf "scale=-2:480" -c:v libx264 -preset slow -crf 21 -profile:v baseline -level 3.0 -pix_fmt yuv420p -r 25 -g 50 -c:a aac -b:a 160k -r:a 44100 -f mp4 output.mp4
```

No sound:

``` sh
ffmpeg -i input.mp4 -an -vf "scale=vga" messenger.mp4
```

**Convert to AV1**

``` sh
# Pass 1
ffmpeg -i input.mp4 -c:v libaom-av1 -b:v 200k -filter:v scale=720:-1 -strict experimental -cpu-used 1 -tile-columns 2 -row-mt 1 -threads 8 -pass 1 -f mp4 NUL && ^
# Pass 2
ffmpeg -i input.mp4 -pix_fmt yuv420p -movflags faststart -c:v libaom-av1 -b:v 200k -filter:v scale=720:-1 -strict experimental -cpu-used 1 -tile-columns 2 -row-mt 1 -threads 8 -pass 2 output.mp4
```

**Convert from/to GIF**

From GIF to MP4

``` sh
ffmpeg -i input.gif -filter_complex "[0:v] fps=15" -vsync 0 -f mp4 -pix_fmt yuv420p output.mp4
```

or

``` sh
ffmpeg -i input.gif -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" output.mp4
```

or for many GIF in one folder:

``` ps1
Get-ChildItem -file -Path * -Include *.gif | Foreach-Object { ffmpeg -i ('"' + $_.Name + '"') -movflags faststart -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" ('"' + $_.BaseName + '.mp4"') }
```

From MP4 to GIF

``` sh
ffmpeg -i input.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```

GIF from a special section

Add e.g. "-ss 5.0 -t 3.2" to only create GIF for 3.2 secounds ot "input.mp4"

``` sh
ffmpeg -ss 5.0 -t 3.2 -i input.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```

GIF video summery

Create a short GIF from a long video

``` sh
ffmpeg -i input.mp4 -vf "scale=vga,thumbnail=100,split[a][b],[b]palettegen=reserve_transparent=0:stats_mode=single[b];[a][b]paletteuse=new=1,settb=1/25,setpts=N" output.gif
```

**Convert to webp**

Webp is great for web content as all browsers can read the format directly. E.g. I use this for videos on the website.

``` sh
ffmpeg -i input.mp4 -vf "fps=30,scale=720:-1:flags=lanczos" -vcodec libwebp -lossless 0 -compression_level 6 -q:v 50 -loop 0 -preset picture -an -vsync 0 output.webp
```

### Convert to Audio

**Convert MP4 to WAV**

e.g. for [Azure Speech to Text conversion](https://0xfab1.net/tech/azure/speech/).

``` sh
ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav
```

**Convert MP4 to FLAC**

``` sh
ffmpeg -i input.mp4 -acodec flac -bits_per_raw_sample 16 -ar 44100 output.flac
```

**Convert MP4 to MP3**

``` sh
ffmpeg -i input.mp4 -vn -acodec mp3 -ab 320k -ar 44100 -ac 2 output.mp3
```

**Convert MP3 to OGA**

``` sh
ffmpeg -i input.mp3 -c:a libvorbis output.oga
```

**Convert all files in the current path to mp3**

This uses `libmp3lame` with default settings. The script will convert all media files it can handel and continue on error.

``` ps1
Get-ChildItem -file -exclude *.mp3 | Foreach-Object { ffmpeg -i ('"' + $_.Name + '"') -map_metadata -1 -acodec libmp3lame ('"' + $_.BaseName + '.mp3"') }
```

## ImageMagick

Info

| What          | Where                                                                              |
|---------------|------------------------------------------------------------------------------------|
| Official Page | <https://imagemagick.org>                                                          |
| Source        | <https://github.com/imagemagick/imagemagick>                                       |
| Download      | <https://imagemagick.org/script/download.php>                                      |
| Install       | `sudo apt install imagemagick` or `choco install imagemagick`                      |
| Examples      | <https://imagemagick.org/script/examples.php> or <https://imagemagick.org/script/> |

### GIF

Use ImageMagick to optimize a GIF

``` sh
convert -layers Optimize input.gif output.gif
```

### Resize

``` sh
convert file.jpg -resize 1024 × 768 "folder\file.jpg"
```

### Diff Images

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

## Squoosh

Make images smaller using best-in-class codecs, right in the browser.

| What          | Where                                         |
|---------------|-----------------------------------------------|
| Official Page | <https://squoosh.app/>                        |
| Source        | <https://github.com/GoogleChromeLabs/squoosh> |
| Install       | npm i -g @squoosh/cli                         |

### JPEG Example

Simple example to compress an JPEG image

``` sh
squoosh-cli --mozjpeg '{quality:50}' image.png -d output
```

Compress an JPEG image with more parameters (default):

``` sh
squoosh-cli --mozjpeg \
'{ 
   "quality":75, 
   "baseline":false, 
   "arithmetic":false, 
   "progressive":true, 
   "op timize_coding":true, 
   "smoothing":0, 
   "color_space":3, 
   "quant_table":3, 
   "trellis_multipass":false, 
   "trel lis_opt_zero":false, 
   "trellis_opt_table":false, 
   "trellis_loops":1, 
   "auto_subsample":true, 
   "chroma_sub sample":2, 
   "separate_chroma_quality":false, 
   "chroma_quality":75 
}' \
~/path/to/image.jpg -d output ./*
```

### PNG Example

Simple example to compress an PNG image

``` sh
squoosh-cli --oxipng '{level:2}' image.png -d output
```

### WEBP Example

Compress an webp image with more parameters (default):

``` sh
squoosh-cli --webp \
'{ 
    quality: 75,
    target_size: 0,
    target_PSNR: 0,
    method: 4,
    sns_strength: 50,
    filter_strength: 60,
    filter_sharpness: 0,
    filter_type: 1,
    partitions: 0,
    segments: 4,
    pass: 1,
    show_compressed: 0,
    preprocessing: 0,
    autofilter: 0,
    partition_limit: 0,
    alpha_compression: 1,
    alpha_filtering: 1,
    alpha_quality: 100,
    lossless: 0,
    exact: 0,
    image_hint: 0,
    emulate_jpeg_size: 0,
    thread_level: 0,
    low_memory: 0,
    near_lossless: 100,
    use_delta_palette: 0,
    use_sharp_yuv: 0
    }' \
~/path/to/image.jpg -d output ./*
```
