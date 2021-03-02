# List all .lnk files and their image paths

$Path = "$Env:ProgramData\Microsoft\Windows\Start Menu\Programs"
$StartMenu = Get-ChildItem $Path -Recurse -Include *.lnk

ForEach ($Item in $StartMenu) {
   $Shell = New-Object -ComObject WScript.Shell
   $Properties = @{
        ShortcutName = $Item.Name
        Target = $Shell.CreateShortcut($Item).targetpath
        }
    New-Object PSObject -Property $Properties
}

[Runtime.InteropServices.Marshal]::ReleaseComObject($Shell) | Out-Null
