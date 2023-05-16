# CyberChef

| What          | Where                                                                |
|---------------|----------------------------------------------------------------------|
| Official Page | <https://gchq.github.io/CyberChef/>                                                   |
| Source        | <https://github.com/gchq/CyberChef>                                       |
| Download      | <https://github.com/gchq/CyberChef/releases>                              |

## Recipies

### Extract Code

```txt
Strings('Single byte',258,'All printable chars (U)',false,false,false)
Find_/_Replace({'option':'Regex','string':'[\\[\\]_\\n]'},'',true,false,true,false)
Drop_bytes(0,559,false)
From_Base64('A-Za-z0-9+/=',true,false)
Decode_text('UTF-16LE (1200)')
Find_/_Replace({'option':'Regex','string':'[ \' ( ) + " ` ]'},'',true,false,true,false)
Find_/_Replace({'option':'Regex','string':'b2H_'},'http',true,false,true,false)
Extract_URLs(false,false,false/disabled)
```

## Eastereggs

Open CyberChef and type the Konami Code: "UUDDLRLRBA"
