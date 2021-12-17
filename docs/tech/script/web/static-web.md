# Static Site Generators

## Signal (Image Gallery)

[Sigal](http://sigal.saimon.org) is a simple static **gallery** generator.

Getting started

Create the config file:

 ``` sh
sigal init
```

Edit the config file...

Then run the build command

 ``` sh
sigal build
```

## thumbsup (Video and Image Gallery)

[Thumbsup](https://github.com/thumbsup/thumbsup) is a Video and Image Gallery but i prefer Signal for images. Thumbsup works great with videos. Read the [documentation](https://thumbsup.github.io/docs/) for details. To get started:

**Requirements**

Option 1: Install on machine

 ``` sh
# Install Nodejs and NPM
# Install GraphicsMagick
npm install -g thumbsup
```

Option 2: Run Docker

 ``` sh
docker run -t -v /Volumes/photos:/input:ro -v "$(pwd)/website:/output" -u $(id -u):$(id -g) ghcr.io/thumbsup/thumbsup thumbsup --input /input --output /output
```

**New Gallery**

Create a new Gallery in subfolder `gallery` from subfolder `source`:

 ``` sh
thumbsup --input ./source --output ./gallery
```

## MkDocs

[MkDocs](https://github.com/MkDocs/MkDocs/) is a great way to host a simple, static website. This website uses [Material for MkDocs](https://github.com/squidfunk/MkDocs-material). Material for MkDocs is a theme for MkDocs, a static site generator geared towards (technical) project documentation.

Use docker or python to quickly create and host a static website:

### Host MkDocs locally with docker

 ``` sh
git clone https://github.com/FullByte/FullByte.github.io.git # clone repo
cd FullByte.github.io # Go to main folder
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/MkDocs-material # run the container
```

### Serve MkDocs locally with python

Run this once to install all requirements:

 ``` sh
choco install -y python
python -m pip install --upgrade pip
pip install MkDocs
pip install MkDocs-material
```

Run this in the folder of the MkDocs.yml file to host the MkDocs page:

 ``` sh
MkDocs serve
```

### Create page

TODO

#### Extensions

[MkDocs-material](https://squidfunk.github.io/MkDocs-material/) is a [great theme](https://squidfunk.github.io/MkDocs-material/setup/changing-the-colors/) and comes [integrated](https://squidfunk.github.io/MkDocs-material/reference/abbreviations/) with the [pymkdown extensions](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/), which lets you add tabbed code blocks, progress bars, task lists, keyboard symbols and more.

Further plugins:

- [MkDocs-minify-plugin](https://github.com/byrnereese/MkDocs-minify-plugin): `pip install MkDocs-minify-plugin`
- [MkDocs-redirects](https://github.com/datarobot/MkDocs-redirects): `pip install MkDocs-redirects`

#### Examples

Checkable List

``` yaml
markdown_extensions:
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tasklist:
      clickable_checkbox: true
```

=== "List"

    * [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
    * [ ] Vestibulum convallis sit amet nisi a tincidunt
        * [x] In hac habitasse platea dictumst
        * [x] In scelerisque nibh non dolor mollis congue sed et metus
        * [ ] Praesent sed risus massa
    * [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque

=== "Markdown"

    ``` md
    * [x] Lorem ipsum dolor sit amet, consectetur adipiscing elit
    * [ ] Vestibulum convallis sit amet nisi a tincidunt
        * [x] In hac habitasse platea dictumst
        * [x] In scelerisque nibh non dolor mollis congue sed et metus
        * [ ] Praesent sed risus massa
    * [ ] Aenean pretium efficitur erat, donec pharetra, ligula non scelerisque
    ```

Lazy load a picutre:

![Placeholder](https://dummyimage.com/600x400/eee/aaa){ loading=lazy }
