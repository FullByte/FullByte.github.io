# Pandoc

| What          | Where                 |
|---------------|-----------------------|
| Official Page | <https://pandoc.org/> |
| Source        |                       |
| Download      |                       |
| Install       |                       |

Additional tools:

- miktex for pdf conversion from LaTeX <https://miktex.org/>

## Markdown

Convert markdowns files passed as arguments into different formats and saves them into a separate folder

```cmd
set list=docx html rst odt rtf epub pdf
for %%x in (%*) do (
    mkdir output   
    mkdir output\\%%~nx
    for %%e in (%list%) do ( 
        mkdir output\\_%%e 
        pandoc %%x -o output/_%%e/%%~nx.%%e
        pandoc %%x -o output/%%~nx/%%~nx.%%e
    )
    mkdir output\\_md
    copy %%x output\_md\
    copy %%x output\%%~nx\
)
```

### Slideshow

Slidshow using revealjs

``` sh
pandoc -s -t revealjs slides.md -o slides.html
```

Slidshow using slidy

``` sh
pandoc -s -t slidy slides.md -o slides.html
```

## Docx

Note, that you can sometimes export the source e.g. Google Docs as "doxc" file.

First step is to convert the docx file to epub which is just a zipped version of a static website

``` sh
FILE="title.docx"
pandoc -s "$FILE" -t epub --epub-chapter-level=2 -o all.epub
unzip -q "all.epub" -d . && rm "all.epub"
```

Run a webserver serviing directory EPUB/ and navigate to "<path>/nav.xhtml" to see result.

Optionally, create HTML files and use a theme e.g. by using a static website generator like mkdocs, which is great for books and documentation.

``` sh
pip install mkdocs
mkdocs new my-project
cd my-project
```

Add a theme and some information to the ```mkdocs.yml```.
Copy all files from the text folder of the epub unzip to the static websites docs folder and create the static website with

``` sh
mkdocs build
```

Clean by removing unwanted chars/content e.g.:

- Remove bookmarks: ```sed -i '' 's/{#.*}$//g' text/*.md```
- Remove lines that starts with `:::`: ```sed -i '' '/^:::/d' text/*.md```
