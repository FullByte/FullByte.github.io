# adb

Prerequisite

- Download Minimal ADB and Fastboot
- Enable dev mode on phone
- active USB Debugging

## Delete an app on your android phone

Run these commands to delete the app <package name>.

```shell
adb devices # check if your device is visible
adb shell
pm list packages -3 # list hidden system apps
pm uninstall --user 0 <package name>
```
