# adb

| What     | Where                                                          |
|----------|----------------------------------------------------------------|
| Download | <https://developer.android.com/studio/releases/platform-tools> |
| Docs     | <https://developer.android.com/studio/command-line/adb>        |
| Windows  | `choco install adb`                                            |
| Ubuntu   | `sudo apt -y install adb`                                  |

Prerequisite

- Download Minimal ADB and Fastboot
- Enable dev mode on phone
- active USB Debugging

Recovery Mode

1. Power off the phone
2. Hold the Power button + the Vol Down button to boot into the Bootloader
3. Select Recovery Mode and press the Power button
4. If you are trying to get into recovery mode, and see an android on his back with No Command, then press and hold Power, then tap Volume Up once, then release Power. This will display the Recovery Mode Menu

## Unlock bootloader

``` sh
adb -d reboot bootloader
fastboot oem unlock
```

## Delete an app on your android phone

Run these commands to delete a specific app <package name>.

``` sh
adb devices # check if your device is visible
adb shell
pm list packages -3 # list hidden system apps
pm uninstall --user 0 <package name>
```

## Install CyanogenMod 12

<https://cyanogenmodroms.com> (successor is <https://lineageos.org/>)

``` sh
adb push cm12.zip /sdcard/
adb reboot bootloader
fastboot oem unlock
fastboot flash recovery twrp.img
```

## Troubleshooting

On Windows, if the drivers you have are not signed run this to accept unsigned drivers. Not recommended but possibly the only option. Requires a reboot.

``` sh
bcdedit.exe -set TESTSIGNING OFF
bcdedit.exe -set loadoptions ENABLE_INTEGRITY_CHECKS
```
