# JS Snippets

## Detect Missing AdBlocker

Shows a message based on whether the user is running an ad blocker.

``` html
<html>
<head>
    <title>Example</title>
    <meta charset="UTF-8">
    <script type="module" src="./detect-missing-adblocker.js"></script>
</head> 
<body>
        <detect-missing-adblocker>
        </detect-missing-adblocker>
</html>
```

The `detect-missing-adblocker.js` looks like this:

``` js
class DetectMissingAdBlocker extends HTMLElement {
  constructor() {
    super();
    this.note = null;
    this.successNote = null;
  }

  connectedCallback() {
    this.ensureMarkup();
    this.note = this.querySelector('#ftf-dma-note');
    this.successNote = this.querySelector('#ftf-dma-success');
    this.hideAll();
    this.detectAdblocker().then((hasAdblocker) => {
      if (hasAdblocker) this.showSuccess(); else this.showNotice();
    });
  }

  ensureMarkup() {
    const hasNote = this.querySelector('#ftf-dma-note');
    const hasSuccess = this.querySelector('#ftf-dma-success');
    if (hasNote && hasSuccess) return;
    this.innerHTML = `
      <div id="ftf-dma-note" style="display:none;">
        <slot name="message">This site doesn't display ads to protect your privacy but please consider using an ad blocker to protect your privacy.</slot>
      </div>
      <div id="ftf-dma-success" style="display:none;">
        <slot name="success">Congrats for using an ad blocker! This site doesn't display ads to protect your privacy.</slot>
      </div>`;
  }

  detectAdblocker() {
    return new Promise((resolve) => {
      let blocked = false;
      const bait = document.createElement('div');
      bait.className = 'adsbox ad-banner ad_unit ad-banner-top sponsor adsbygoogle';
      bait.style.cssText = 'position:absolute; left:-9999px; width:1px; height:1px;';
      document.body.appendChild(bait);
      const checkBait = () => {
        const b = window.getComputedStyle(bait);
        const isBlocked = b.display === 'none' || b.visibility === 'hidden' || bait.offsetParent === null || bait.offsetHeight === 0;
        bait.remove();
        blocked = blocked || isBlocked;
      };
      const script = document.createElement('script');
      script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js';
      script.async = true;
      script.type = 'text/javascript';
      const finish = () => resolve(blocked);
      script.onerror = () => { blocked = true; script.remove(); finish(); };
      script.onload = () => { script.remove(); finish(); };
      const timeout = window.setTimeout(() => { script.remove(); finish(); }, 1200);
      window.setTimeout(() => { checkBait(); document.body.appendChild(script); }, 100);
      const origResolve = resolve;
      resolve = (value) => { window.clearTimeout(timeout); origResolve(value); };
    });
  }

  showSuccess() { this.hideAll(); if (this.successNote) this.successNote.style.display = 'block'; }
  showNotice() { this.hideAll(); if (this.note) this.note.style.display = 'block'; }
  hideAll() { if (this.note) this.note.style.display = 'none'; if (this.successNote) this.successNote.style.display = 'none'; }
}

customElements.define('detect-missing-adblocker', DetectMissingAdBlocker);
export { DetectMissingAdBlocker as default };
```
