# Markdown

``` txt
#######   ,#####. .#####.
  ###    ########.########
  ###    #################
  ###    `###############'
  ###     `#############'
  ###       `#########'
  ###         `#####'
#######         `#'

####     ####     ###
#####   #####     ###
######.######     ###
### ##### ###     ###
###  ###  ###   #######
###   #   ###    #####
###       ###     ###
###       ###      #
```

## Basic Markdown Formatting

### Headings

    # This is an <h1> tag
    ## This is an <h2> tag
    ### This is an <h3> tag
    #### This is an <h4> tag
    ##### This is an <h5> tag
    ###### This is an <h6> tag
    
### Emphasis

    *This text will be italic*
    _This will also be italic_
    
    **This text will be bold**
    __This will also be bold__
    
    _You **can** combine them_
    
Result:

*This text will be italic*

_This will also be italic_

**This text will be bold**

__This will also be bold__

_You **can** combine them_

### Lists

**Inordered:**

    * Milk
    * Bread
        * Wholegrain
    * Butter

Result:

* Milk
* Bread
    * Wholegrain
* Butter

**Ordered:**

    1. Tidy the kitchen  
    2. Prepare ingredients  
    3. Cook delicious things

Result:

1. Tidy the kitchen  
2. Prepare ingredients  
3. Cook delicious things

### Images

    ![Alt Text](url)

Result:

![m'lady](http://i.imgur.com/v8IVDka.jpg)

### Links

    [link](http://example.com)

Result:

[link](http://example.com)

### Blockquotes

    As Kanye West said:

    > We're living the future so
    > the present is our past.

Result:

As Kanye West said:
> We're living the future so
> the present is our past.

### Horizontal Rules

    ---

Result:

---

### Code Snippets

    Indenting by 4 spaces will turn an entire paragraph into a code-block.

Result:

    .my-link {
        text-decoration: underline;
    }

### Reference Lists & Titles

    **The quick brown [fox][1], jumped over the lazy [dog][2].**

    [1]: https://en.wikipedia.org/wiki/Fox "Wikipedia: Fox"
    [2]: https://en.wikipedia.org/wiki/Dog "Wikipedia: Dog"

Result:

**The quick brown [fox][1], jumped over the lazy [dog][2].**

[1]: https://en.wikipedia.org/wiki/Fox "Wikipedia: Fox"
[2]: https://en.wikipedia.org/wiki/Dog "Wikipedia: Dog"

### Escaping

    \*literally\*

Result:

\*literally\*

### Embedding HTML

    <button class="button-save large">Big Fat Button</button>

Result:

<button class="button-save large">Big Fat Button</button>

## Advanced Markdown

Note: Some syntax which is not standard to native Markdown. They're extensions of the language.

### Strike-throughs

    ~~deleted words~~

Result:

~~deleted words~~

### Highlights

Work in [Ghost](https://ghost.org/):

    ==oooh fancy==

Result:

==oooh fancy==

### Automatic Links

    https://ghost.org

Result:

https://ghost.org

### Markdown Footnotes

Work in [Ghost](https://ghost.org/):

    The quick brown fox[^1] jumped over the lazy dog[^2].

    [^1]: Foxes are red
    [^2]: Dogs are usually not red

Result:

The quick brown fox[^1] jumped over the lazy dog[^2].

[^1]: Foxes are red
[^2]: Dogs are usually not red

## GitHub Flavored Markdown

### Syntax Highlighting

    ```javascript
    function fancyAlert(arg) {
      if(arg) {
        $.facebox({div:'#foo'})
      }
    }
    ```

Result:

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```

### Task Lists

    - [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
    - [x] list syntax required (any unordered or ordered list supported)
    - [x] this is a complete item
    - [ ] this is an incomplete item

Result:

- [x] @mentions, #refs, [links](), **formatting**, and <del>tags</del> supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

### Tables

You can create tables by assembling a list of words and dividing them with hyphens `-` (for the first row), and then separating each column with a pipe `|`:

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

### SHA references

Any reference to a commit’s SHA-1 hash will be automatically converted into a link to that commit on GitHub.

    16c999e8c71134401a78d4d46435517b2271d6ac
    mojombo@16c999e8c71134401a78d4d46435517b2271d6ac
    mojombo/github-flavored-markdown@16c999e8c71134401a78d4d46435517b2271d6ac

### Issue references within a repository

Any number that refers to an Issue or Pull Request will be automatically converted into a link.

    #1
    mojombo#1
    mojombo/github-flavored-markdown#1

### Username @mentions

Typing an `@` symbol, followed by a username, will notify that person to come and view the comment. This is called an “@mention”, because you’re mentioning the individual. You can also @mention teams within an organization.

### Emoji

GitHub supports emoji! Check out the [Emoji Cheat Sheet](http://www.emoji-cheat-sheet.com/).

## Markdown Interpreters

### mkdocs

todo

### Mermaid

JavaScript based diagramming and charting tool that renders Markdown-inspired text definitions to create and modify diagrams dynamically.

https://mermaid.js.org/

### Argdown

A simple syntax for complex argumentation

- Docs: <https://argdown.org/>
- Source: <https://github.com/christianvoigt/argdown>
- VS Code Extension: <https://marketplace.visualstudio.com/items?itemName=christianvoigt.argdown-vscode>
- CLI Tool: ```npm install -g @argdown/cli```
