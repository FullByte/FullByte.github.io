# Firefox

| What          | Where                                                      |
|---------------|------------------------------------------------------------|
| Official Page | <https://www.mozilla.org/en-US/firefox/browsers>          |
| Source        | <https://hg.mozilla.org/mozilla-central/>                  |
| Download      | <https://www.mozilla.org/en-US/firefox/download>          |
| Docs          | <https://developer.mozilla.org/en-US/docs/Mozilla/Firefox> |
| Windows       | `choco install firefox`                                |
| Ubuntu        | `sudo apt -y install firefox`                          |

## Firefox remote debugging

- Enable Developer options on your phone
- Enable Remote debugging via USB in your mobile browser settings
- Connect device with USB
- Visit about:debugging in your PC browser
- Press connect next to your device
- Select your device and press Inspect on your desired tab

## Bookmarks

- Toggle Bookmarks: Ctrl + Shift + B
- Add all open tabs to bookmark folder: Right clock on a tab, mark all tabs, save tabs as bookmark, provide folder name

## Addons

- uBlock Origin
- Privacy Badger
- ghostery

## Script Bookmarks

- <p><a title="bullshit" href="javascript:(function(){var d=document,s=d.createElement('script');s.crossOrigin='anonymous';s.src='https://unpkg.com/@mourner/bullshit@1.3.0/bullshit.js';d.body.appendChild(s);}())">Bullshit Detector</a>
- <p><a title="Censor" href="javascript:(function (dummyze, entry) {function textWalker(node, cbck) {var i = -1,n, s, w, h;if (!node) {return}if (node.nodeType === 3) {cbck(node, 'nodeValue');return}if (node.tagName == 'IFRAME') {try {textWalker(node.contentDocument.documentElement, cbck)} catch (e) {}return}if (node.tagName == 'STYLE' || node.tagName == 'SCRIPT' || node.tagName == 'SVG') {return}if (node.tagName == 'IMG') {s = getComputedStyle(node);node.src = 'https://dummyimage.com/' + (parseInt(s.width) || 10) + 'x' + (parseInt(s.height) || 10);return}if (node.tagName == 'INPUT' || node.tagName == 'TEXTAREA') {cbck(node, 'placeholder');cbck(node, 'value');return}if (node.tagName) {if ((s = node.getAttribute('style')) &amp;&amp; (s = (s = getComputedStyle(node)).backgroundImage) &amp;&amp; (s != 'none') &amp;&amp; (s = (s.match(/url\(&quot;([^&quot;]+)&quot;\)/))) &amp;&amp; (s = s[1])) {pic = new Image();pic.onload = function () {node.style.backgroundImage = 'url(https://dummyimage.com/' + (parseInt(pic.width) || 10) + 'x' + (parseInt(pic.height) || 10) + ')'};pic.src = s;}if ((b = (b = getComputedStyle(node, '::before')).content) &amp;&amp; (b != 'none') &amp;&amp; b.indexOf('attr(') == 0 &amp;&amp; (b = b.match(/^attr\((.*?)\)$/)) &amp;&amp; (b = b[1])) {cbck(node, b);}if ((b = (b = getComputedStyle(node, '::after')).content) &amp;&amp; (b != 'none') &amp;&amp; b.indexOf('attr(') == 0 &amp;&amp; (b = b.match(/^attr\((.*?)\)$/)) &amp;&amp; (b = b[1])) {cbck(node, b);}while (n = node.childNodes[++i]) textWalker(n, cbck);}};textWalker(entry, dummyze)})(function (n, p, a, w, pic) {p = p || 'nodeValue';a = n[p];if (a) {w = a.replace(/\S/g, '\u2591');if (a != w) n[p] = w} else {a = n.getAttribute &amp;&amp; n.getAttribute(p);if (a) {w = a.replace(/\S/g, '\u2591');if (a != w) n.setAttribute(p, w);}}}, document.documentElement);">Censor</a>
</p>
- <p><a href="javascript:(function() { 'use strict'; window.addEventListener('load', function() { var s = document.createElement('script'); s.addEventListener('load', function() { var sheep = new eSheep(); sheep.Start(); }); s.setAttribute('src', 'https://adrianotiger.github.io/web-esheep/dist/esheep.min.js'); document.getElementsByTagName('head')[0].appendChild(s); }); })(); ">Sheep</a></p>
- <p><a href="javascript:(function(){window.open('https://home.omg.lol/address/yolo/statuslog-bookmarklet?title='+document.title+'&url='+document.location.href,'status.lol','width=700,height=670')})();">Post on OMG LOL</a></p>
