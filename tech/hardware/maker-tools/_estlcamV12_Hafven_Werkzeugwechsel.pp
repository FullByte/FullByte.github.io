Version=12123
Length unit CNC=mm
Feed unit CNC=mm_min
File extension=ngc
External postprocessor=
Use arcs=yes
I/J relative=yes
Program start=
[>>>]
(Projekt <project>)
(Erstellt mit Estlcam <build>)
(Laufzeit ca. <time> Stunden)

(Benötigte Werkzeuge:)
<tools>

(Projekt <project>)
(Erstellt mit Estlcam Version <version> Build <build>)
(Laufzeit ca. <time> Stunden)

(Benötigte Werkzeuge:)
<tools>
G64 P0.1
G90
M06 T<t> (<n>)
M03 S<s>
[<<<]
Program end=
[>>>]


M05
M30
[<<<]
Operation start=
[>>>]

(Nr. <order> <op>: <name>)
[<<<]
Tool change=
[>>>]
M05
M06 T<t> (<n>)
M03 S<s><!L>
[<<<]
Laser before down=
Laser after down=M03 S<s>
Laser before up=M05
Laser after up=
Mist coolant on=M08
Mist coolant off=M09
Flood coolant on=M10
Flood coolant off=M11
Name X=X
Format X=
Order X=2
Scale X=1
Enable X=yes
Repeat X=no
Name Y=Y
Format Y=
Order Y=3
Scale Y=1
Enable Y=yes
Repeat Y=no
Name Z=Z
Format Z=
Order Z=4
Scale Z=1
Enable Z=yes
Repeat Z=no
Name I=I
Format I=
Order I=5
Scale I=1
Enable I=yes
Repeat I=yes
Name J=J
Format J=
Order J=6
Scale J=1
Enable J=yes
Repeat J=yes
Name F=F
Format F=
Order F=7
Scale F=1
Enable F=yes
Repeat F=no
Name S=S
Format S=
Order S=8
Scale S=1
Enable S=yes
Repeat S=no
Name N=
Format N=
Order N=1
Scale N=1
Enable N=no
Repeat N=no
Plot axis Z=no
Up Z=
Down Z=
Rapid feed XY=
Rapid feed Z=
Initial value N=1
Command rapid move=G00
Command linear move=G01
Command clockwise arc=G02
Command counterclockwise arc=G03
Command order=1
Command repeat=yes
Encoder=ASCII
Delimiter= 
Decimal point=.
Line end=
Character replacements=
[>>>]
Ä|Ae
Ö|Oe
Ü|Ue
ä|ae
ö|oe
ü|ue
ß|ss
[<<<]
Lock units=no
Special formatter=Off
EOL=19FE38C0AB207ED8
