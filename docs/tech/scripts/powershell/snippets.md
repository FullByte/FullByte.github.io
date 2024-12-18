# Snippets

## Registry

Example to read registry values:

``` ps1
Get-ChildItem -Path "HKCU:\Software\Microsoft\Office\Outlook\Addins"
Get-ChildItem -Path "HKLM:\Software\Microsoft\Office\Outlook\Addins"
```
