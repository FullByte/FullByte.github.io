# Office

## Excel

Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

### Random

Find double entries

``` xlsx
=IF(MATCH(A2;A:A;0)=ROW();"";"Double")
```

Create a Sierpinski triangle

Add "1" in field "V1" and copy the formula down and to the sides:

``` xlsx
=WENN(SUMME(U1:W1)=1;1;"")
```

### Settings

Define number format

``` xlsx
Selection.NumberFormat = "#,##0_ ;-#,##0 "
```

Turn off aAlerts

``` xlsx
Application.DisplayAlerts = False
```

AutoFit

``` xlsx
Worksheets(Customer).Columns("A:X").EntireColumn.AutoFit
```

### Chart Trendline Formulas

When you add a trendline to a chart, Excel provides an option to display the trendline equation in the chart. This tip describes how to create formulas that generate the trendline coefficients. You can then use these formulas to calculate predicted y values for give values of x. These equations assume that your sheet has two named ranges: x and y.

Linear Trendline

``` xlsx
Equation: y = m * x + b
m: =SLOPE(y,x)
b: =INTERCEPT(y,x)
```

Logarithmic Trendline

``` xlsx
Equation: y = (c * LN(x)) + b
c: =INDEX(LINEST(y,LN(x)),1)
b: =INDEX(LINEST(y,LN(x)),1,2)
```

Power Trendline

``` xlsx
Equation: y=c*x^b
c: =EXP(INDEX(LINEST(LN(y),LN(x),,),1,2))
b: =INDEX(LINEST(LN(y),LN(x),,),1)
```

Exponential Trendline

``` xlsx
Equation: y = c *e ^(b * x)
c: =EXP(INDEX(LINEST(LN(y),x),1,2))
b: =INDEX(LINEST(LN(y),x),1)
```

2nd Order Polynomial Trendline

``` xlsx
Equation: y = (c2 * x^2) + (c1 * x ^1) + b
c2: =INDEX(LINEST(y,x^{1,2}),1)
C1: =INDEX(LINEST(y,x^{1,2}),1,2)
b = =INDEX(LINEST(y,x^{1,2}),1,3)
```

3rd Order Polynomial Trendline

``` xlsx
Equation: y = (c3 * x^3) + (c2 * x^2) + (c1 * x^1) + b
c3: =INDEX(LINEST(y,x^{1,2,3}),1)
c2: =INDEX(LINEST(y,x^{1,2,3}),1,2)
C1: =INDEX(LINEST(y,x^{1,2,3}),1,3)
b: =INDEX(LINEST(y,x^{1,2,3}),1,4)
```

## OBS

Info

|What|Where|
|-|-|
|Official Page||
|Source||
|Download||
|Install||

### Links

OBS+Restream=free multi-platform streaming

- OBS: <https://obsproject.com/>
- Restream: <https://restream.io>
- VR Streaming <https://github.com/baffler/OBS-OpenVR-Input-Plugin>
- StreamFX: <https://github.com/Xaymar/obs-StreamFX/releases>
- Inpput overlay <https://github.com/univrsal/input-overlay>
- OBS-virtual-cam: <https://github.com/CatxFish/obs-virtual-cam>

### General Settings

TODO

### OBS-virtual-cam

To put them together you have to:

- Follow guide from <https://github.com/CatxFish/obs-virtual-cam>
- Open OBS -> Tools -> v4l2 Video Output -> select "Start"
- Go to the audio/video settings of the vidconf software and select the new video device
- Select new virtual cam from video conferencing tool you use.

## Draw.io

Info

| What          | Where                        |
|---------------|------------------------------|
| Official Page |                              |
| Source        |                              |
| Download      |                              |
| Install       |                              |
| Online        | <https://app.diagrams.net/>> |

### Create and edit SVG in vscode

Create and edit SVG files nativly in VSCoode with Draw.io with a draw.io extension:

1. [Install](vscode:extension/hediet.vscode-drawio) the [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) for [Visual Studio Code](https://code.visualstudio.com/) by [Henning Dieterichs](https://marketplace.visualstudio.com/publishers/hediet)
2. Create a new file called whatever.drawio.svg
3. Open the file in VScode and the draw.io extension should pop-up an enable editing.
4. Link the SVG file to e.g. a markdown or web document

Example file showing the process:

![vscode_drawio](_example.drawio.svg)

### Create a mockup

Draw.io enables quick an easy mockup creation for simple GUI interfaces.
The possiblities are limited but it is an excellent first mockup draft method to figure out what you need.

Add the mockup shapes:

- Open Shapes
- click on "More Shapes"
- Navigate to Software -> Mockups
- Add Mockups

Create your first page. Use that design as a template for further pages.
Create a link to other pages for specific buttons.

Export as HTML to demo the mockup online/offline.
