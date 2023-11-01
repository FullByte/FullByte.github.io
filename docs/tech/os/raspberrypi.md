# Raspberry Pi

Alternative OS: <https://dietpi.com/>

## Config

### Display Rotation

Edit ```/boot/config.txt```

``` sh
display_rotate=0
display_rotate=1 # 90 degress
display_rotate=2 # 180 degrees
display_rotate=3 # 270 degrees
```

### Headless Setup

Enable SSH by placing a file named "ssh" onto the boot partition of the SD card.

``` sh
touch /path/to/sd/card/volume/ssh
```

### Configure WiFi

``` sh
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
network={
    ssid="WiFi"
    psk="WiFiPassword"
}
sudo wpa_cli reconfigure
```

eventually reboot and/or try this:

``` sh
sudo ifconfig wlan0 down
sudo ifconfig wlan0 up
sudo ifconfig wlan0 | grep inet
sudo service networking restart
```

Test Config:

``` sh
wpa_supplicant -i wlan0 -D wext -c /etc/wpa_supplicant/wpa_supplicant.conf -d
```

## Helper

### Find Raspberry Pi in network

Find Pi with an ARP scan filtering for known Pi MAC Addresses

From windows:

```cmd
arp -a | findstr b8-27-eb
```

From linux

``` sh
arp-scan --localnet --interface=eth0 | grep b8:27:eb
arp-scan --localnet --interface=wlan0 | grep b8:27:eb
```

### Stress test

Tools to stress test your Raspberry Pi:

- <https://github.com/nschloe/stressberry>
- <https://github.com/akopytov/sysbench>
- <https://github.com/ColinIanKing/stress-ng>

### Stable Wi-Fi and Bluetooth

Making your Raspberry Pi resilient to Wi-Fi and Bluetooth connection failures involves a combination of software configurations, scripts, and sometimes additional hardware. Here are some steps you can take:

1. **Persistent Wi-Fi Connection**:
   - **WPA_Supplicant**: Ensure your `/etc/wpa_supplicant/wpa_supplicant.conf` is correctly set up. This is the primary configuration file for Wi-Fi.
   - **Auto-Reconnect Script**: Create a script that checks the Wi-Fi connection periodically and tries to reconnect if the connection is lost.
     ```bash
     #!/bin/bash
     while true; do
       if ! ping -c 1 google.com; then
         sudo ifdown wlan0 && sudo ifup wlan0
       fi
       sleep 60
     done
     ```
     Save the script, make it executable with `chmod +x script_name.sh`, and consider adding it to your crontab or systemd to run on boot.

2. **Persistent Bluetooth Connection**:
   - **Bluetoothctl**: Use `bluetoothctl` to pair and trust devices. Once a device is trusted, it will attempt to auto-reconnect.
   - **Auto-Reconnect Script**: Similar to Wi-Fi, you can create a script that checks the Bluetooth connection and tries to reconnect if it's lost. This might be a bit more complex, depending on the Bluetooth service you're using (like BlueZ).

3. **Network Manager**:
   - Consider using a more robust network manager like `NetworkManager` or `ConnMan`. These tools often handle reconnections better than the default setup.

4. **External Watchdog**:
   - Some advanced users employ an external hardware watchdog. This is a separate piece of hardware that monitors the Raspberry Pi and can reset it if it detects a failure. This is a more extreme solution and is typically used in scenarios where the Raspberry Pi must remain operational.

5. **External Antenna**:
   - If you're experiencing connection drops due to weak signals, consider using a Raspberry Pi variant or a Wi-Fi/Bluetooth dongle that supports external antennas. An external antenna can significantly improve connection stability.

6. **Regular Updates**:
   - Ensure your Raspberry Pi's OS and packages are regularly updated. Updates often contain bug fixes and improvements for hardware drivers, including Wi-Fi and Bluetooth.

7. **Logs and Monitoring**:
   - Regularly check system logs for any Wi-Fi or Bluetooth-related errors. The `dmesg` and `journalctl` commands can be useful.
   - Consider setting up monitoring tools like `iftop`, `nmon`, or `bmon` to keep an eye on network activities.

8. **Static IP**:
   - Assigning a static IP to your Raspberry Pi can sometimes help in scenarios where the DHCP server is causing connectivity issues.

9. **Power Supply**:
   - Ensure you're using a reliable power supply. Insufficient power can cause a myriad of issues, including unstable network connections.

Remember, the key to resilience is redundancy and regular monitoring. By setting up scripts to auto-reconnect and regularly checking the health of your connections, you can ensure that your Raspberry Pi remains connected most of the time.
