# rclone

rclone is a great tool to backup, copy, sync files to the cloud encrypted and without the client installed on the local machine.

## Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

## Restore rclone.conf

Run this command to find out where your `rclone.conf` file is.

```sh
rclone config file
```

If you installed rclone and didn't configure anything yet you will get this information

```txt
Configuration file doesn't exist, but rclone will use this path:
C:\Users\0xfab1\AppData\Roaming\rclone\rclone.conf
```

else, rclone will repond as follows:

```txt
Configuration file is stored at:
C:\Users\0xfab1\AppData\Roaming\rclone\rclone.conf
```

Be sure to backup this file so you restore it (overwrite it or partcially update).

If you restore a file you may need to refresh the token(s) you are using.

Run the following command todo so e.g. for connection call "onedrive":

```sh
rclone config reconnect onedrive:
```

The process will walk though parts of the steps you did whenever you set up this connection. ONce done the connection should work again.
