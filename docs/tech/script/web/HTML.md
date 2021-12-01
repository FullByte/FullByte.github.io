# HTML

## Show Base64 Images

```HTML
<img src="data:image/png;base64,<Base64codehere>"/>
```

## Link Trick

```HTML
<!doctype html>
<head>
<script>
   function tricked() {
      document.getElementById("naughty").href="http://www.bad.org";
   }
</script>
</head>
<body>
   <a href="http://www.google.com" onclick="tricked()" id="naughty">www.google.com</a>
</body>
```

## Empty HTML File Template

```HTML
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <meta name="description" content="">
    <title>Minimal base.html</title>
</head>
<body>

</body>
</html>
```
