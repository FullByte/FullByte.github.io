How to decrypt a
DVD: in haiku form.
(Thanks, Prof. D. S. T.)
------------------------

(I abandon my
exclusive rights to make or
perform copies of

this work, U. S. Code
Title Seventeen, section
One Hundred and Six.)

Muse!  When we learned to
count, little did we know all
the things we could do

some day by shuffling
those numbers: Pythagoras
said "All is number"

long before he saw
computers and their effects,
or what they could do

by computation,
naive and mechanical
fast arithmetic.

It changed the world, it
changed our consciousness and lives
to have such fast math

available to
us and anyone who cared
to learn programming.

Now help me, Muse, for
I wish to tell a piece of
controversial math,

for which the lawyers
of DVD CCA
don't forbear to sue:

that they alone should
know or have the right to teach
these skills and these rules.

(Do they understand
the content, or is it just
the effects they see?)

And all mathematics
is full of stories (just read
Eric Temple Bell);

and CSS is
no exception to this rule.
Sing, Muse, decryption

once secret, as all
knowledge, once unknown: how to
decrypt DVDs.



Arrays' elements
start with zero and count up
from there, don't forget!

Integers are four
bytes long, or thirty-two bits,
which is the same thing.

To decode these discs,
you need a master key, as
hardware vendors get.

(This is a "player
key" and some folks other than
vendors know them now.

If they didn't, there
is also a way not to
need one, to start off.)

You'll read a "disk key"
from the disc, and decrypt it
with that player key.

You'll read a "title
key" for the video file
that you want to play.

With the disk key, you
can decrypt the title key;
that decrypts the show.



Here's a description
of how a player key will
decrypt a disk key.

You need two things here:
An encrypted disk key, which
is just six bytes long.

(Only five of those
are the _key itself_, because
"zero" marks the end.

So that's five real bytes,
and eight times five is forty;
in the ideal case,

forty bits will yield
just short of two trillion
possible choices!

Ian Goldberg once
recovered a key that long
in seven half-hours.

But his office-mate
David Wagner points out that
it's _impossible_

to achieve what the
DVD CCA seems
to want to achieve,

even by making
the key some reasonable,
"adequate" key-length:

There's no way to write
a "secure" software player
which contains the key

and runs on PCs,
yet somehow prevents users
from extracting it.

If the player can
decrypt, Wagner has noted,
users can learn how.)

This is a pointer,
"KEY", to those bytes, and when we're
done, they'll be clear-text.

Oh, the other thing!
Called "im", a pointer to six
bytes: a player key.

(Now those six bytes, the
DVD CCA says
under penalty

of perjury, are
its trade secret, and you are
breaking the law if

you tell someone that,
for instance, the Xing player
used the following:

Eighty-one; and then
one hundred three -- two times; then
two hundred (less three);

two hundred twenty
four; and last (of course not least)
the humble zero.)

We will use these few
internal variables:
t1 through t6,

unsigned integers.
k, pointer to five unsigned
bytes.  i, integer.

So here's how you do
it: first, take the first byte of
im -- that's byte zero;

OR that byte with the
number 0x100
(hexadecimal --

that's two hundred and
fifty-six to you if you
prefer decimal).

Store the result in
t1.  Take byte one of im.
Store it in t2.

Take bytes two through five
of im; store them in t3.
Take its three low bits

(you can get them by
ANDing t3 with seven);
store this in t4.

Double t3, add
eight, subtract t4; store the
result in t3.

Make t5 zero.
Now we'll start a loop; set i
equal to zero.

