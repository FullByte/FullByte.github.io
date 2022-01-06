# Package Manager

These Windows Package Manager are a great way to install software on Windows.

## Chocolatey

Get Chocolatey

- Install Chocolatey: ```Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))```
- Update Chocolatey: ```choco upgrade chocolatey```

Get Packages

- Find a Package: List: ```choco list 7zip``` and specific: ```choco find 7zip -e -v```
- Install a Package: ```choco -y install 7zip```
- List Local Packages: ```choco list --local-only```
- Uninstall a Package: ```choco uninstall 7zip```
- Update all Packages: ```choco upgrade all```

## Scoop

TODO

## WinGet

TODO
