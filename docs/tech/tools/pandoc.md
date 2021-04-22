# Pandoc

## Info

|What|Where|
|-|-|
|Official Page|<https://pandoc.org/>|
|Source||
|Download||
|Install||

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
