# FFmpeg

FFmpeg is a great tool and here are some examples.

## Info

|What|Where|
|-|-|
|Official Page|<https://ffmpeg.org/>|
|Source|<https://github.com/FFmpeg/FFmpeg>|
|Download|<https://ffmpeg.org/download.html>|
|Docs|<https://ffmpeg.org/documentation.html>|
|Windows|```choco install ffmpeg```|
|Linux|```apt install ffmpeg```|

Helper:

- FFmpeg Command Generator <https://www.mrfdev.com/ffmpeg-command-generator>

## Get File Information

Get codec details of a given video file e.g. "video.mp4":

```ffmpeg
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 video.mp4
```

## Create Time Lapse Video

**Time Lapse using pictures**

This example will create a video based on pictures as input. In this case the files are from a GoPro so all pictures start with a "G" followed by seven digits e.g. G0011565.jpg. The starting number of the series of pictures is 11021 in my example. Change the value for "start_number", the filename prefix (in this case "G") and the length of the number (currently 7) to match your requirements.

```ffmpeg
ffmpeg -framerate 30 -start_number 11021 -i "E:\path\G%07d.jpg" -c:v libx264 "E:\path\output.mp4"
```

**Time Lapse using long video**

This example will shorten a given video to create a time lapse video. The video quality in this example will be reduced to VGA and reduce image quality. If the video is to slow/fast change the value for "thumbnail" (currently at 100).

```ffmpeg
ffmpeg -i input.mp4 -vf "scale=vga,thumbnail=100,split[a][b],[b]palettegen=reserve_transparent=0:stats_mode=single[b];[a][b]paletteuse=new=1,settb=1/25,setpts=N" output.mp4
```

## Compress Video

To compress an avi file you can use H.264 on the output file named e.g. "input.avi" and create a smaller version of the video named "output.mkv"
More details: <https://trac.ffmpeg.org/wiki/Encode/H.264>

```ffmpeg
ffmpeg -i input.avi -c:v libx264 -preset slow -crf 15 output.mkv
```

## Convert Video optimized for Messenger

This works well for Whatsapp, Signal, Threema, Telegram, etc...
Make sure not to reach current allowed max files size.

With sound:

```ffmpeg
ffmpeg -i input.mp4 -vf "scale=vga" messenger.mp4
```

No sound:

```ffmpeg
ffmpeg -i input.mp4 -an -vf "scale=vga" messenger.mp4
```

## SConvert to AV1

```ffmpeg
# Pass 1
ffmpeg -i input.mp4 -c:v libaom-av1 -b:v 200k -filter:v scale=720:-1 -strict experimental -cpu-used 1 -tile-columns 2 -row-mt 1 -threads 8 -pass 1 -f mp4 NUL && ^
# Pass 2
ffmpeg -i input.mp4 -pix_fmt yuv420p -movflags faststart -c:v libaom-av1 -b:v 200k -filter:v scale=720:-1 -strict experimental -cpu-used 1 -tile-columns 2 -row-mt 1 -threads 8 -pass 2 output.mp4
```

## Convert from/to GIF

**From GIF to MP4**

```ffmpeg
ffmpeg -i input.gif -filter_complex "[0:v] fps=15" -vsync 0 -f mp4 -pix_fmt yuv420p output.mp4
```

**From MP4 to GIF**

```ffmpeg
ffmpeg -i input.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```

**GIF from a special section**

Add e.g. "-ss 5.0 -t 3.2" to only create GIF for 3.2 secounds ot "input.mp4"

```ffmpeg
ffmpeg -ss 5.0 -t 3.2 -i input.mp4 -vf "fps=12,scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 output.gif
```

**GIF video summery**

Create a short GIF from a long video

```ffmpeg
ffmpeg -i input.mp4 -vf "scale=vga,thumbnail=100,split[a][b],[b]palettegen=reserve_transparent=0:stats_mode=single[b];[a][b]paletteuse=new=1,settb=1/25,setpts=N" output.gif
```

## Convert from/to webp

```ffmpeg
ffmpeg -ss 32.5 -t 7 -i input.mp4 -vf "fps=10,scale=720:-1:flags=lanczos" -vcodec libwebp -lossless 0 -compression_level 6 -q:v 50 -loop 0 -preset picture -an -vsync 0 output.webp
```

## Stack Videos in a Grid (Horizontally and Vertically)

**2 Videos Horizontally**

```ffmpeg
ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex hstack=inputs=2 horizontal-stacked-output.mp4
```

**2 Videos Vertically**

```ffmpeg
ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex vstack=inputs=2 vertical-stack-output.mp4
```

**Videos of Different Lengths**

```ffmpeg
ffmpeg -i input0.mp4 -i input1.mp4 -filter_complex hstack=inputs=2:shortest=1 shortest-output.mp4
```

**2×2 Grid of Videos**

```ffmpeg
ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 -i input3.mp4 -filter_complex "[0:v][1:v]hstack=inputs=2[top]; [2:v][3:v]hstack=inputs=2[bottom]; [top][bottom]vstack=inputs=2[v]" -map "[v]" finalOutput.mp4
```

```ffmpeg
ffmpeg -i input0.mp4 -i input1.mp4 -i input2.mp4 -i input3.mp4 -i input4.mp4 -i input5.mp4 -filter_complex "[0:v][1:v][2:v]hstack=inputs=3[top]; [3:v][4:v][5:v]hstack=inputs=3[bottom]; [top][bottom]vstack=inputs=2[v]" -map "[v]" finalOutput.mp4
```

## Convert to audio only

**Convert MP4 to WAV**

e.g. for [Azure Speech to Text conversion](https://0xfab1.net/tech/azure/speech/).

```ffmpeg
ffmpeg -i input.mp4 -vn -acodec pcm_s16le -ar 44100 -ac 2 output.wav
```

**Convert MP4 to FLAC**

```ffmpeg
ffmpeg -i input.mp4 -acodec flac -bits_per_raw_sample 16 -ar 44100 output.flac
```

**Convert MP4 to MP3**

```ffmpeg
ffmpeg -i input.mp4 -vn -acodec mp3 -ab 320k -ar 44100 -ac 2 output.mp3
```

**Convert all files in the current path to mp3**

This uses libmp3lame with default settings. The script will convert all media files it can handel and continue on error.

```powershell
Get-ChildItem -file -exclude *.mp3 | Foreach-Object { ffmpeg -i ('"' + $_.Name + '"') -map_metadata -1 -acodec libmp3lame ('"' + $_.BaseName + '.mp3"') }
```
