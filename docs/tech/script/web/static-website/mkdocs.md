# mkdocs

[MkDocs](https://github.com/mkdocs/mkdocs/) is a great way to host a simple, static website. This website uses [Material for MkDocs](https://github.com/squidfunk/mkdocs-material). Material for MkDocs is a theme for MkDocs, a static site generator geared towards (technical) project documentation.

## Hosting

Use docker or python to quickly create and host a static website.

### Container

```shell
git clone https://github.com/FullByte/FullByte.github.io.git # clone repo
cd FullByte.github.io # Go to main folder
docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material # run the container
```

### Python

Run this once to install all requirements:

```shell
choco install -y python
python -m pip install --upgrade pip
pip install mkdocs
pip install mkdocs-material
```

Run this in the folder of the mkdocs.yml file to host the mkdocs page:

```shell
mkdocs serve
```

Currently Mkdocs does not yet support 3.9.x. This may change soon and be outdated, however the general problem of having different python versions installed may still be relevant. To solve the problem, [download](https://www.python.org/downloads/) and install the latest supported python version e.g. 3.8.x.

In case you have multiple python versions installed (like me) you need to explicitly mention to use 3.8.x! Run ```py –list``` to get your 3.8.x version. Mine is -3.8-64; your version may vary. Run this to install the mkdocs dependencies:

```shell
py -3.8-64 -m pip install --upgrade pip --user
py -3.8-64 -m pip install mkdocs
py -3.8-64 -m pip install --upgrade mkdocs-material
```

Then run this in the main folder with mkdocs.yml file

```shell
py -3.8-64 -m mkdocs serve
```

## Create page

### Extensions

[MKdocs-material](https://squidfunk.github.io/mkdocs-material/) is a [great theme](https://squidfunk.github.io/mkdocs-material/setup/changing-the-colors/) and comes [integrated](https://squidfunk.github.io/mkdocs-material/reference/abbreviations/) with the [pymkdown extensions](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/), which lets you add tabbed code blocks, progress bars, task lists, keyboard symbols and more.

Further plugins:

- [mkdocs-minify-plugin](https://github.com/byrnereese/mkdocs-minify-plugin): `pip install mkdocs-minify-plugin`
- [mkdocs-redirects](https://github.com/datarobot/mkdocs-redirects): `pip install mkdocs-redirects`

### Examples

Checkable List

```yaml
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