i gets values from
zero up to four; each time,
do all of these steps:

	Use t2 for an
	index into Table Two:
	find a byte b1.

	Use t1 for an
	index into Table Three:
	find a byte b2.

	Take exclusive OR
	of b1 with b2 and
	store this in t4.

	Shift t1 right by
	a single bit (like halving);
	store this in t2.

	Take the low bit of
	t1 (so, AND it with one),
	shift it left eight bits,

	then take exclusive
	OR of that with t4; store
	this back in t1.

	Use t4 for an
	index into Table Four:
	find a byte and store

	it back in t4.
	Shift t3 right by three bits,
	take exclusive OR

	of this with t3,
	shift this right by one bit, and
	take exclusive OR

	of this with t3,
	shift this right by eight bits, and
	take exclusive OR

	of this with t3,
	shift this right by five bits, and
	(No exclusive OR!

	Orange you glad I
	didn't say banana?) take
	the low byte (by AND

	with two hundred and
	fifty-five); now store this
	into t6.  Phew!

	Shift t3 left eight
	bits, take OR with t6, and
	store this in t3.

	Use t6 for an
	index into Table Four:
	find a byte and store

	it in t6.  Add
	t6, t5, t4; store
	the sum in t5.

	Take t5's low byte
	(AND t5 with two hundred
	fifty five) to put it

	in the ith byte of
	the vector called k.  Now shift
	t5 right eight bits;

	store the result in
	t5 again.  Now that's the
	last step in the loop.

No sooner have we
finished that loop than we'll start
another; no rest

for the wicked nor
those innocents whom lawyers
serve with paperwork.

Reader!  Think not that
technical information
ought not be called speech;

think not diagrams,
schematics, tables, numbers,
formulae -- like the

terrifying and
uniquely moving, though cliche,
Einstein equation

"Energy is just
the same as matter, but for
a little factor,

speed of light by speed
of light, and we are ourselves
frozen energy."

Einstein's formula
to convert from joules into
kilogram-meters

squared per second squared,
for all its power, uses
just five characters.

But Einstein wrote to
physicists: formal, concise,
specific, detailed.

And sometimes we write
to machines to teach them how
tasks are carried out:

and sometimes we write
to our friends to show a way
tasks are carried out.

We write precisely
since such is our habit in
talking to machines;

we say exactly
how to do a thing or how
every detail works.

The poet has choice
of words and order, symbols,
imagery, and use

of metaphor.  She
can allude, suggest, permit
ambiguities.

She need not say just
what she means, for readers can
always interpret.

Poets too, despite
their famous "license" sometimes
are constrained by rules:

How often have we
heard that some strange twist of plot
or phrase was simply

"Metri causa", for
the meter's sake, solely done
"to fit the meter"?

Programmers' art as
that of natural scientists
is to be precise,

complete in every
detail of description, not
leaving things to chance.

Reader, see how yet
technical communicants
deserve free speech rights;

see how numbers, rules,
patterns, languages you don't
yourself speak yet,

still should in law be
protected from suppression,
called valuable speech!

Ending my appeal
on that note, I will describe
the second loop.  Store

nine in i; i gets
values from nine down to
naught.  Each time, do this:

	Use i+1 as
	an index into Table
	Zero: find a byte.

	Call that byte p1.
	Now use i for an index
	in Table Zero:

	find a byte and
	call that byte p0.  Now
	use p1 as an

	index into k
	(a vector, remember?); thus
	find a byte b1.

	Use p1 as an
	index into KEY, as well:
	find a byte, use that

	byte as an index
	into Table One.  Call the
	byte you find b2.

	Use p0 as
	an index into KEY to
	find a byte b3.

	Take exclusive OR
	of b1, b2, b3,
	and store that in KEY

	(not just anywhere,
	though!).  In KEY at the byte that's
	indexed by p1.

That's it for that loop
and also for the task of
disk key decryption.



Title keys are next.
It isn't hard to decrypt
one.  The rule's the same!

Well, there's one slight
change: where you use t6, it's
Table "Five", not "Four".

And this time im is
the decrypted disk key, and
KEY the title key.



How would you like to
hear how to decrypt _both_ the
disk and title keys?

All we'll need are the
encrypted versions and a
player key.  No sweat!

We'll call the title
key TKEY, a pointer to
six bytes, encrypted.

We'll call the disk key
DKEY, a pointer to six
bytes, encrypted too.

We will use a few
internal variables,
once again: so i,

an integer, will
serve again as loop index.
im1 is six bytes,

im2 is six bytes.
Both vectors and the latter
holds our player key.

Now I told you once
about a player key I
think they gave to Xing --

I don't know this for
sure; DVD CCA
said so in court, though.

Otherwise I'd say
that this is just a "magic
number" from on high,

vouchsafed to mortals
from the mouths of the Muses
for our benefit.

In reality
I'm told it was discovered
by M.o.R.E.,

some Europeans
two-thirds of whom are today
still anonymous.

I don't want to make
a long excursus right now
on why that's not bad:

reverse engineers
in many fields are heroes
of technology,

for advancing the
knowledge of their colleagues or
of the public mind.

Yet in software the
recent trend has been to brand
tinkerers as thieves!

I urge you to read
the Crypto-gram newletter
on why that's not so.

Bruce can make the point
better there than I can here,
sticking to haiku.

So this number is,
once again, the player key:
(trade secret haiku?)

"Eighty-one; and then
one hundred three -- two times; then
two hundred (less three);

two hundred twenty
four; and last (of course not least)
the humble zero."

If you didn't know
a valid player key, then
you could find one out --

ask Frank Stevenson,
or his fellow programmer
wise Andreas Bogk.

All we have to do
is this: copy our DKEY
into im1,

use the rule above
that decrypts a disk key (with
im1 and its

friend im2 as
inputs) -- thus we decrypt the
disk key im1.

Use the rule above
that decrypts a title key.
TKEY and our new

disk key im1
are inputs now -- we decrypt
TKEY, and we're done.

That was straightforward.
Probably we didn't need
to explain this part,

but computers are
very literal, so we
might as well do so.



This part is really
exciting for movie fans:
decrypt DVDs!

Well, at least sectors
of DVDs, but they are
made up of sectors.

Sectors (of two to
the eleventh bytes) are the
encryption units.

Rejoice then, get some
popcorn out, and butter if
you aren't vegan.

Margarine works well
if you're vegan, or if you
are watching your weight.

I've heard you can put
tarragon on your popcorn.
I haven't tried it.

Why did I tell you
to rejoice?  Because we are
about to watch a

movie, at least if
we have a good MPEG-2
player close at hand.

We need two things now,
though, beyond our MPEG-2
players and popcorn:

A vector "SEC" of
two thousand forty-eight bytes,
disk sector contents.

(These start off in their
encrypted form, but we will
leave them decrypted.)

And a vector KEY
of six bytes, the decrypted
title key we'll use.

We will use these few
internal variables:
t1 through t6,

unsigned integers.
Remember those from before?
END is a pointer

to the end of the
sector, which is SEC plus two
thousand forty-eight.

Take the first byte of
KEY (that's byte zero), perform
exclusive OR with

byte eighty-four of
SEC.  Treating the result as
an integer, take

OR of that with two
hundred fifty-six.  Store the
result in t1.

Take the next byte (which
is byte one) of KEY, perform
exclusive OR with

the next byte of SEC
(byte eighty-five, right?); store the
result in t2.

Take bytes two through five
of KEY and take exclusive
OR of these with their

counterparts abroad,
bytes eighty-six through eighty-nine
of our sector SEC.

Store this in t3.
(It will fit because it is
four bytes, like t3.)

I must quote myself
because we're going to do
some things once again:

(Above, in the first
part, we talked about t3:)
"Take its three low bits

(you can get them by
ANDing t3 with seven);
store this in t4.

Double t3, add
eight, subtract t4; store the
result in t3."

(Now increment SEC
by one hundred twenty-eight!)
"Make t5 zero."

Now start a loop, and
do these things as long as SEC
doesn't equal END:

	Use t2 for an
	index into Table Two:
	find a byte b1.

	Use t1 for an
	index into Table Three:
	find a byte b2.

	Take exclusive OR
	of b1 with b2 and
	store this in t4.

	Shift t1 right by
	a single bit (like halving);
	store this in t2.

	Take the low bit of
	t1 (so, AND it with one),
	shift it left eight bits,

	then take exclusive
	OR of that with t4; store
	this back in t1.

	(The step that's coming
	up is _slightly_ different from
	the original.)

	Use t4 for an
	index into Table Five:
	find a byte and store

	it back in t4.
	Shift t3 right by three bits,
	take exclusive OR

	of this with t3,
	shift this right by one bit, and
	take exclusive OR

	of this with t3,
	shift this right by eight bits, and
	take exclusive OR

	of this with t3,
	shift this right by five bits, and
	(No exclusive OR!

	Orange you glad I
	didn't say banana?) take
	the low byte (by AND

	with two hundred and
	fifty-five); now store this
	into t6.  Phew!

	Shift t3 left eight
	bits, take OR with t6, and
	store this in t3.

	Use t6 for an
	index into Table Four:
	find a byte and store

	it in t6.  Add
	t6, t5, t4; store
	the sum in t5.

	(Again, here's a change
	from the original steps:
	please don't get confused.)

	In Table One use
	the byte SEC points to as an
	index, get a byte

	there, take exclusive
	OR of that byte with the low
	byte of t5; store

	the result where SEC
	points, and increment SEC by
	one.  This is all that

	has changed in these steps.
	And we're almost done!  Now shift
	t5 right eight bits;

	store the result in
	t5 again.  That is the
	last step in the loop.

Now I want a drink
(mnemonics in crypto poems
are great!); exercise

from singing so long
makes me thirst for a glass of
soda, slice of pie.

For this is the end
of the decryption process;
you can now go home.



But wait!  I hear a
voice entreating me to stay:
"O, the Tables tell!"

Alas, I have not
as yet declared to you the
CSS Tables.

This is a major
issue, in that I don't know
what these tables _mean_:

our noble guide has
told us in outline what they
are for, or something

of their structure.  But
to me, a humble poet
of mathematics,

they are opaque, they
are certain combinations
of ancient, noble

Number.  Their inner
logic, aitia, telos,
still unknown to me.

Herein a clear free
speech question: would courts see fit
to muzzle me, then,

from speaking numbers,
technical data, which I
did not make and more

cannot memorize,
cannot explain in detail,
cannot understand?

I have these numbers.
They have meaning, this is clear:
else why suppress them?

I wish to speak or
let the Muse announce through me
Tables of Numbers.

Professor Moglen!
Help defend my right to share
these numbers with you!

You called the right to
speak with PGP like that
to use Navaho.

Help me then in my
haiku quest to share these bits,
and not be censored.

Preserve my right to
speak here, in this extreme, these
mystery Tables

the products, pieces
of technique, which but a very
few will understand.

Mary Jo White, the
United States Attorney
for S.D.N.Y.,

your logic erodes
any meaningful power
Internet speakers

would retain against
state censorship.  Do you care?
Have you any shame?

Fight, brave amici,
with effective, functional
argumentation.

I'll try to help by
singing these octets, until
court orders forbid.

(Sad to say, I have
removed hyphens in numbers:
poetic license.)

Table Zero is:
Five, zero, one, two, three, four,
oh, one, two, three, four.

Table One is long:
two to the eighth power bytes.
Ready?  Here they are:

Fifty one; then one
hundred fifteen; fifty nine;
thirty eight; ninety

nine; thirty five; one
hundred seven; one hundred
eighteen; sixty two;

one hundred twenty
six; fifty four; forty three;
one hundred ten; then

forty six; then one
hundred two; one hundred and
twenty three; then two

hundred eleven;
one hundred forty seven;
two hundred nineteen;

six; sixty seven;
three; seventy five; then one
hundred fifty; two

hundred twenty two;
one hundred fifty eight; two
hundred fourteen; then

eleven; and then
seventy eight; fourteen; then
seventy; then one

hundred fifty five;
eighty seven; twenty three;
ninety five; then one

hundred thirty; one
hundred ninety nine; then one
hundred thirty five;

two hundred seven;
eighteen; ninety; twenty six;
eighty two; then one

hundred forty three;
two hundred two; one hundred
thirty eight; then one

hundred ninety four;
thirty one; two hundred and
seventeen; then one

hundred fifty three;
two hundred nine; zero; then
seventy three; nine;

sixty five; then one
hundred forty four; then two
hundred sixteen; one

hundred fifty two;
two hundred eight; one; and then
seventy two; eight;

sixty four; then one
hundred forty five; sixty
one; one hundred and

twenty five; fifty
three; thirty six; one hundred
nine; forty five; one

hundred one; then one
hundred sixteen; sixty; one
hundred twenty four;

fifty two; thirty
seven; one hundred eight; then
forty four; then one

hundred; one hundred
seventeen; two hundred and
twenty one; then one

hundred and fifty
seven; two hundred thirteen;
four; seventy plus

seven; thirteen; then
sixty nine; one hundred and
forty eight; then two

hundred twenty; one
hundred fifty six; then two
hundred twelve; five; then

seventy six; twelve;
sixty eight; one hundred and
forty nine; eighty

nine; twenty five; then
eighty one; one hundred and
twenty eight; then two

hundred one; then one
hundred thirty seven; one
hundred ninety three;

sixteen; eighty eight;
twenty four; eighty; then one
hundred twenty nine;

two hundred; then one
hundred thirty six; then one
hundred ninety two;

seventeen; then two
hundred fifteen; one hundred
fifty one; then two

hundred twenty three;
two; seventy one; seven;
seventy nine; one

hundred forty six;
two hundred eighteen; then one
hundred fifty four;

two hundred ten; then
fifteen; seventy four; ten;
sixty six; then one

hundred fifty nine;
eighty three; nineteen; ninety
one; one hundred and

thirty four; then one
hundred ninety five; then one
hundred thirty one;

two hundred three; then
twenty two; ninety four; then
thirty; eighty six;

one hundred thirty
nine; two hundred six; then one
hundred forty two;

one hundred ninety
eight; twenty seven; then one
hundred seventy

nine; two hundred and
forty three; one hundred and
eighty seven; one

hundred sixty six;
two hundred twenty seven;
one hundred sixty

three; two hundred and
thirty five; two hundred and
forty six; then one

hundred ninety; two
hundred fifty four; then one
hundred eighty two;

then one hundred and
seventy one; two hundred
thirty eight; then one

hundred seventy
four; two hundred thirty; two
hundred fifty one;

fifty five; then one
hundred nineteen; sixty three;
thirty four; then one

hundred three; thirty
nine; one hundred eleven;
one hundred fourteen;

fifty eight; then one
hundred twenty two; fifty;
forty seven; one

hundred six; forty
two; ninety eight; one hundred
twenty seven; one

hundred eighty five;
two hundred forty nine; one
hundred seventy

seven; one hundred
sixty; two hundred thirty
three; one hundred and

sixty nine; then two
hundred twenty five; then two
hundred forty; one

hundred eighty four;
two hundred forty eight; one
hundred seventy

six; one hundred and
sixty one; two hundred and
thirty two; then one

hundred sixty eight;
two hundred twenty four; two
hundred forty one;

ninety three; twenty
nine; eighty five; one hundred
thirty two; then two

hundred five; then one
hundred forty one; then one
hundred and ninety

seven; twenty; then
ninety two; twenty eight; then
eighty four; then one

hundred thirty three;
two hundred four; one hundred
forty; one hundred

ninety six; twenty
one; one hundred eighty nine;
two hundred fifty

three; one hundred and
eighty one; one hundred and
sixty four; then two

hundred and thirty
seven; then one hundred and
seventy three; two

hundred twenty nine;
two hundred forty four; one
hundred eighty eight;

two hundred fifty
two; one hundred eighty; one
hundred sixty five;

two hundred thirty
six; one hundred seventy
two; two hundred and

twenty eight; then two
hundred forty five; fifty
seven; one hundred

twenty one; forty
nine; thirty two; one hundred
five; forty one; then

ninety seven; one
hundred twelve; fifty six; one
hundred twenty; then

forty eight; thirty
three; one hundred four; forty;
ninety six; then one

hundred thirteen; one
hundred eighty three; then two
hundred and forty

seven; one hundred
ninety one; one hundred and
sixty two; then two

hundred thirty one;
one hundred sixty seven;
two hundred thirty

nine; two hundred and
forty two; one hundred and
eighty six; then two

hundred fifty; one
hundred seventy eight; one
hundred seventy

five; two hundred and
thirty four; one hundred and
seventy; then two

hundred twenty six;
two hundred fifty five.
That's the whole Table.

Just when you thought it
was safe, here is Table Two,
which has the same length:

Zero; one; two; three;
four; five; six; seven; nine; eight;
eleven; ten; then

thirteen; twelve; fifteen;
fourteen; eighteen; nineteen; then
sixteen; seventeen;

twenty two; twenty
three; twenty; twenty one; then
twenty seven; then

twenty six; twenty
five; twenty four; thirty one;
thirty; twenty nine;

twenty eight; thirty
six; thirty seven; thirty
eight; thirty nine; then

thirty two; thirty
three; thirty four; thirty five;
forty five; forty

four; forty seven;
forty six; forty one; then
forty; forty three;

forty two; fifty
four; fifty five; fifty two;
fifty three; fifty;

fifty one; forty
eight; forty nine; sixty three;
sixty two; sixty

one; sixty; fifty
nine; fifty eight; fifty plus
seven; fifty six;

seventy three; then
seventy two; seventy
five; seventy four;

seventy seven;
seventy six; seventy
nine; seventy eight;

sixty four; sixty
five; sixty six; sixty plus
seven; sixty eight;

sixty nine; and then
seventy; seventy one;
ninety one; ninety;

eighty nine; eighty
eight; ninety five; ninety four;
ninety three; ninety

two; eighty two; then
eighty three; eighty; eighty
one; eighty six; then

eighty seven; then
eighty four; eighty five; one
hundred nine; then one

hundred eight; then one
hundred eleven; then one
hundred ten; then one

hundred five; then one
hundred four; one hundred and
seven; one hundred

six; one hundred; one
hundred one; one hundred two;
one hundred three; then

ninety six; ninety
seven; ninety eight; ninety
nine; one hundred and

twenty seven; one
hundred twenty six; then one
hundred twenty five;

one hundred twenty
four; one hundred twenty three;
one hundred twenty

two; one hundred and
twenty one; one hundred and
twenty; one hundred

eighteen; one hundred
nineteen; one hundred sixteen;
then one hundred and

seventeen; then one
hundred fourteen; one hundred
fifteen; one hundred

twelve; one hundred and
thirteen; one hundred forty
six; one hundred and

forty seven; one
hundred forty four; then one
hundred forty five;

one hundred fifty;
one hundred fifty one; one
hundred forty eight;

one hundred forty
nine; one hundred fifty five;
one hundred fifty

four; one hundred and
fifty three; one hundred and
fifty two; then one

hundred fifty nine;
one hundred fifty eight; one
hundred and fifty

seven; one hundred
fifty six; one hundred and
twenty eight; then one

hundred twenty nine;
one hundred thirty; then one
hundred thirty one;

one hundred thirty
two; one hundred thirty three;
one hundred thirty

four; one hundred and
thirty five; one hundred and
thirty seven; one

hundred thirty six;
one hundred thirty nine; one
hundred thirty eight;

one hundred forty
one; one hundred forty; one
hundred forty three;

one hundred forty
two; one hundred eighty two;
one hundred eighty

three; one hundred and
eighty; one hundred eighty
one; one hundred and

seventy eight; one
hundred seventy nine; one
hundred seventy

six; one hundred and
seventy seven; then one
hundred ninety one;

one hundred ninety;
one hundred eighty nine; one
hundred eighty eight;

one hundred eighty
seven; one hundred eighty
six; one hundred and

eighty five; then one
hundred eighty four; then one
hundred sixty four;

one hundred sixty
five; one hundred sixty six;
one hundred sixty

seven; one hundred
sixty; one hundred sixty
one; one hundred and

sixty two; then one
hundred sixty three; then one
hundred seventy

three; one hundred and
seventy two; one hundred
seventy five; one

hundred seventy
four; one hundred sixty nine;
one hundred sixty

eight; one hundred and
seventy one; one hundred
seventy; then two

hundred nineteen; two
hundred eighteen; two hundred
seventeen; then two

hundred sixteen; two
hundred twenty three; then two
hundred twenty two;

two hundred twenty
one; two hundred twenty; two
hundred ten; then two

hundred eleven;
two hundred eight; two hundred
nine; two hundred and

fourteen; two hundred
fifteen; two hundred twelve; two
hundred thirteen; two

hundred one; then two
hundred; two hundred three; two
hundred two; then two

hundred five; then two
hundred four; two hundred and
seven; two hundred

six; one hundred and
ninety two; one hundred and
ninety three; then one

hundred ninety four;
one hundred ninety five; one
hundred ninety six;

one hundred ninety
seven; one hundred ninety
eight; one hundred and

ninety nine; then two
hundred fifty five; then two
hundred fifty four;

two hundred fifty
three; two hundred fifty two;
two hundred fifty

one; two hundred and
fifty; two hundred forty
nine; two hundred and

forty eight; then two
hundred forty six; then two
hundred and forty

seven; two hundred
forty four; two hundred and
forty five; then two

hundred forty two;
two hundred forty three; two
hundred forty; two

hundred forty one;
two hundred thirty seven;
two hundred thirty

six; two hundred and
thirty nine; two hundred and
thirty eight; then two

hundred thirty three;
two hundred thirty two; two
hundred thirty five;

two hundred thirty
four; two hundred twenty eight;
two hundred twenty

nine; two hundred and
thirty; two hundred thirty
one; two hundred and

twenty four; then two
hundred twenty five; then two
hundred twenty six;

two hundred twenty
seven.  That's the end of the
Table Two listing.

Table Three repeats
itself sixty-four times with
this eight-byte sequence:

Zero, thirty six,
seventy three, one hundred
nine, one hundred and

forty six, then one
hundred eighty two, and then
two hundred nineteen,

and last of all, two
to the eighth, less one (or two
hundred fifty five).

Dr. Touretzky
has a more concise account
of what Table Four

is for, and where it
comes from; but for now, I think
I will just list it:

Zero; one hundred
twenty eight; sixty four; one
hundred ninety two;

thirty two; then one
hundred sixty; ninety six;
two hundred twenty

four; sixteen; then one
hundred forty four; eighty;
two hundred eight; then

forty eight; then one
hundred seventy six; one
hundred twelve; then two

hundred forty; eight;
one hundred thirty six; then
seventy two; two

hundred; forty; one
hundred sixty eight; then one
hundred four; then two

hundred thirty two;
twenty four; one hundred and
fifty two; eighty

eight; two hundred and
sixteen; fifty six; then one
hundred eighty four;

one hundred twenty;
two hundred forty eight; four;
one hundred thirty

two; sixty eight; one
hundred ninety six; thirty
six; one hundred and

sixty four; then one
hundred; two hundred twenty
eight; twenty; then one

hundred forty eight;
eighty four; two hundred twelve;
fifty two; then one

hundred eighty; one
hundred sixteen; two hundred
forty four; twelve; one

hundred forty; then
seventy six; two hundred
four; forty four; one

hundred seventy
two; one hundred eight; then two
hundred thirty six;

twenty eight; then one
hundred fifty six; ninety
two; two hundred and

twenty; sixty; one
hundred eighty eight; then one
hundred twenty four;

two hundred fifty
two; two; one hundred thirty;
sixty six; then one

hundred ninety four;
thirty four; one hundred and
sixty two; ninety

eight; two hundred and
twenty six; eighteen; then one
hundred forty six;

eighty two; then two
hundred ten; fifty; then one
hundred seventy

eight; one hundred and
fourteen; two hundred forty
two; ten; one hundred

thirty eight; and then
seventy four; two hundred
two; forty two; one

hundred seventy;
one hundred six; two hundred
thirty four; twenty

six; one hundred and
fifty four; ninety; then two
hundred eighteen; then

fifty eight; then one
hundred eighty six; then one
hundred twenty two;

two hundred fifty;
six; one hundred thirty four;
seventy; then one

hundred ninety eight;
thirty eight; one hundred and
sixty six; then one

hundred two; then two
hundred thirty; twenty two;
one hundred fifty;

eighty six; then two
hundred fourteen; fifty four;
one hundred eighty

two; one hundred and
eighteen; two hundred forty
six; fourteen; then one

hundred forty two;
seventy eight; two hundred
six; forty six; one

hundred seventy
four; one hundred ten; then two
hundred thirty eight;

thirty; one hundred
fifty eight; ninety four; two
hundred twenty two;

sixty two; then one
hundred ninety; one hundred
twenty six; then two

hundred fifty four;
one; one hundred twenty nine;
sixty five; then one

hundred ninety three;
thirty three; one hundred and
sixty one; ninety

seven; two hundred
twenty five; seventeen; one
hundred forty five;

eighty one; then two
hundred nine; forty nine; one
hundred seventy

seven; one hundred
thirteen; two hundred forty
one; nine; one hundred

thirty seven; then
seventy three; two hundred
one; forty one; one

hundred sixty nine;
one hundred five; two hundred
thirty three; twenty

five; one hundred and
fifty three; eighty nine; two
hundred seventeen;

fifty seven; one
hundred eighty five; then one
hundred twenty one;

two hundred forty
nine; five; one hundred thirty
three; sixty nine; one

hundred and ninety
seven; thirty seven; one
hundred sixty five;

one hundred one; two
hundred twenty nine; twenty
one; one hundred and

forty nine; eighty
five; two hundred thirteen; then
fifty three; then one

hundred eighty one;
one hundred seventeen; two
hundred forty five;

thirteen; one hundred
forty one; seventy plus
seven; two hundred

five; forty five; one
hundred seventy three; one
hundred nine; then two

hundred and thirty
seven; twenty nine; then one
hundred and fifty

seven; ninety three;
two hundred twenty one; then
sixty one; then one

hundred eighty nine;
one hundred twenty five; two
hundred fifty three;

three; one hundred and
thirty one; sixty seven;
one hundred ninety

five; thirty five; one
hundred sixty three; ninety
nine; two hundred and

twenty seven; then
nineteen; one hundred forty
seven; eighty three;

then two hundred and
eleven; fifty one; one
hundred seventy

nine; one hundred and
fifteen; two hundred forty
three; eleven; one

hundred thirty nine;
seventy five; two hundred
three; forty three; one

hundred seventy
one; one hundred seven; two
hundred thirty five;

twenty seven; one
hundred fifty five; ninety
one; two hundred and

nineteen; fifty nine;
one hundred eighty seven;
one hundred twenty

three; two hundred and
fifty one; seven; then one
hundred thirty five;

seventy one; one
hundred ninety nine; thirty
nine; one hundred and

sixty seven; one
hundred three; two hundred and
thirty one; twenty

three; one hundred and
fifty one; eighty seven;
two hundred fifteen;

fifty five; then one
hundred eighty three; then one
hundred nineteen; two

hundred and forty
seven; fifteen; one hundred
forty three; and then

seventy nine; two
hundred seven; forty plus
seven; one hundred

seventy five; one
hundred eleven; then two
hundred thirty nine;

thirty one; then one
hundred fifty nine; ninety
five; two hundred and

twenty three; sixty
three; one hundred ninety one;
one hundred twenty

seven; two hundred
fifty five.  And that's the end
of the fourth Table.

(You'll get Table Five
if you flip each bit in the
Table Four, supra.)

Have mercy on me,
Lord, and lesser judges, and
on Jon Johansen.
