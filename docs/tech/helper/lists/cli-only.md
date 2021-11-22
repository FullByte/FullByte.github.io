# CLI/TUI Tools

More: <https://github.com/you-dont-need/You-Dont-Need-GUI>

## Internet

- w3m Browser: <http://w3m.sourceforge.net/>
- Googler: <https://github.com/jarun/googler>
- DuckDuckGo: <https://github.com/jarun/ddgr> (Browser: <https://duckduckgo.com/tty/>)
- Twitter: [rainbowstream](https://github.com/orakaro/rainbowstream) `sudo apt -y install python3-pip && sudo pip3 install rainbowstream`

## Office

- Mail: <https://aerc-mail.org/>
- Calendar: <https://www.calcurse.org/>
- Charts: <https://github.com/irevenko/tsukae>
- Time Tracker: <https://github.com/jotaen/klog>
- Text Editor: <https://micro-editor.github.io/>
- plaintext accounting tool: <https://github.com/simonmichael/hledger>
- CSV pretty printer: <https://github.com/alexhallam/tv>
- Bits, bytes and address calculator: <https://github.com/jarun/bcal>
- Code Editor: <https://micro-editor.github.io/>

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
- Spotify: [spotify-tui](https://github.com/Rigellute/spotify-tui) or [ncspot](https://github.com/hrkfdn/ncspot)
- Pictures: <https://github.com/posva/catimg>
- Wikipedia: <https://github.com/yashsinghcodes/fetch>

Example running ncspot:

![ncspot](_ncspot.png)

Watch Movies in ASCII

```sh
sudo apt-get install mplayer
wget https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_stereo.ogg
mplayer -vo caca big_buck_bunny_480p_stereo.ogg
```

Using [mpv](https://mpv.io/) with [libcaca](http://caca.zoy.org/wiki/libcaca)

```sh
mpv --quiet -vo=caca 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
```

Using [mpv](https://mpv.io/) with tct:

```sh
mpv --quiet -vo=tct 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
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
- Text-based desktop environment: <https://github.com/netxs-group/vtm>

Fun Stuff

| Tool       | Install                    | Use            |
|------------|----------------------------|----------------|
| certstream | pip install certstream     | certstream     |
| nba-go     | sudo npm install -g nba-go | nba-go game -T |
| Mapscii    | npm install -g mapscii     | mapscii        |
| asciinema  | pip install asciinema      | asciinema rec  |
