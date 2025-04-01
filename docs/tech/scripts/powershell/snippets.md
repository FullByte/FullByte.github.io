# Snippets

## Registry

Example to read registry values:

``` ps1
Get-ChildItem -Path "HKCU:\Software\Microsoft\Office\Outlook\Addins"
Get-ChildItem -Path "HKLM:\Software\Microsoft\Office\Outlook\Addins"
```

## Media

One-liner to convert all PNG Images of a folder to JPG images:

``` ps1
Get-ChildItem -Path (Get-Location) -Filter *.png | ForEach-Object { $img=[System.Drawing.Image]::FromFile($_.FullName); $jpg=([System.IO.Path]::ChangeExtension($_.FullName, '.jpg')); $enc=[System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders()|?{$_.MimeType -eq 'image/jpeg'}; $par=New-Object System.Drawing.Imaging.EncoderParameters(1); $par.Param[0]=New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality,90); $img.Save($jpg,$enc,$par); $img.Dispose() }; Write-Output 'Conversion complete.'
```
