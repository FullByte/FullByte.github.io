# Fritzbox

## Remote Reboot

``` bat
set IP=192.168.178.1
set FRITZUSER=rebootuser
set FRITZPW=rebootuserpw
set location=/upnp/control/deviceconfig
set uri=urn:dslforum-org:service:DeviceConfig:1
set action=Reboot

curl -k -m 5 --anyauth -u "%FRITZUSER%:%FRITZPW%" http://%IP%:49000%location% -H "Content-Type: text/xml; charset="utf-8"" -H "SoapAction:%uri%#%action%" -d "<?xml version='1.0' encoding='utf-8'?><s:Envelope s:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/' xmlns:s='http://schemas.xmlsoap.org/soap/envelope/'><s:Body><u:Reboot xmlns:u='urn:dslforum-org:service:DeviceConfig:1'></u:Reboot></s:Body></s:Envelope>" -s > output.log 2>&1
```

## Log Network Traffic

Open <http://192.168.178.1/html/capture.html> and start logging traffic. The stored file can be viewed in Wireshark.

## Script Bookmarks

<p><a title="Censor" href="javascript:(function (dummyze, entry) {function textWalker(node, cbck) {var i = -1,n, s, w, h;if (!node) {return}if (node.nodeType === 3) {cbck(node, 'nodeValue');return}if (node.tagName == 'IFRAME') {try {textWalker(node.contentDocument.documentElement, cbck)} catch (e) {}return}if (node.tagName == 'STYLE' || node.tagName == 'SCRIPT' || node.tagName == 'SVG') {return}if (node.tagName == 'IMG') {s = getComputedStyle(node);node.src = 'https://dummyimage.com/' + (parseInt(s.width) || 10) + 'x' + (parseInt(s.height) || 10);return}if (node.tagName == 'INPUT' || node.tagName == 'TEXTAREA') {cbck(node, 'placeholder');cbck(node, 'value');return}if (node.tagName) {if ((s = node.getAttribute('style')) &amp;&amp; (s = (s = getComputedStyle(node)).backgroundImage) &amp;&amp; (s != 'none') &amp;&amp; (s = (s.match(/url\(&quot;([^&quot;]+)&quot;\)/))) &amp;&amp; (s = s[1])) {pic = new Image();pic.onload = function () {node.style.backgroundImage = 'url(https://dummyimage.com/' + (parseInt(pic.width) || 10) + 'x' + (parseInt(pic.height) || 10) + ')'};pic.src = s;}if ((b = (b = getComputedStyle(node, '::before')).content) &amp;&amp; (b != 'none') &amp;&amp; b.indexOf('attr(') == 0 &amp;&amp; (b = b.match(/^attr\((.*?)\)$/)) &amp;&amp; (b = b[1])) {cbck(node, b);}if ((b = (b = getComputedStyle(node, '::after')).content) &amp;&amp; (b != 'none') &amp;&amp; b.indexOf('attr(') == 0 &amp;&amp; (b = b.match(/^attr\((.*?)\)$/)) &amp;&amp; (b = b[1])) {cbck(node, b);}while (n = node.childNodes[++i]) textWalker(n, cbck);}};textWalker(entry, dummyze)})(function (n, p, a, w, pic) {p = p || 'nodeValue';a = n[p];if (a) {w = a.replace(/\S/g, '\u2591');if (a != w) n[p] = w} else {a = n.getAttribute &amp;&amp; n.getAttribute(p);if (a) {w = a.replace(/\S/g, '\u2591');if (a != w) n.setAttribute(p, w);}}}, document.documentElement);">Censor</a>
</p>

``` js
(function(dummyze, entry) {
    function textWalker(node, cbck) {
        var i = -1,
            n, s, w, h;
        if (!node) {
            return
        }
        if (node.nodeType === 3) {
            cbck(node, 'nodeValue');
            return
        }
        if (node.tagName == 'IFRAME') {
            try {
                textWalker(node.contentDocument.documentElement, cbck)
            } catch (e) {}
            return
        }
        if (node.tagName == 'STYLE' || node.tagName == 'SCRIPT' || node.tagName == 'SVG') {
            return
        }
        if (node.tagName == 'IMG') {
            s = getComputedStyle(node);
            node.src = 'https://dummyimage.com/' + (parseInt(s.width) || 10) + 'x' + (parseInt(s.height) || 10);
            return
        }
        if (node.tagName == 'INPUT' || node.tagName == 'TEXTAREA') {
            cbck(node, 'placeholder');
            cbck(node, 'value');
            return
        }
        if (node.tagName) {
            if ((s = node.getAttribute('style')) & amp; & amp;
                (s = (s = getComputedStyle(node)).backgroundImage) & amp; & amp;
                (s != 'none') & amp; & amp;
                (s = (s.match(/url\(&quot;([^&quot;]+)&quot;\)/))) & amp; & amp;
                (s = s[1])) {
                pic = new Image();
                pic.onload = function() {
                    node.style.backgroundImage = 'url(https://dummyimage.com/' + (parseInt(pic.width) || 10) + 'x' + (parseInt(pic.height) || 10) + ')'
                };
                pic.src = s;
            }
            if ((b = (b = getComputedStyle(node, '::before')).content) & amp; & amp;
                (b != 'none') & amp; & amp; b.indexOf('attr(') == 0 & amp; & amp;
                (b = b.match(/^attr\((._?)\)$/)) & amp; & amp;
                (b = b[1])) {
                cbck(node, b);
            }
            if ((b = (b = getComputedStyle(node, '::after')).content) & amp; & amp;
                (b != 'none') & amp; & amp; b.indexOf('attr(') == 0 & amp; & amp;
                (b = b.match(/^attr\((._?)\)$/)) & amp; & amp;
                (b = b[1])) {
                cbck(node, b);
            }
            while (n = node.childNodes[++i]) textWalker(n, cbck);
        }
    };
    textWalker(entry, dummyze)
})(function(n, p, a, w, pic) {
    p = p || 'nodeValue';
    a = n[p];
    if (a) {
        w = a.replace(/\S/g, '\u2591');
        if (a != w) n[p] = w
    } else {
        a = n.getAttribute & amp; & amp;
        n.getAttribute(p);
        if (a) {
            w = a.replace(/\S/g, '\u2591');
            if (a != w) n.setAttribute(p, w);
        }
    }
}, document.documentElement);
```

<p><a href="javascript:(function() { 'use strict'; window.addEventListener('load', function() { var s = document.createElement('script'); s.addEventListener('load', function() { var sheep = new eSheep(); sheep.Start(); }); s.setAttribute('src', 'https://adrianotiger.github.io/web-esheep/dist/esheep.min.js'); document.getElementsByTagName('head')[0].appendChild(s); }); })(); ">Sheep</a></p>

``` js
(function() {
    'use strict';
    window.addEventListener("load", function() {
      var s = document.createElement("script");
      s.addEventListener("load", function() {
          var sheep = new eSheep(); 
          sheep.Start(); 
      });
      s.setAttribute("src", "https://adrianotiger.github.io/web-esheep/dist/esheep.min.js");
      document.getElementsByTagName('head')[0].appendChild(s);
    });
})();
```

<p><a href="javascript:h=['nitter.it','nitter.snopyta.org','nitter.net'];window.location.host=h[Math.floor(Math.random()*h.length)]; ">Nitter</a></p>

``` js
javascript:h=['nitter.it','nitter.snopyta.org','nitter.net'];window.location.host=h[Math.floor(Math.random()*h.length)];
```
