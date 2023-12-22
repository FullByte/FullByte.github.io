# Linux IoT

Add your user to the dialout group, then logout and log back in:

```sh
sudo usermod -a -G dialout $USER
```

"Cannot open /dev/tty0: Permission denied" -> Grant permissions to read/write to the serial port with this terminal command (replace tty port)

```sh
sudo chmod a+rw /dev/tty
```

"Failed to open /dev/tty (port busy)" -> Kill the busy serial port with command (replace tty port):

```sh
fuser -k /dev/tty
```
