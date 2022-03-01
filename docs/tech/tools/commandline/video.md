# Video

## Watch Movies in ASCII

``` sh
sudo apt-get install mplayer
wget https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_stereo.ogg
mplayer -vo caca big_buck_bunny_480p_stereo.ogg
```

Using [mpv](https://mpv.io/) with [libcaca](http://caca.zoy.org/wiki/libcaca)

``` sh
mpv --quiet -vo=caca 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
```

Using [mpv](https://mpv.io/) with tct:

``` sh
mpv --quiet -vo=tct 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
```

## asciinema

Install

``` sh
sudo apt-get install python3 pip
sudo pip3 install asciinema
```

Record a session

``` sh
asciinema rec
echo "hello world"
exit
```

Play existing recordings (local/online):

``` sh
asciinema play /path/to/asciicast.cast
asciinema play https://asciinema.org/a/237459
```