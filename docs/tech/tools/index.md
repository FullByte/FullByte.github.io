# Tool Overview

## Sort Information

Obviously there are many approaches to this. I will explain how I sort information of relevance to me and hopefully some methods are interesting to you or help decide how to approach the topic so it works best for you.

My tooling and methods have changed over time and I expect them to change in future. Hopefully I will remember to update this page if I do so. My current approach focuses on two main things: clear text and the right tool/place/format to store the information so I can easily use it when needed.

Here is an overview of different clear-text information and where I store it:

- Blog/Doku: Mkdocs -> Repo
- Notes: Logseq, Joplin, Obsidian -> DAV Sync
- Code Examples: Jupyter Notebooks -> Repo
- Code: Repo / Gist -> Repo
- Snippets: VSCode Snippets -> Repo
- One-liner: Navi -> Repo

## Download Files

Download files, depending on your purpose with the following tools:

| Purpose  | 0xfab1                        | Tool                                             |
|----------|-------------------------------|--------------------------------------------------|
| Videos   | [yt-dlp](yt-dlp.md)           | [yt-dlp](https://github.com/yt-dlp/yt-dlp)       |
| Torrents | [qbittorrent](qbittorrent.md) | [qbittorrent](https://www.qbittorrent.org/)      |
| IRC XDCC | [irc](irc.md)                 | [mirc](https://www.mirc.com/)                    |
| Images   | [gallery-dl](gallery-dl.md)   | [gallery-dl](https://github.com/mikf/gallery-dl) |
| Files    | [wget](wget.md)               | [wget](https://ftp.gnu.org/gnu/wget/)            |

## Copy Files

The best tools to copy files, depending on source and destination:

| Destination     | 0xfab1                    | Tool                                                                                                 | Comment                                                                                            |
|-----------------|---------------------------|------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| Cloud           | [rclone](rclone.md)       | [rclone](https://rclone.org/)                                                                        | Encryption possible, no client needed, many vendors supported                                      |
| Local drive/NAS | [RoboCopy](robocopy.md)   | [RoboCopy](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) | Already installed, has sync option, works.                                                         |
| SFTP/WebDAV     | [WinSCP](winscp.md)       | [WinSCP](https://winscp.net)                                                                         | Scripting possible using winscp.com                                                                |
| Sync P2P        | [Syncthing](syncthing.md) | [Syncthing](https://syncthing.net/)                                                                  | Use [SyncTrayzor](https://github.com/canton7/SyncTrayzor) for GUI and sync files via peer-to-peer. |
| Backup Server   | [Restic](restic.md)       | [Restic](https://restic.net/)                                                                        | Good for regular backups. Uses rclone in the backend.                                              |

## Convert Files

Depending of the file typ, use the following tools to convert the original file into something else:

| File type     | 0xfab1                         | Tool                                   |
|---------------|--------------------------------|----------------------------------------|
| Text          | [Pandoc](pandoc.md)            | [Pandoc](https://pandoc.org/)          |
| Audio & Video | [FFmpeg](ffmpeg.md)            | [FFmpeg](https://ffmpeg.org/)          |
| Pictures      | [ImageMagick](image-magick.md) | [ImageMagick](https://imagemagick.org) |
| eBooks        | [Calibre](calibre.md)          | [Calibre](https://calibre-ebook.com/)  |

## Print and Scan

For printing and scanning I personally prefer a laser printer with LAN support. There should be no need to install the vendors drivers and extra software; simply go with the OS printer drivers identified for your device.

### Windows

For scanning on windows I prefer [NAPS2](https://www.naps2.com).

Alternatively try [VueScan](https://www.hamrick.com/).

### Linux

#### Print

Usually there is no need to install specific drivers to print. Use the [HP print and scan drivers for linux](https://developers.hp.com/hp-linux-imaging-and-printing) if you have issues with your printer. This is required for scanning.

Steps to get HP Printers running on Ubuntu 20.04:

- Download the latest [dhplip rivers](https://sourceforge.net/projects/hplip/files/). Check this [overview](https://developers.hp.com/hp-linux-imaging-and-printing/gethplip) if link is not working.
- Run the script with ```sh hplip-<version>.run``` and go throgh the steps.
- Download the latest [hplip plugin](https://developers.hp.com/hp-linux-imaging-and-printing/plugins)
- Run the script with ```sh hplip-<version>.run```
- Now run the HO Device Manger or your scan tool of choice e.g. SimpleScan or gscan2pdf.

#### Scan

Install SimpleScan

``` sh
sudo apt-get install simple-scan

gsettings set org.gnome.SimpleScan jpeg-quality 85
gsettings set org.gnome.SimpleScan brightness -10
gsettings set org.gnome.SimpleScan contrast 25 
```

Install gscan2pdf

``` sh
sudo apt-get install gscan2pdf
sudo apt-get install tesseract-ocr-deu 
```

## RSS

RSS (Rich Site Summary or Really Simple Syndication) is a format for delivering regularly changing web content. Many news-related sites, blogs, and other online publishers syndicate their content as an RSS Feed.

### YouTube

There are 3 RSS feed types for YouTube:

- User : <https://www.youtube.com/feeds/videos.xml?user=>
- Channel : <https://www.youtube.com/feeds/videos.xml?channel_id=>
- Playlist : <https://www.youtube.com/feeds/videos.xml?playlist_id=>

### GitHub

Add ".atom" to a given commit link to get an RSS Reader update on a given file/folder or the entire project.

For example:

- Link: <https://github.com/FullByte/FullByte.github.io/commits/main>
- RSS Feed: <https://github.com/FullByte/FullByte.github.io/commits/main.atom>

Add the atom link to your rss feed reader to get notified on updates.

## Privacy Link List

A list of lists and overviews on the topic privacy tools. Please be aware that using "better" tools do not improve your privacy much; it's just a small step.

### Links

- [Briar](https://briarproject.org/)
- [Browser Fingerprint](https://amiunique.org/fp)
- [Defensive Computing Checklist](https://www.defensivecomputingchecklist.com/)
- [EFF Surveillance Self-Defense](https://ssd.eff.org/)
- [Magisk](https://github.com/topjohnwu/Magisk)
- [Mobile Messenger overview](https://www.securemessagingapps.com/)
- [Open Source alternatives](https://github.com/GorvGoyl/clone-wars)
- [Open Source alternatives](https://www.opensourcealternative.to/)
- [Prism-break](https://prism-break.org/en/all)
- [Privacy Guides](https://www.privacyguides.org)
- [privacy is sexy](https://privacy.sexy/)
- [privacy test](https://privacytests.org/)
- [Switching software](https://switching.software)
- [The Hitchhiker’s Guide to Online Anonymity](https://anonymousplanet.org/guide.html)
- [use plaintext in emails](https://useplaintext.email)

### Client Alternatives

If you can't or don't want to use platform alternatives you can at least use different clients/alternative websites, text only offerings from a given source.

Great Browser Plugin to automatically redirect to some of these services: <https://github.com/libredirect/libredirect>

| Service    | Client                                                                                                                                                                                                                                         |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Video      | [newpipe](https://newpipe.net/) and [Piped](https://piped.video) and [Invidious](https://docs.invidious.io/instances/)                                                                                                                         |
| Social     | [Twitter](https://nitter.net), [Instagram](https://bibliogram.art/), [Reddit](https://teddit.net/) or [old Reddit](https://old.reddit.com/), [Tumblr](https://www.tumbex.com/)                                                                 |
| World News | [NPR](https://text.npr.org/), [Google News](http://68k.news/), [CNN](https://lite.cnn.com/en),  [CBC](https://www.cbc.ca/lite/trending-news), [The Guadian](https://guardian.gyford.com/), [New York Times](https://www.nytimes.com/timeswire) |
| Tech News  | [skimfeed](https://skimfeed.com/), [Hacker News](https://hackerweb.app/)                                                                                                                                                                       |
| Search     | [SearXNG](https://github.com/searxng/searxng), [instances](https://searx.space/), [startpage](https://www.startpage.com), [DuckDuckGo](https://duckduckgo.com/), [millionshort](https://millionshort.com/)                                     |
| Maps       | [OSM](https://www.openstreetmap.org), [qwant](https://www.qwant.com/maps)                                                                                                                                                                      |
| Music      | [libre.fm](https://libre.fm/)                                                                                                                                                                                                                  |

### Fediverse

More info about the [Fediverse](https://fediverse.party/en/fediverse/).

Alternatives to:

- Facebook: [Friendica](https://friendi.ca)
- GoodReads: [BookWyrm](https://joinbookwyrm.com)
- Instagram: [Pixelfed](https://pixelfed.org)
- MeetUp: [Mobilizon](https://joinmobilizon.org)
- Podcasting: [Castopod](https://castopod.org)
- Reddit: [Lemmy](https://join-lemmy.org)
- Social Media: [Mastodon](https://joinmastodon.org)
- Soundcloud: [Reel2Bits](https://reel2bits.org)
- Spotify: [Funkwhale](https://funkwhale.audio)
- Twitter: [Pleroma](https://pleroma.social/) and [Misskey](https://join.misskey.page/en-US/)
- YouTube: [PeerTube](https://joinpeertube.org)

### Android Apps

#### Open board

100% FOSS keyboard, based on AOSP

- Github: <https://github.com/dslul/openboard>
- f-droid: <https://f-droid.org/packages/org.dslul.openboard.inputmethod.latin/>

#### Gadgetbridge

- homepage: <https://gadgetbridge.org/>
- f-droid: <https://f-droid.org/packages/nodomain.freeyourgadget.gadgetbridge/>
- Source: <https://codeberg.org/Freeyourgadget/Gadgetbridge/>

### DRM

Buy DRM free products (Media, Software,..)

- <https://www.defectivebydesign.org/guide>

## Resume

Ways to create a CV/resume.

### Links

Inspiring tools/templates:

- <https://www.canva.com/search/templates?q=resume>
- <https://jsonresume.org/themes/>

### JSON Resume

[JSON Resume](https://jsonresume.org) is an open source solution to create a JSON-based standard for resumes. Create a HTML or PDF output using the [CLI](https://github.com/jsonresume/resume-cli). Use a different theme without changing anything in the resume file.

- Install: ```npm i resume-cli``` or use remotly with ```npx resume```
- Create initial json file: ```resume init```
- Edit `resume.json` and validate with resume validate: ```resume validate```
- Create a PDF: ```resume export resume.pdf```
- Create a HTML file: ```resume export resume.html```
- Host HTML file: ```resume serve```

To use other [themes](https://jsonresume.org/themes/) browse and select what you prefer (and follow their config/install doc.)

Example for theme [kendall](https://github.com/LinuxBozo/jsonresume-theme-kendall):

``` bash
cd ~/path/to/resume/
git clone https://github.com/LinuxBozo/jsonresume-theme-kendall
cp resume.json /jsonresume-theme-kendall/resume.json
cd jsonresume-theme-kendall
npm install
resume export resume.pdf --theme .
resume export resume.html --theme .
resume serve --theme .
```

### Man page + curl

Create a [Linux manual page formated](https://www.man7.org/linux/man-pages/man7/man.7.html) file which can be downloaded and intepreted using the [man](https://www.kernel.org/doc/man-pages/) command.

I created a markdown file and converted it using [pandoc](https://pandoc.org/). Use [definition-lists](https://pandoc.org/MANUAL.html#definition-lists) and [metadata-blocks](https://pandoc.org/MANUAL.html#metadata-blocks) to pimp the file if you like (not really needed for our incentive of creating a CV)

Convert the file as follows

``` pandoc
pandoc --standalone --to man cv.md -o cv.7
```

To read the created man page simply run: ```man cv.7```

If the file is hosted online run the following command to read the file:

- Windows: use [groff](https://www.gnu.org/software/groff/#downloading) or [mandoc](https://embedeo.org/ws/doc/man_windows/) or simply install WSL and follow Linux command below.
- Linux: ```man <( curl -sL https://cv.example.com/cv.7 )```
- MacOS: ```curl -sL https://cv.example.com/cv.7 > /tmp/cv.7; man /tmp/cv.7```

I uploaded my `cv.7` file to <https://cv.fromm.rocks/cv.7>. Access to subdomain "cv" is password protected using htaccess.

In order to access the password protected file we need to run curl as follows: ```curl -u username:password https://cv.example.com```

Alternativly it is also possible to use wget: ```wget --http-user=username --http-password=password http://cv.example.com```

Combine this with the command and we have a one-liner to read a cv using `man` :)

- Linux: ```man <( curl -u "user":"password" -sL https://cv.example.com/cv.7 )```
- MacOS: ```curl -u "user":"password" -sL https://cv.example.com/cv.7 > /tmp/cv.7; man /tmp/cv.7```
