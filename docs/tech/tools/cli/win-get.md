# WinGet

| What          | Where                                                          |
|---------------|----------------------------------------------------------------|
| Official Page | <https://docs.microsoft.com/en-us/windows/package-manager/>    |
| Source        | <https://github.com/microsoft/winget-cli>                      |
| Download      | <https://www.microsoft.com/en-us/p/app-installer/9nblggh4nns1> |

## Install

Install [winget](https://github.com/microsoft/winget-cli/releases) or get it from the [windows store](https://apps.microsoft.com/store/detail/appinstaller/9NBLGGH4NNS1).

Make sure ```%userprofile%\AppData\Local\Microsoft\WindowsApps\``` is in the `Path` Environment Variables.

## Use

Open a new command prompt (with admin privledges for installs) to install e.g. powertoys:

``` ps1
winget install powertoys 
```
