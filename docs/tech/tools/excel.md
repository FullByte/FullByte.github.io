# Excel

Info

| What      | Where                                                                                                          |
| --------- | -------------------------------------------------------------------------------------------------------------- |
| Online    | <https://www.office.com/launch/excel>                                                                          |
| Docs      | <https://support.microsoft.com/de-de/excel>                                                                    |
| Functions | <https://support.microsoft.com/en-us/office/excel-functions-alphabetical-b3944572-255d-4efb-bb96-c6d90033e188> |

[Translate Excel Formaulas](https://en.excel-translator.de/translator/) form one language to another.

![clippy](_clippy.svg)

## Random

Find double entries

``` xlsx
=WENN(VERGLEICH(A1;A:A;0)=ZEILE();"Einfacher Eintrag";"Mehrere Einträge")
=IF(MATCH(A1;A:A;0)=ROW();"Single entry";"Multiple entries")
```

Create a Sierpinski triangle

Add "1" in field "V1" and copy the formula down and to the sides:

``` xlsx
=WENN(SUMME(U1:W1)=1;1;"")
=IF(SUM(U1:W1)=1,1,"")
```

Extract first name from email:

``` xlsx
=LINKS(LINKS(A1;FINDEN(".";A1)-1);FINDEN("@";A1)-1)
=LEFT(LEFT(A1,FIND(".",A1)-1),FIND("@",A1)-1)
```

Extract last name from email:

``` xlsx
=LINKS(RECHTS(A1;LÄNGE(A1)-FINDEN(".";A1));FINDEN("@";RECHTS(A1;LÄNGE(A1)-FINDEN(".";A1)))-1)
=LEFT(RIGHT(A1,LEN(A1)-FIND(".",A1)),FIND("@",RIGHT(A1,LEN(A1)-FIND(".",A1)))-1)
```

Extract full name from email:

``` xlsx
=WECHSELN((LINKS(A1;FINDEN("@";A1)-1));".";" ")
=SUBSTITUTE((LEFT(A1,FIND("@",A1)-1)),"."," ")
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
