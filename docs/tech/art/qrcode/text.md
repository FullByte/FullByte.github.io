# Text QR Codes

## libqrencode

Install [libqrencode](https://github.com/fukuchi/libqrencode.git):

``` sh
git clone https://github.com/fukuchi/libqrencode.git
cd libqrencode/
./autogen.sh
./configure
make
sudo make install
sudo ldconfig
cmake .
make
```

Example output

```qrencode -t ASCIIi 'https://0xfab1.net'```

``` txt
##########################################################
##########################################################
####              ####      ##  ########              ####
####  ##########  ########    ##  ##  ##  ##########  ####
####  ##      ##  ####      ######    ##  ##      ##  ####
####  ##      ##  ##  ##    ####  ##  ##  ##      ##  ####
####  ##      ##  ##  ##  ##    ####  ##  ##      ##  ####
####  ##########  ####    ####    ######  ##########  ####
####              ##  ##  ##  ##  ##  ##              ####
######################  ####    ##    ####################
####    ######      ##    ##  ##  ##########    ##########
####    ######  ####  ##  ######    ##  ##          ######
######    ######    ##  ##    ####  ##########  ##    ####
########      ##########    ####      ##  ####  ####  ####
####  ########      ##    ####    ##  ##  ##########  ####
####  ##      ######  ##  ##        ##############  ######
####  ######  ##      ########                  ##    ####
####  ##  ####  ##  ##    ##      ##  ####  ##    ##  ####
####  ####            ##  ##  ##              ##  ########
####################  ##  ########    ######  ############
####              ##  ######      ##  ##  ##  ######  ####
####  ##########  ##    ##  ####  ##  ######  ############
####  ##      ##  ####      ######            ##  ##  ####
####  ##      ##  ##########    ######    ########    ####
####  ##      ##  ####    ####      ##########    ##  ####
####  ##########  ##      ##    ####  ##      ######  ####
####              ##  ####      ####  ##  ####  ####  ####
##########################################################
##########################################################
```

```qrencode -t UTF8 'https://0xfab1.net'```

``` txt
█████████████████████████████
██ ▄▄▄▄▄ ██▄▄ ▀▄▀█▀█ ▄▄▄▄▄ ██
██ █   █ █▀▄  ██▀▄ █ █   █ ██
██ █▄▄▄█ █▄▀ █▄ ▀█▄█ █▄▄▄█ ██
██▄▄▄▄▄▄▄█▄▀▄█ ▀▄▀ █▄▄▄▄▄▄▄██
██  ███ ▄▄▀▄ █▄█ ▀█▀█▀  ▀▀███
███▄ ▀▀█▄▄█▄▀ ▄█▀ ▀█▀██ █▄ ██
██ █▀▀▀▄▄▄▀▄ █▀  ▀▄█▄████▀▄██
██ █▀█▄▀▄ ▄▀▀█▀  ▄ ▄▄ ▄ ▀▄ ██
██▄██▄▄▄▄▄ █ █▄█▄  ▄▄▄ █▄████
██ ▄▄▄▄▄ █ ▀█▀▄▄ █ █▄█ ███▄██
██ █   █ ██▄▄▄▀▀█▄▄  ▄▄█▄▀ ██
██ █▄▄▄█ █▀  █▀ ▄▄▀█▀▀▀▄▄█ ██
██▄▄▄▄▄▄▄█▄██▄▄▄██▄█▄██▄██▄██
█████████████████████████████
```

```qrencode -t UTF8i 'https://0xfab1.net'```

``` txt
█▀▀▀▀▀█  ▀▀█▄▀▄ ▄ █▀▀▀▀▀█
█ ███ █ ▄▀██  ▄▀█ █ ███ █
█ ▀▀▀ █ ▀▄█ ▀█▄ ▀ █ ▀▀▀ █
▀▀▀▀▀▀▀ ▀▄▀ █▄▀▄█ ▀▀▀▀▀▀▀
██   █▀▀▄▀█ ▀ █▄ ▄ ▄██▄▄ 
 ▀█▄▄ ▀▀ ▀▄█▀ ▄█▄ ▄  █ ▀█
█ ▄▄▄▀▀▀▄▀█ ▄██▄▀ ▀    ▄▀
█ ▄ ▀▄▀█▀▄▄ ▄██▀█▀▀█▀█▄▀█
▀  ▀▀▀▀▀█ █ ▀ ▀██▀▀▀█ ▀  
█▀▀▀▀▀█ █▄ ▄▀▀█ █ ▀ █   ▀
█ ███ █  ▀▀▀▄▄ ▀▀██▀▀ ▀▄█
█ ▀▀▀ █ ▄██ ▄█▀▀▄ ▄▄▄▀▀ █
▀▀▀▀▀▀▀ ▀  ▀▀▀  ▀ ▀  ▀  ▀
```

## QR Code as DNS TXT records

Why save a QR code as TXT record in your DNS and call it whenever instead of generating it?

TXT records can contain any printable ASCII character and should be enclosed in quotes. Each quoted string in a DNS TXT record can be up to 255 characters. So we need to translate the UTF encoding into ASCII and chop the TXT into quoted chunks.

In the first step this generates the Text for the TXT record:

```sh
qrencode -t UTF8i 'https://0xfab1.net' | tr -d '\n' | sed 's/█/A/g; s/▀/B/g; s/▄/C/g; s/ /D/g'
```

This outputs:

```txt
DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDABBBBBADDBBACBCDCDABBBBBADDDDDDDDADAAADADCBAADDCBADADAAADADDDDDDDDADBBBDADBCADBACDBDADBBBDADDDDDDDDBBBBBBBDBCBDACBCADBBBBBBBDDDDDDDDAADDDABBCBADBDACDCDCAACCDDDDDDDDDDBACCDBBDBCABDCACDCDDADBADDDDDDDDADCCCBBBCBADCAACBDBDDDDCBDDDDDDDDADCDBCBABCCDCAABABBABACBADDDDDDDDBDDBBBBBADADBDBAABBBADBDDDDDDDDDDABBBBBADACDCBBADADBDADDDBDDDDDDDDADAAADADDBBBCCDBBAABBDBCADDDDDDDDADBBBDADCAADCABBCDCCCBBDADDDDDDDDBBBBBBBDBDDBBBDDBDBDDBDDBDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD
```

Adding the QR Code to DNS (in this example "qr.0xfab1.net") looks like this:

```txt
qr 10800 IN TXT "DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDABBBBBADDBBACBCDCDABBBBBADDDDDDDDADAAADADCBAADDCBADADAAADADDDDDDDDADBBBDADBCADBA" "CDBDADBBBDADDDDDDDDBBBBBBBDBCBDACBCADBBBBBBBDDDDDDDDAADDDABBCBADBDACDCDCAACCDDDDDDDDDDBACCDBBDBCABDCACDCDDADBADDDDDDDDADCCCBBBCBADCAACBDBDDDDCBDDDDDDD" "DADCDBCBABCCDCAABABBABACBADDDDDDDDBDDBBBBBADADBDBAABBBADBDDDDDDDDDDABBBBBADACDCBBADADBDADDDBDDDDDDDDADAAADADDBBBCCDBBAABBDBCADDDDDDDDADBBBDADCAADCABBC" "DCCCBBDADDDDDDDDBBBBBBBDBDDBBBDDBDBDDBDDBDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD"
```

To read the TXT record and show it as a QR code in the console run this:

```sh
dig +short TXT qr.0xfab1.net | tr -d '\" ' | fold -w 33 | sed 's/A/█/g; s/B/▀/g; s/C/▄/g; s/D/ /g'
```

The script removes the quoted blocks, creates a line return every 33 chars and replaces the chars A-D with the original UTF chars. The output looks like this:

```txt


    █▀▀▀▀▀█  ▀▀█▄▀▄ ▄ █▀▀▀▀▀█
    █ ███ █ ▄▀██  ▄▀█ █ ███ █
    █ ▀▀▀ █ ▀▄█ ▀█▄ ▀ █ ▀▀▀ █
    ▀▀▀▀▀▀▀ ▀▄▀ █▄▀▄█ ▀▀▀▀▀▀▀
    ██   █▀▀▄▀█ ▀ █▄ ▄ ▄██▄▄
     ▀█▄▄ ▀▀ ▀▄█▀ ▄█▄ ▄  █ ▀█
    █ ▄▄▄▀▀▀▄▀█ ▄██▄▀ ▀    ▄▀
    █ ▄ ▀▄▀█▀▄▄ ▄██▀█▀▀█▀█▄▀█
    ▀  ▀▀▀▀▀█ █ ▀ ▀██▀▀▀█ ▀
    █▀▀▀▀▀█ █▄ ▄▀▀█ █ ▀ █   ▀
    █ ███ █  ▀▀▀▄▄ ▀▀██▀▀ ▀▄█
    █ ▀▀▀ █ ▄██ ▄█▀▀▄ ▄▄▄▀▀ █
    ▀▀▀▀▀▀▀ ▀  ▀▀▀  ▀ ▀  ▀  ▀

```
