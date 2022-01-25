# Resume

Ways to create a CV/resume.

## Links

Inspiring tools/templates:

- <https://www.canva.com/search/templates?q=resume>

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
