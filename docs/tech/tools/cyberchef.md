# CyberChef

| What          | Where                                        |
|---------------|----------------------------------------------|
| Official Page | <https://gchq.github.io/CyberChef/>          |
| Source        | <https://github.com/gchq/CyberChef>          |
| Download      | <https://github.com/gchq/CyberChef/releases> |

## Recipes

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

### Extract base64, raw inflate and code beautify

```txt
[{"op":"Regular expression","args":["User defined","[a-zA-Z0-9+/=]{30,}",true,true,false,false,false,false,"List matches"]},{"op":"From Base64","args":["A-Za-z0-9+/=",true]},{"op":"Raw Inflate","args":[0,0,"Adaptive",false,false]},{"op":"Generic Code Beautify","args":[]}]
```

### Invoke-Obfuscation

```txt
[{"op":"Find / Replace","args":[{"option":"Regex","string":"\^|\\|-|_|\/|\s"},"",true,false,true,false]},{"op":"Reverse","args":["Character"]},{"op":"Generic Code Beautify","args":[]},{"op":"Find / Replace","args":[{"option":"Simple string","string":"http:"},"http://",true,false,true,false]}]
```

### From CharCode

Decode Scripts using Charcode to represent characters in order to evade from AV and EDR solutions.

```txt
[{"op":"Regular expression","args":["User defined","([0-9]{2,3}(,\s|))+",true,true,false,false,false,false,"List matches"]},{"op":"From Charcode","args":["Comma",10]},{"op":"Regular expression","args":["User defined","([0-9]{2,3}(,\s|))+",true,true,false,false,false,false,"List matches"]},{"op":"From Charcode","args":["Space",10]}]
```

### Google ei timestamp

Google ei dates are an encoded Base64 string containing various parameters including a Unix timestamp as recorded by Google.

```txt
[{"op":"From Base64","args":["A-Za-z0-9-_=",true]},{"op":"To Hex","args":["None"]},{"op":"Take bytes","args":[0,8,false]},{"op":"Swap endianness","args":["Hex",4,true]},{"op":"From Base","args":[16]},{"op":"From UNIX Timestamp","args":["Seconds (s)"]}]
```

## Easter eggs

Open CyberChef and type the Konami Code: "UUDDLRLRBA"
