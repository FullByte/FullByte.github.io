# Windows Terminal

| What  | Where                                                                                         |
|-------|-----------------------------------------------------------------------------------------------|
| Store | <https://www.microsoft.com/de-de/p/windows-terminal/9n0dx20hk701?activetab=pivot:overviewtab> |
| Docs  | <https://docs.microsoft.com/en-us/windows/terminal/>                                          |

## Tips

Open a new Terminal Window with PowerShell 7, cmd and WSL (in my case Ubuntu)

``` ps1
wt -p "PowerShell 7" `; split-pane -p "cmd" `; split-pane -H wsl.exe
```

## Customized command prompt

Install the required modules

``` ps1
Install-Module posh-git -Scope CurrentUser
Install-Module oh-my-posh -Scope CurrentUser
```

Check available themes:

``` ps1
Get-PoshThemes
```

If this doesn't look good install a font that works e.g. [NerdFonts](https://www.nerdfonts.com/).

Now update $PROFILE to load modules with every start

``` ps1
echo "Import-Module posh-git") >> $PROFILE
echo "Import-Module oh-my-posh" >> $PROFILE
```

Add the Theme you like as well e.g. paradox:

``` ps1
echo "Set-PoshPrompt -Theme paradox" >> $PROFILE
```

## settings.json

Edit the "settings.json" and add under "profiles", "defaults" a line for a font you like e.g.:

```json
"fontFace": "MesloLGM NF"
```
