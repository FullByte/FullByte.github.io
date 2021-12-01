# CSS

## Links

Lern CSS

- <https://web.dev/learn/css/>

CSS Tools

- <http://www.patternify.com/>
- <http://layerstyles.org/builder.html>
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

## CSS Examples

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
