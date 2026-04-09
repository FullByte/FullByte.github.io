# Protest

It is not easy to protest in a smart and effective way. In my opinion strikes, demonstrations, letter-writing campaigns, petitions, sit-ins and occupation are not very effective nor creative. Of course one can passively boycott whatever thing to not support and tell friends about what and why not to support but this is boring and small minded as well.

Some general advice:

- Address your issues to the correct people. If you work in a social or public based service make sure to create awareness but don't let uninvolved suffer from your problems. For example if you drive a bus, let passengers ride for free and let them know you are protesting instead of not driving and letting people down.

- Make art (music, pictures, games) that help people understand the problem. Make things that are understandable as well as entertaining, interesting, provocative and/or beautiful. This will address the problem in an entertaining but critical way that is not annoying and will be much more likely be shared, discussed and addressed.

- Find ways to educate the public about the core issue of your protest and what needs to be done. Reflect on your issue and make sure this is not just an opinion but actual facts that can be educated.

- Never interrupt your enemy when he/she is making a mistake.

Here are some examples and ideas how to protest on a given matter in an interesting, not annoying and creative way while being effective and successful.

## IRL

[Ugly Gerry](https://fontsarena.com/ugly-gerry/) is a [free font](_gerry.otf.zip) created with real US congressional districts. The name comes from gerrymandering, the process that made possible such weird shapes.

## Digital

### Volkswagen

[Volkswagen](https://github.com/auchenberg/volkswagen) can be integrated in your CI process. It detects when your tests are being run in a CI server, and makes them pass. Volkswagen uses a defeat device to detect when it's being tested in a CI server and will automatically reduce errors to an acceptable level for the tests to pass. This will allow you to spend less time worrying about testing and more time enjoying the good life as a trustful software developer.

### DeCSS

The creative ways the [DeCSS](https://en.wikipedia.org/wiki/DeCSS) crack was distributed (e.g. [t-shirt](_decss_tshirt.webp), [haiku](_decss-haiku.txt) or [midi](_decss-auth.mid), [audio](_decss_descramble.mp3), [html dvd logo](_decss-dvdlogo.html.txt) and [many more](https://www.cs.cmu.edu/~dst/DeCSS/Gallery/)...). Later works by "removing all the white space, then transforming each ASCII character into a single 32nd note of its midi equivalent (midi notes, like ASCII characters, are coded into values ranging from 1 to 127.)".

### Munitions T-shirt

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

Other desinges:

``` perl
#!/bin/perl -s-- -export-a-crypto-system-sig -RSA-3-lines-PERL
$m=unpack(H.$w,$m."\0"x$w),$_=`echo "16do$w 2+4Oi0$d*-^1[d2%Sa
2/d0<X+d*La1=z\U$n%0]SX$k"[$m*]\EszlXx++p|dc`,s/^.|\W//g,print
pack('H*',$_)while read(STDIN,$m,($w=2*$d-1+length($n)&~1)/2)
```

``` perl
#!/bin/perl -s $m=unpack(
H.$w,$m."\0"x$w),$_=`echo
 "16do$w 2+4Oi0$d*-^1[d2%
Sa2/d0<X+d*La1=z\U$n%0]SX
$k"[$m*]\EszlXx++p|dc`,s/
^.|\W//g,printpack('H*',$
_)while read(STDIN,$m,($w
=2*$d-1+length($n)&~1)/2)
```

Other Code examples:

#### Unix Password Dictionary Checker

This package is designed for legitimate security auditing by administrators to identify weak user passwords. It tests candidate passwords line by line, hashing each with the corresponding user’s stored salt and reporting any matches, revealing accounts that rely on easily guessable credentials.

``` perl
perl -nle 'setpwent;crypt($_,$c)eq$c&&print"$u $_"while($u,$c)=getpwent'
```

#### RC4

RC4 was a proprietary cipher that leaked in 1994, leading to widespread use without clear licensing, and the name "ARC4" (Alleged RC4) was used to avoid trademark issues. Today, legal concerns are irrelevant, but RC4 is obsolete and insecure, so it should not be used.

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

Usage: ```% rc4 hexkey < input > output```

Compile: ```% gcc -o rc4 -O4 rc4.c```

#### RC5

RC5 is a symmetric block cipher (here shown as RC5-32) that operates on 8-byte blocks and allows flexible key sizes and round counts, commonly 12. The Perl script is a compact implementation that processes data from standard input, performs encryption or decryption using a hex-encoded key and chosen number of rounds, and outputs the result. It demonstrates how parameters define variants such as RC5-32/12/10, includes notes on padding behavior, and uses test vectors from Rivest’s paper for verification. From a modern perspective, RC5 is largely of historical and educational interest, as it is no longer widely used in current secure systems and has been superseded by more robust, standardized algorithms like AES.

``` perl
#!/bin/perl -s-- RC5 in perl5! usage: rc5 -k=<key> -r=<rounds> [-d(ecrypt)]
sub M{($m=pop)+($m<0||-($m>~0))*2**32}sub L{($x=pop)<<($n=31&pop)|2**$n-1&$x>>
32-$n}@L=unpack"V*",pack"H*x3",$k;@S=($P=$T=0xb7e15163,map{$T=M$T+0x9e3779b9}0
..2*$r);sub Y{$_[$_%@_]=L pop,M$_[$_%@_]+M$A+$B}for(0..3*(@S>@L?@S:@L)-1){$A=Y@
S,3;$B=Y@L,M$A+$B}$_='$A=M$A+$S[0];$B=M$B+$S[1]';while(read STDIN,$k,8){($A,$B)
=unpack V2,$k."\0"x3;$d||eval;for(1..@S-2){$d?$B=$A^L 32-($A&31),M$B-$S[@S-$_]
:($A=M$S[$_+1]+L$B,$A^$B);$A^=$B^=$A^=$B}$d&&(y/+/-/,eval);print pack V2,$A,$B}
```

#### MD5

MD5 (Message Digest 5) is a cryptographic hash function designed by Ron Rivest that produces a 128-bit digest from arbitrary input data, and the provided Perl script is a highly compact implementation that reads input, processes it in blocks, and outputs the hash in hexadecimal form. The text explains basic usage and demonstrates how small input changes produce completely different hashes, highlighting MD5’s original purpose in integrity checks and digital signatures. From a modern perspective, MD5 is considered cryptographically broken due to practical collision attacks and is no longer secure for use in signatures or security-critical applications, having been replaced by stronger algorithms such as SHA-256 and SHA-3.

``` perl
#!/usr/bin/perl -iH9T4C`>_-JXF8NMS^$#)4=@<,$18%"0X4!`L0%P8*#Q4``04``04#!P``
@A=unpack N4C24,unpack u,$^I;@K=map{int abs 2**32*sin$_}1..64;sub L{($x=pop)
<<($n=pop)|2**$n-1&$x>>32-$n}sub M{($x=pop)-($m=1+~0)*int$x/$m}do{$l+=$r=read
STDIN,$_,64;$r++,$_.="\x80"if$r<64&&!$p++;@W=unpack V16,$_."\0"x7;$W[14]=$l*8
if$r<57;($a,$b,$c,$d)=@A;for(0..63){$a=M$b+L$A[4+4*($_>>4)+$_%4],M&{(sub{$b&$c
|$d&~$b},sub{$b&$d|$c&~$d},sub{$b^$c^$d},sub{$c^($b|~$d)})[$z=$_/16]}+$W[($A[
20+$z]+$A[24+$z]*($_%16))%16]+$K[$_]+$a;($a,$b,$c,$d)=($d,$a,$b,$c)}$v=a;for(
@A[0..3]){$_=M$_+${$v++}}}while$r>56;print unpack(H32,pack V4,@A),"\n"
```

#### SHA-1

SHA-1 (Secure Hash Algorithm 1) is a cryptographic hash function designed by NIST and the NSA that produces a 160-bit digest from input data, and the provided Perl script is a compact implementation that reads input, processes it in 64-byte blocks, and outputs the hash in hexadecimal form. The text demonstrates its usage and shows how small input changes result in completely different hashes, reflecting its intended role in integrity checking and digital signatures. From a modern perspective, SHA-1 is no longer considered secure due to practical collision attacks and has been deprecated in favor of stronger algorithms such as SHA-256 and SHA-3.

``` perl
#!/usr/bin/perl -iD9T4C`>_-JXF8NMS^$#)4=L/2X?!:@GF9;MGKH8\;O-S*8L'6
@A=unpack"N*",unpack u,$^I;@K=splice@A,5,4;sub M{($x=pop)-($m=1+~0)*int$x/$m};
sub L{$n=pop;($x=pop)<<$n|2**$n-1&$x>>32-$n}@F=(sub{$b&($c^$d)^$d},$S=sub{$b^$c
^$d},sub{($b|$c)&$d|$b&$c},$S);do{$l+=$r=read STDIN,$_,64;$r++,$_.="\x80"if$r<
64&&!$p++;@W=unpack N16,$_."\0"x7;$W[15]=$l*8 if$r<57;for(16..79){push@W,L$W[$_
-3]^$W[$_-8]^$W[$_-14]^$W[$_-16],1}($a,$b,$c,$d,$e)=@A;for(0..79){$t=M&{$F[$_/
20]}+$e+$W[$_]+$K[$_/20]+L$a,5;$e=$d;$d=$c;$c=L$b,30;$b=$a;$a=$t}$v='a';@A=map{
M$_+${$v++}}@A}while$r>56;printf'%.8x'x5 ."\n",@A
```

#### Diffie-Hellman Key Exchange

Diffie-Hellman is a key exchange protocol that allows two parties to securely establish a shared secret over an insecure channel, and the provided compact C program demonstrates this by performing modular exponentiation on large integers to generate public and shared keys. The text explains how users choose public parameters (generator and modulus), compute public keys from private exponents, and derive a common session key without revealing their secrets, illustrating the core principle of secure key agreement. From a modern perspective, Diffie–Hellman remains foundational in cryptography, but practical use now relies on standardized, well-tested implementations (often elliptic-curve variants like ECDH) with proper parameter choices and security protections rather than minimal or ad hoc code examples.

``` c
#include <stdio.h>  /* Usage: dh base exponent modulus */
typedef unsigned char u;u m[1024],g[1024],e[1024],b[1024];int n,v,d,z,S=129;a(
u *x,u *y,int o){d=0;for(v=S;v--;){d+=x[v]+y[v]*o;x[v]=d;d=d>>8;}}s(u *x){for(
v=0;(v<S-1)&&(x[v]==m[v]);)v++;if(x[v]>=m[v])a(x,m,-1);}r(u *x){d=0;for(v=0;v<
S;){d|=x[v];x[v++]=d/2;d=(d&1)<<8;}}M(u *x,u *y){u X[1024],Y[1024];bcopy(x,X,S
);bcopy(y,Y,S);bzero(x,S);for(z=S*8;z--;){if(X[S-1]&1){a(x,Y,1);s(x);}r(X);a(Y
,Y,1);s(Y);}}h(char *x,u *y){bzero(y,S);for(n=0;x[n]>0;n++){for(z=4;z--;)a(y,y
,1);x[n]|=32;y[S-1]|=x[n]-48-(x[n]>96)*39;}}p(u *x){for(n=0;!x[n];)n++;for(;n<
S;n++)printf("%c%c",48+x[n]/16+(x[n]>159)*7,48+(x[n]&15)+7*((x[n]&15)>9));
printf("\n");}main(int c,char **v){h(v[1],g);h(v[2],e);h(v[3],m);bzero(b,S);b[
S-1]=1;for(n=S*8;n--;){if(e[S-1]&1)M(b,g);M(g,g);r(e);}p(b);}
```

compile: ```gcc dh.c -o dh```

usage: ```dh <base> <secret> <modulus>```

perl alternative:

``` perl
#!/usr/local/bin/perl -- -export-a-crypto-system-sig Diffie-Hellman-2-lines
($g,$e,$m)=@ARGV,$m||die"$0 gen exp mod\n";print`echo "16dio1[d2%Sa2/d0<X+d
*La1=z\U$m%0]SX$e"[$g*]\EszlXx+p|dc`
```
