# Music

- Beets: <https://github.com/beetbox/beets> `pip install beets`
- Musikcube (Spotify): <https://github.com/clangen/musikcube>
- Background Noise: <https://github.com/JaDogg/noisebox>
- Spotify: [spotify-tui](https://github.com/Rigellute/spotify-tui) or [ncspot](https://github.com/hrkfdn/ncspot)

Example running ncspot:

![ncspot](_ncspot.png)

Visualize audio in the terminal

paura_lite.py takes no arguments and just records sounds, while visualizing each segment's spectrogram in the console.

Install required tools

``` sh
sudo apt update
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install python3-opencv gnuplot
pip3 install numpy pyaudio termplotlib
cd ~
git clone https://github.com/tyiannak/pyAudioAnalysis.git
cd pyAudioAnalysis
pip3 install -r ./requirements.txt
pip3 install -e .
cd ..
git clone https://github.com/tyiannak/paura
cd paura
python3 paura_lite.py
```

This is how it should look like: <https://www.youtube.com/watch?v=YEi9AmA-07s>