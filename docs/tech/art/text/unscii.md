# Unscii

[Unscii](https://github.com/viznut/unscii) (a portmanteau of Unicode and ASCII) is a set of bitmapped fonts. Unlike the smoothed, vector-based fonts we use in web browsers or word processors, [Unscii](http://viznut.fi/unscii/) is pixel-perfect.

It comes in ![_unscii.7z](two main flavors):

- Unscii-8: 8×8 pixels per glyph (classic low-res feel).
- Unscii-16: 8×16 pixels per glyph (taller, more like a VGA text mode).

While its primary goal is to support character cell art, it is also highly legible, making it a surprisingly comfortable choice for programming or terminal use if you enjoy a retro aesthetic.

## ASCII vs. ANSI vs. Unscii

To understand why Unscii is special, we have to distinguish it from the other terms often thrown around in the text art community.

1. ASCII (The Character Set)
ASCII is strictly the content. It is a 7-bit standard that defines letters, numbers, and basic symbols (@, #, /).

The Art Style: "ASCII Art" usually refers to pictures made only using these standard keyboard characters.

The Limitation: You can't draw solid boxes or seamless lines because standard ASCII doesn't contain those shapes.

2. ANSI (The Styling)
ANSI usually refers to escape codes used to control the terminal. It tells the computer "make this text red" or "move the cursor to row 10."

The Art Style: "ANSI Art" (popular in the BBS era) uses specific block characters (like █, ▀, ▄) combined with coloring codes.

The Problem: ANSI art relies on the computer using a specific "Code Page" (usually CP437). If you view an old ANSI art file in a modern Unicode terminal without the right font, the boxes might break, or the line-drawing characters might turn into question marks.

3. Unscii (The Visual Bridge)
Unscii is the font that solves the rendering problem. It takes those specific block characters used in ANSI art, old Commodore 64 (PETSCII) graphics, and Teletext, and maps them to modern Unicode locations.

In short: Unscii ensures that the specific pixel patterns of the past render correctly on modern operating systems.
