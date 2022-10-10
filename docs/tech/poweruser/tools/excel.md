# Excel

Info

| What          | Where |
|---------------|-------|
| Official Page |       |
| Source        |       |
| Download      |       |
| Install       |       |

## Random

Find double entries

``` xlsx
=IF(MATCH(A2;A:A;0)=ROW();"";"Double")
```

Create a Sierpinski triangle

Add "1" in field "V1" and copy the formula down and to the sides:

``` xlsx
=WENN(SUMME(U1:W1)=1;1;"")
```

## Settings

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

## Chart Trendline Formulas

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
