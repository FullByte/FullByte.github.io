# Protest

It is not easy to protest in a smart and effective way. In my opinion strikes, demonstrations, letter-writing campaigns, petitions, sit-ins and occupation are not very effective nor creative. Of course one can passively boycott whatever thing to not support and tell friends about what and why not to support but this is boring and small minded as well. Here are some examples and ideas how to protest on a given matter in an interesting, not annoying and creative way while being effective and successful:

- [Ugly Gerry](https://fontsarena.com/ugly-gerry/) is a [free font](_gerry.otf.zip) created with real US congressional districts. The name comes from gerrymandering, the process that made possible such weird shapes.

- [Volkswagen](https://github.com/auchenberg/volkswagen) can be integrated in your CI process. It detects when your tests are being run in a CI server, and makes them pass. Volkswagen uses a defeat device to detect when it's being tested in a CI server and will automatically reduce errors to an acceptable level for the tests to pass. This will allow you to spend less time worrying about testing and more time enjoying the good life as a trustful software developer.

- The creative ways the [DeCSS](https://en.wikipedia.org/wiki/DeCSS) crack was distributed (e.g. [t-shirt](_decss_tshirt.webp), [haiku](_decss-haiku.txt) or [midi](_decss-auth.mid), [audio](_decss_descramble.mp3), [html dvd logo](_decss-dvdlogo.html.txt) and [many more](https://www.cs.cmu.edu/~dst/DeCSS/Gallery/)...). Later works by "removing all the white space, then transforming each ASCII character into a single 32nd note of its midi equivalent (midi notes, like ASCII characters, are coded into values ranging from 1 to 127.)".

- Address your issues to the correct people. If you work in a social or public based service make sure to create awareness but don't let uninvolved suffer from your problems. For example if you drive a bus, let passengers ride for free and let them know you are protesting instead of not driving and letting people down.

- Make art (music, pictures, games) that help people understand the problem. Make things that are understandable as well as entertaining, interesting, provocative and/or beautiful. This will address the problem in an entertaining but critical way that is not annoying and will be much more likely be shared, discussed and addressed.

- Find ways to educate the public about the core issue of your protest and what needs to be done. Reflect on your issue and make sure this is not just an opinion but actual facts that can be educated.

- Never interrupt your enemy when he/she is making a mistake.

## Munitions T-shirt

The “Munitions T-shirt” refers to a 1990s protest in which a working RSA encryption program, written in a few lines of Perl, was printed on a T-shirt. At the time, US export laws classified strong cryptographic software as “munitions,” similar to weapons, meaning that sharing such code internationally could be restricted or even illegal. The shirt highlighted the absurdity of this by effectively turning wearable clothing into a supposed export-controlled weapon. It not only displayed the code in text form but also encoded it as a scannable barcode, making it functionally usable. The design often included legal warnings and excerpts from regulations like ITAR to emphasize the point. The project aimed to challenge these restrictions and argue that code is a form of free speech, exposing inconsistencies in how information was regulated. After US crypto laws were relaxed in 1999, the shirt became mainly a historical symbol of the broader struggle between technology, law, and freedom of expression.

RSA code examples:

``` perl
#!/usr/local/bin/perl -s
do 'bigint.pl';($_,$n)=@ARGV;s/^.(..)*$/0$&/;($k=unpack('B*',pack('H*',$_)))=~
s/^0*//;$x=0;$z=$n=~s/./$x=&badd(&bmul($x,16),hex$&)/ge;while(read(STDIN,$_,$w
=((2*$d-1+$z)&~1)/2)){$r=1;$_=substr($_."\0"x$w,$c=0,$w);s/.|\n/$c=&badd(&bmul
($c,256),ord$&)/ge;$_=$k;s/./$r=&bmod(&bmul($r,$r),$x),$&?$r=&bmod(&bmul($r,$c
),$x):0,""/ge;($r,$t)=&bdiv($r,256),$_=pack(C,$t).$_ while$w--+1-2*$d;print}
```

Other Code examples



This package is intended for use by people wearing white hats to weed out users on systems they administer with poor tastes in passwords.

``` perl
perl -nle 'setpwent;crypt($_,$c)eq$c&&print"$u $_"while($u,$c)=getpwent'
```

### rc4

``` perl
#!/usr/bin/perl -p
INIT{sub Q{$s[($_[0]+=$_[1])%=256]}sub S{@s[$y,$x++]=@s[$x,$y]}@k=pop
=~/../g;S$y=map{S Q$y,$_+hex$k[$x%@k]}@s=0..255}s/\C/$&^chr Q S Q$y,Q$x/eg
```

Alternative:

``` perl
#!/bin/perl -0777p-- export-a-crypto-system-sig -RC4-in-3-lines-of-perl
use integer;BEGIN{sub S{@s[$x,$y]=@s[$y,$x]}@k=unpack"C*",pack"H*",shift@ARGV;
for(@t=@s=0..255){($y+=$k[$_%@k]+$s[$x=$_])%=256;&S}$x=$y=0}$l=0;($y+=$s[($x+=
1)%=256])%=256,&S,vec($_,$l++,8)^=$s[($s[$x]+$s[$y])%256]while$l<length
```


