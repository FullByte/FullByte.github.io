# Tweaks

Releases and Editions

- [Windows 10 Enterprise LTSC](https://docs.microsoft.com/en-us/windows/whats-new/ltsc/) is a version with less updates and less noise.
- [Windows 10 Releases](https://docs.microsoft.com/en-us/windows/release-health/release-information)
- [Compare Windows 10 Editions](https://www.microsoft.com/en-us/WindowsForBusiness/Compare) and also check [wikipedia](https://en.wikipedia.org/wiki/Windows_10_editions)

Windows History: <https://winhistory.de>

## Windows Cleaner

Windows Base Install (depending on the release you are using) comes with more or less possibly undesired settings/applications. Here are some tools that take care of that:

- Sophia Script for Windows: <https://github.com/farag2/Sophia-Script-for-Windows>

Be careful with these tools and scripts; ideally copy those parts of the script you want and create your own.

## Commands that help

- Export current drivers: ```pnputil /export-driver * e:\treiber```

## Pimp Desktop

Note really required and may just waste laptop battery life and/or desktop CPU but nice to look at/use:

- Animated Background and Screen Saver: <https://github.com/rocksdanister/lively>
- Microsoft PowerToys: <https://docs.microsoft.com/en-us/windows/powertoys/>
- Ear Trumpet: <https://github.com/File-New-Project/EarTrumpet>

## Useful shortcuts

### App volume and device preferences

URI for "App volume and device preferences" is: ```ms-settings:apps-volume```

Create a file e.g. ```winaudio.url``` with the following content:

``` url
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,0
[InternetShortcut]
IDList=
URL=ms-settings:apps-volume
```
