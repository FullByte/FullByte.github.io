# CLI Tools

More: <https://github.com/you-dont-need/You-Dont-Need-GUI>

## Internet

- w3m Browser: <http://w3m.sourceforge.net/>
- Googler: <https://github.com/jarun/googler>
- DuckDuckGo: <https://github.com/jarun/ddgr> (Browser: <https://duckduckgo.com/tty/>)

## Office

- Mail: <https://aerc-mail.org/>
- Calendar: <https://www.calcurse.org/>
- Charts: <https://github.com/irevenko/tsukae>
- Time Tracker: <https://github.com/jotaen/klog>
- Text Editor: <https://micro-editor.github.io/>
- plaintext accounting tool: <https://github.com/simonmichael/hledger>
- CSV pretty printer: <https://github.com/alexhallam/tv>
- Bits, bytes and address calculator: <https://github.com/jarun/bcal>

## Collaborate

- Chat: <https://weechat.org/> `sudo apt-get install weechat` ([Documentation](https://weechat.org/files/doc/devel/weechat_quickstart.en.html))
- Chat: <https://github.com/irssi/irssi> e.g. `apt install irssi`
- Stream Terminal Session: <https://github.com/miguelmota/streamhut>
- Share Files using QR code: <https://github.com/claudiodangelis/qrcp>
- GPG: <https://github.com/orhun/gpg-tui>
- Video-Chat: <https://github.com/dialup-inc/ascii>

## Media

Music

- Beets: <https://github.com/beetbox/beets> `pip install beets`
- Musikcube (Spotify): <https://github.com/clangen/musikcube>
- Spotify: <https://github.com/Rigellute/spotify-tui>
- Pictures: <https://github.com/posva/catimg>
- Wikipedia: <https://github.com/yashsinghcodes/fetch>

Watch Movies in ASCII

```shell
sudo apt-get install mplayer
wget https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_stereo.ogg
mplayer -vo caca big_buck_bunny_480p_stereo.ogg
```

## File Transfer

- Sync <https://www.etebase.com/> -> <https://www.etesync.com/>
- Sync/Backup <https://syncthing.net/>
- Send Files: <https://github.com/magic-wormhole/magic-wormhole>
- rtorrent: <https://github.com/rakshasa/rtorrent>
- IPFS: <https://ipfs.io>
- transfer.sh: <https://github.com/dutchcoders/transfer.sh>
- croc: <https://github.com/schollz/croc>

## Work with files

- File Explorer: <https://github.com/sayanarijit/xplr>
- Photo Search Tool: <https://github.com/yurijmikhalevich/rclip>
- Terminal UI for SQLite: <https://github.com/mathaou/termdbms>

## Money

- Stocks <https://github.com/achannarasappa/ticker>
- CoinMon <https://github.com/bichenkk/coinmon>

## Games

- nudoku is a ncurses based sudoku game. <https://bronevichok.ru/ttygames/#nudoku>
- Chess: <https://github.com/vinc/littlewing>
- Solitaire: <https://github.com/mpereira/tty-solitaire>

## Other

- Weather: "curl wttr.in" (<https://github.com/chubin/wttr.in>)
- jmespath: <https://github.com/jmespath/jmespath.terminal>

### certstream

```shell
pip install certstream
certstream
```

### nba-go

```shell
sudo npm install -g nba-go
nba-go game -T
```

### Mapscii

```shell
npm install -g mapscii
mapscii
```

### asciinema

Install

```shell
sudo apt install asciinema
```

or

```shell
sudo apt-get install python3 pip
sudo pip3 install asciinema
```

Record a session

```shell
asciinema rec
echo "hello world"
exit
```

Play existing recordings (local/online):

```shell
asciinema play /path/to/asciicast.cast
asciinema play https://asciinema.org/a/237459
```
