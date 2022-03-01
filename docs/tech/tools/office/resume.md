# Resume

Ways to create a CV/resume.

## Links

Inspiring tools/templates:

- <https://www.canva.com/search/templates?q=resume>
- <https://jsonresume.org/themes/>

## JSON Resume

[JSON Resume](https://jsonresume.org) is an open source solution to create a JSON-based standard for resumes. Create a HTML or PDF output using the [CLI](https://github.com/jsonresume/resume-cli). Use a different theme without changing anything in the resume file.

- Install: ```npm i resume-cli``` or use remotly with ```npx resume```
- Create initial json file: ```resume init```
- Edit `resume.json` and validate with resume validate: ```resume validate```
- Create a PDF: ```resume export resume.pdf```
- Create a HTML file: ```resume export resume.html```
- Host HTML file: ```resume serve```

To use other [themes](https://jsonresume.org/themes/) browse and select what you prefer (and follow their config/install doc.)

Example for theme [kendall](https://github.com/LinuxBozo/jsonresume-theme-kendall):

``` bash
cd ~/path/to/resume/
git clone https://github.com/LinuxBozo/jsonresume-theme-kendall
cp resume.json /jsonresume-theme-kendall/resume.json
cd jsonresume-theme-kendall
npm install
resume export resume.pdf --theme .
resume export resume.html --theme .
resume serve --theme .
```

## Man page + curl

Create a [Linux manual page formated](https://www.man7.org/linux/man-pages/man7/man.7.html) file which can be downloaded and intepreted using the [man](https://www.kernel.org/doc/man-pages/) command.

I created a markdown file and converted it using [pandoc](https://pandoc.org/). Use [definition-lists](https://pandoc.org/MANUAL.html#definition-lists) and [metadata-blocks](https://pandoc.org/MANUAL.html#metadata-blocks) to pimp the file if you like (not really needed for our incentive of creating a CV)

Convert the file as follows

``` pandoc
pandoc --standalone --to man cv.md -o cv.7
```

To read the created man page simply run: ```man cv.7```

If the file is hosted online run the following command to read the file:

- Windows: use [groff](https://www.gnu.org/software/groff/#downloading) or [mandoc](https://embedeo.org/ws/doc/man_windows/) or simply install WSL and follow Linux command below.
- Linux: ```man <( curl -sL https://cv.example.com/cv.7 )```
- MacOS: ```curl -sL https://cv.example.com/cv.7 > /tmp/cv.7; man /tmp/cv.7```

I uploaded my `cv.7` file to <https://cv.fromm.rocks/cv.7>. Access to subdomain "cv" is password protected using htaccess.

In order to access the password protected file we need to run curl as follows: ```curl -u username:password https://cv.example.com```

Alternativly it is also possible to use wget: ```wget --http-user=username --http-password=password http://cv.example.com```

Combine this with the command and we have a one-liner to read a cv using `man` :)

- Linux: ```man <( curl -u "user":"password" -sL https://cv.example.com/cv.7 )```
- MacOS: ```curl -u "user":"password" -sL https://cv.example.com/cv.7 > /tmp/cv.7; man /tmp/cv.7```
