# OBS

Info

| What          | Where                                      |
|---------------|--------------------------------------------|
| Official Page | <https://obsproject.com/>                  |
| Source        | <https://github.com/obsproject/obs-studio> |
| Windows       | `choco install obs-studio`                   |
| Linux         | `sudo apt install obs-studio`                |

## Links

- OBS+[Restream](https://restream.io)=free multi-platform streaming
- VR Streaming <https://github.com/baffler/OBS-OpenVR-Input-Plugin>
- StreamFX: <https://github.com/Xaymar/obs-StreamFX/releases>
- Input overlay <https://github.com/univrsal/input-overlay>
- OBS-virtual-cam: <https://github.com/CatxFish/obs-virtual-cam>

## OBS-virtual-cam

To put them together you have to:

- Follow guide from <https://github.com/CatxFish/obs-virtual-cam>
- Open OBS → Tools → v4l2 Video Output → select "Start"
- Go to the audio/video settings of the vidconf software and select the new video device
- Select new virtual cam from video conferencing tool you use.

## Install on Ubuntu

``` sh
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt update
sudo apt install obs-studio
```
