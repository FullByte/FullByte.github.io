# Codes

Yet another not complete list of random codes.

## QR-Code

A QR code (Quick Response code) is a type of two-dimensional barcode (matrix barcode) invented in 1994 by Denso Wave, a Japanese company. Unlike traditional 1D barcodes, QR codes encode data both horizontally and vertically, enabling much higher data capacity and fast scanning. 

QR codes use advanced math for reliability. Data and error correction are encoded using polynomial operations in a special number system called a Galois Field (GF(256)). Masking algorithms help make QR codes easy to scan by rearranging data patterns. The design and function of QR codes are defined by the international standard ISO/IEC 18004.

QR codes support multiple encoding modes for efficient data storage:

- Numeric mode: Only digits (0-9). Most efficient.
- Alphanumeric mode: Digits, uppercase English letters, and a few symbols (space, $, %, *, +, -, ., /, :).
- Byte mode: Binary data (8-bit bytes, e.g., UTF-8 text).
- Kanji mode: Japanese characters (Shift JIS encoding).
- ECI mode: Extended Channel Interpretation (for character set switching).

QR codes can restore lost or corrupted data via Reed-Solomon codes. There are four levels:

- L (Low): ~7% of codewords can be restored.
- M (Medium): ~15% restored.
- Q (Quartile): ~25% restored.
- H (High): ~30% restored.

QR codes have 40 versions: Version 1 is a 21x21 matrix. Each increment in version adds 4 modules per side. Version 40 is a 177x177 matrix.

Data capacity depends on version, error correction level, and encoding mode.
For example, Version 40, Low ECC can encode up to:

- Numeric: 7,089 characters
- Alphanumeric: 4,296 characters
- Byte: 2,953 bytes
- Kanji: 1,817 characters

??? info "QR Code data capacity"
        | Version | Size       | Error Correction | Numeric | Alphanumeric | Byte |
        |---------|------------|------------------|---------|--------------|------|
        | 1       | 21 x 21    | LOW              | 41      | 25           | 17   |
        |         |            | MEDIUM           | 34      | 20           | 14   |
        |         |            | QUARTILE         | 27      | 16           | 11   |
        |         |            | HIGH             | 17      | 10           | 7    |
        | 2       | 25 x 25    | LOW              | 77      | 47           | 32   |
        |         |            | MEDIUM           | 63      | 38           | 26   |
        |         |            | QUARTILE         | 48      | 29           | 20   |
        |         |            | HIGH             | 34      | 20           | 14   |
        | 3       | 29 x 29    | LOW              | 127     | 77           | 53   |
        |         |            | MEDIUM           | 101     | 61           | 42   |
        |         |            | QUARTILE         | 77      | 47           | 32   |
        |         |            | HIGH             | 58      | 35           | 24   |
        | 4       | 33 x 33    | LOW              | 187     | 114          | 78   |
        |         |            | MEDIUM           | 149     | 90           | 62   |
        |         |            | QUARTILE         | 111     | 67           | 46   |
        |         |            | HIGH             | 82      | 50           | 34   |
        | 5       | 37 x 37    | LOW              | 255     | 154          | 106  |
        |         |            | MEDIUM           | 202     | 122          | 84   |
        |         |            | QUARTILE         | 144     | 87           | 60   |
        |         |            | HIGH             | 106     | 64           | 44   |
        | 6       | 41 x 41    | LOW              | 322     | 195          | 134  |
        |         |            | MEDIUM           | 255     | 154          | 106  |
        |         |            | QUARTILE         | 178     | 108          | 74   |
        |         |            | HIGH             | 139     | 84           | 58   |
        | 7       | 45 x 45    | LOW              | 370     | 224          | 154  |
        |         |            | MEDIUM           | 293     | 178          | 122  |
        |         |            | QUARTILE         | 207     | 125          | 86   |
        |         |            | HIGH             | 154     | 93           | 64   |
        | 8       | 49 x 49    | LOW              | 461     | 279          | 192  |
        |         |            | MEDIUM           | 365     | 221          | 152  |
        |         |            | QUARTILE         | 259     | 157          | 108  |
        |         |            | HIGH             | 202     | 122          | 84   |
        | 9       | 53 x 53    | LOW              | 552     | 335          | 230  |
        |         |            | MEDIUM           | 432     | 262          | 180  |
        |         |            | QUARTILE         | 312     | 189          | 130  |
        |         |            | HIGH             | 235     | 143          | 98   |
        | 10      | 57 x 57    | LOW              | 652     | 395          | 271  |
        |         |            | MEDIUM           | 513     | 311          | 213  |
        |         |            | QUARTILE         | 364     | 221          | 151  |
        |         |            | HIGH             | 288     | 174          | 119  |
        | 11      | 61 x 61    | LOW              | 772     | 468          | 321  |
        |         |            | MEDIUM           | 604     | 366          | 251  |
        |         |            | QUARTILE         | 427     | 259          | 177  |
        |         |            | HIGH             | 331     | 200          | 137  |
        | 12      | 65 x 65    | LOW              | 883     | 535          | 367  |
        |         |            | MEDIUM           | 691     | 419          | 287  |
        |         |            | QUARTILE         | 489     | 296          | 203  |
        |         |            | HIGH             | 374     | 227          | 155  |
        | 13      | 69 x 69    | LOW              | 1022    | 619          | 425  |
        |         |            | MEDIUM           | 796     | 483          | 331  |
        |         |            | QUARTILE         | 580     | 352          | 241  |
        |         |            | HIGH             | 427     | 259          | 177  |
        | 14      | 73 x 73    | LOW              | 1101    | 667          | 458  |
        |         |            | MEDIUM           | 871     | 528          | 362  |
        |         |            | QUARTILE         | 621     | 376          | 258  |
        |         |            | HIGH             | 468     | 283          | 194  |
        | 15      | 77 x 77    | LOW              | 1250    | 758          | 520  |
        |         |            | MEDIUM           | 991     | 600          | 412  |
        |         |            | QUARTILE         | 703     | 426          | 292  |
        |         |            | HIGH             | 530     | 321          | 220  |
        | 16      | 81 x 81    | LOW              | 1408    | 854          | 586  |
        |         |            | MEDIUM           | 1082    | 656          | 450  |
        |         |            | QUARTILE         | 775     | 470          | 322  |
        |         |            | HIGH             | 602     | 365          | 250  |
        | 17      | 85 x 85    | LOW              | 1548    | 938          | 644  |
        |         |            | MEDIUM           | 1212    | 734          | 504  |
        |         |            | QUARTILE         | 876     | 531          | 364  |
        |         |            | HIGH             | 674     | 408          | 280  |
        | 18      | 89 x 89    | LOW              | 1725    | 1046         | 718  |
        |         |            | MEDIUM           | 1346    | 816          | 560  |
        |         |            | QUARTILE         | 948     | 574          | 394  |
        |         |            | HIGH             | 746     | 452          | 310  |
        | 19      | 93 x 93    | LOW              | 1903    | 1153         | 792  |
        |         |            | MEDIUM           | 1500    | 909          | 624  |
        |         |            | QUARTILE         | 1063    | 644          | 442  |
        |         |            | HIGH             | 813     | 493          | 338  |
        | 20      | 97 x 97    | LOW              | 2061    | 1249         | 858  |
        |         |            | MEDIUM           | 1600    | 970          | 666  |
        |         |            | QUARTILE         | 1159    | 702          | 482  |
        |         |            | HIGH             | 919     | 557          | 382  |
        | 21      | 101 x 101  | LOW              | 2232    | 1352         | 929  |
        |         |            | MEDIUM           | 1708    | 1035         | 711  |
        |         |            | QUARTILE         | 1224    | 742          | 509  |
        |         |            | HIGH             | 969     | 587          | 403  |
        | 22      | 105 x 105  | LOW              | 2409    | 1460         | 1003 |
        |         |            | MEDIUM           | 1872    | 1134         | 779  |
        |         |            | QUARTILE         | 1358    | 823          | 565  |
        |         |            | HIGH             | 1056    | 640          | 439  |
        | 23      | 109 x 109  | LOW              | 2620    | 1588         | 1091 |
        |         |            | MEDIUM           | 2059    | 1248         | 857  |
        |         |            | QUARTILE         | 1468    | 890          | 611  |
        |         |            | HIGH             | 1108    | 672          | 461  |
        | 24      | 113 x 113  | LOW              | 2812    | 1704         | 1171 |
        |         |            | MEDIUM           | 2188    | 1326         | 911  |
        |         |            | QUARTILE         | 1588    | 963          | 661  |
        |         |            | HIGH             | 1228    | 744          | 511  |
        | 25      | 117 x 117  | LOW              | 3057    | 1853         | 1273 |
        |         |            | MEDIUM           | 2395    | 1451         | 997  |
        |         |            | QUARTILE         | 1718    | 1041         | 715  |
        |         |            | HIGH             | 1286    | 779          | 535  |
        | 26      | 121 x 121  | LOW              | 3283    | 1990         | 1367 |
        |         |            | MEDIUM           | 2544    | 1542         | 1059 |
        |         |            | QUARTILE         | 1804    | 1094         | 751  |
        |         |            | HIGH             | 1425    | 864          | 593  |
        | 27      | 125 x 125  | LOW              | 3517    | 2132         | 1465 |
        |         |            | MEDIUM           | 2701    | 1637         | 1125 |
        |         |            | QUARTILE         | 1933    | 1172         | 805  |
        |         |            | HIGH             | 1501    | 910          | 625  |
        | 28      | 129 x 129  | LOW              | 3669    | 2223         | 1528 |
        |         |            | MEDIUM           | 2857    | 1732         | 1190 |
        |         |            | QUARTILE         | 2085    | 1263         | 868  |
        |         |            | HIGH             | 1581    | 958          | 658  |
        | 29      | 133 x 133  | LOW              | 3909    | 2369         | 1628 |
        |         |            | MEDIUM           | 3035    | 1839         | 1264 |
        |         |            | QUARTILE         | 2181    | 1322         | 908  |
        |         |            | HIGH             | 1677    | 1016         | 698  |
        | 30      | 137 x 137  | LOW              | 4158    | 2520         | 1732 |
        |         |            | MEDIUM           | 3289    | 1994         | 1370 |
        |         |            | QUARTILE         | 2358    | 1429         | 982  |
        |         |            | HIGH             | 1782    | 1080         | 742  |
        | 31      | 141 x 141  | LOW              | 4417    | 2677         | 1840 |
        |         |            | MEDIUM           | 3486    | 2113         | 1452 |
        |         |            | QUARTILE         | 2473    | 1499         | 1030 |
        |         |            | HIGH             | 1897    | 1150         | 790  |
        | 32      | 145 x 145  | LOW              | 4686    | 2840         | 1952 |
        |         |            | MEDIUM           | 3693    | 2238         | 1538 |
        |         |            | QUARTILE         | 2670    | 1618         | 1112 |
        |         |            | HIGH             | 2022    | 1226         | 842  |
        | 33      | 149 x 149  | LOW              | 4965    | 3009         | 2068 |
        |         |            | MEDIUM           | 3909    | 2369         | 1628 |
        |         |            | QUARTILE         | 2805    | 1700         | 1168 |
        |         |            | HIGH             | 2157    | 1307         | 898  |
        | 34      | 153 x 153  | LOW              | 5253    | 3183         | 2188 |
        |         |            | MEDIUM           | 4134    | 2506         | 1722 |
        |         |            | QUARTILE         | 2949    | 1787         | 1228 |
        |         |            | HIGH             | 2301    | 1394         | 958  |
        | 35      | 157 x 157  | LOW              | 5529    | 3351         | 2303 |
        |         |            | MEDIUM           | 4343    | 2632         | 1809 |
        |         |            | QUARTILE         | 3081    | 1867         | 1283 |
        |         |            | HIGH             | 2361    | 1431         | 983  |
        | 36      | 161 x 161  | LOW              | 5836    | 3537         | 2431 |
        |         |            | MEDIUM           | 4588    | 2780         | 1911 |
        |         |            | QUARTILE         | 3244    | 1966         | 1351 |
        |         |            | HIGH             | 2524    | 1530         | 1051 |
        | 37      | 165 x 165  | LOW              | 6153    | 3729         | 2563 |
        |         |            | MEDIUM           | 4775    | 2894         | 1989 |
        |         |            | QUARTILE         | 3417    | 2071         | 1423 |
        |         |            | HIGH             | 2625    | 1591         | 1093 |
        | 38      | 169 x 169  | LOW              | 6479    | 3927         | 2699 |
        |         |            | MEDIUM           | 5039    | 3054         | 2099 |
        |         |            | QUARTILE         | 3599    | 2181         | 1499 |
        |         |            | HIGH             | 2735    | 1658         | 1139 |
        | 39      | 173 x 173  | LOW              | 6743    | 4087         | 2809 |
        |         |            | MEDIUM           | 5313    | 3220         | 2213 |
        |         |            | QUARTILE         | 3791    | 2298         | 1579 |
        |         |            | HIGH             | 2927    | 1774         | 1219 |
        | 40      | 177 x 177  | LOW              | 7089    | 4296         | 2953 |
        |         |            | MEDIUM           | 5596    | 3391         | 2331 |
        |         |            | QUARTILE         | 3993    | 2420         | 1663 |
        |         |            | HIGH             | 3057    | 1852         | 1273 |

## GTIN

GTIN is the umbrella term for globally standardized product identifiers used to uniquely identify trade items. There are different types based on length:

- GTIN-13 (13 digits) → same as EAN-13*
- GTIN-12 (12 digits) → same as UPC-A**
- GTIN-14 (14 digits) → used for packaging levels or logistics
- GTIN-8 (8 digits) → for small products

*EAN is an older term, originally used mainly in Europe. EAN-13 (or GTIN-13) is the most common EAN form. Although the term EAN is still commonly used, it has been officially replaced by GTIN in global standards.

**UPC-A (Universal Product Code) or GTIN-12 is a 12-digit code widely used in the United States and Canada. There's also a shortened version called UPC-E (8 digits) used for small packages.

### GTIN structure

A GTIN is a numeric code (8, 12, 13, or 14 digits long) with this general structure:

[Country Code] + [Company Prefix] + [Item Reference] + [Check Digit]

- Company Prefix: Assigned by GS1 (the global standards organization). Identifies the brand owner.
- Item Reference: Assigned by the company to identify a specific product.
- Check Digit: A single digit at the end, used to verify that the number was correctly composed or scanned.

??? info "GTIN Prefixes"
        | Prefix        | Country / Use                      | Prefix       | Country / Use                          |
        |---------------|------------------------------------|--------------|----------------------------------------|
        | 00–13         | USA & Canada                       | 20–29        | Internal numbering                     |
        | 30–37         | France                             | 380          | Bulgaria                               |
        | 383           | Slovenia                           | 385          | Croatia                                |
        | 387           | Bosnia and Herzegovina             | 400–440      | Germany                                |
        | 45, 49        | Japan                              | 460–469      | Russia                                 |
        | 471           | Taiwan                             | 474          | Estonia                                |
        | 475           | Latvia                             | 476          | Azerbaijan                             |
        | 477           | Lithuania                          | 478          | Uzbekistan                             |
        | 479           | Sri Lanka                          | 480          | Philippines                            |
        | 481           | Belarus                            | 482          | Ukraine                                |
        | 484           | Moldova                            | 485          | Armenia                                |
        | 486           | Georgia                            | 487          | Kazakhstan                             |
        | 489           | Hong Kong                          | 50           | United Kingdom                         |
        | 520           | Greece                             | 528          | Lebanon                                |
        | 529           | Cyprus                             | 531          | North Macedonia                        |
        | 535           | Malta                              | 539          | Ireland                                |
        | 54            | Belgium and Luxembourg             | 560          | Portugal                               |
        | 569           | Iceland                            | 57           | Denmark                                |
        | 590           | Poland                             | 594          | Romania                                |
        | 599           | Hungary                            | 600, 601     | South Africa                           |
        | 608           | Bahrain                            | 609          | Mauritius                              |
        | 611           | Morocco                            | 613          | Algeria                                |
        | 616           | Kenya                              | 619          | Tunisia                                |
        | 621           | Syria                              | 622          | Egypt                                  |
        | 624           | Libya                              | 625          | Jordan                                 |
        | 626           | Iran                               | 627          | Kuwait                                 |
        | 628           | Saudi Arabia                       | 629          | United Arab Emirates                   |
        | 64            | Finland                            | 690–695      | China                                  |
        | 70            | Norway                             | 729          | Israel                                 |
        | 73            | Sweden                             | 740          | Guatemala                              |
        | 741           | El Salvador                        | 742          | Honduras                               |
        | 743           | Nicaragua                          | 744          | Costa Rica                             |
        | 745           | Panama                             | 746          | Dominican Republic                     |
        | 750           | Mexico                             | 76           | Switzerland and Liechtenstein          |
        | 770           | Colombia                           | 773          | Uruguay                                |
        | 775           | Peru                               | 777          | Bolivia                                |
        | 779           | Argentina                          | 780          | Chile                                  |
        | 784           | Paraguay                           | 786          | Ecuador                                |
        | 789–790       | Brazil                             | 80–83        | Italy                                  |
        | 84            | Spain                              | 850          | Cuba                                   |
        | 858           | Slovakia                           | 859          | Czech Republic                         |
        | 860           | Yugoslavia                         | 867          | North Korea                            |
        | 869           | Turkey                             | 87           | Netherlands                            |
        | 880           | South Korea                        | 885          | Thailand                               |
        | 888           | Singapore                          | 890          | India                                  |
        | 893           | Vietnam                            | 899          | Indonesia                              |
        | 90, 91        | Austria                            | 93           | Australia                              |
        | 94            | New Zealand                        | 955          | Malaysia                               |
        | 958           | Macau                              | 977          | Magazines (ISSN)                       |
        | 978–979       | Books (ISBN)                       | 980          | Refund receipts, voucher codes         |
        | 981–983       | Common Currency Coupons            | 990–999      | Coupon codes                           |

The check digit is calculated using the modulo 10 algorithm, also known as the Luhn algorithm variant for GTINs. Here is a python code example that uses the check digit to validate a GTIN-8, GTIN-12, GTIN-13, or GTIN-14 code:

??? info "GTIN code validation"
        One-liner:

        ```py
        is_valid_gtin=lambda g:g.isdigit()and len(g)in[8,12,13,14]and(10-sum(int(d)*(3 if i%2 else 1)for i,d in enumerate(reversed(g[:-1])))%10)%10==int(g[-1])
        ```

        Readable and with example:

        ```py
        def is_valid_gtin(gtin):
            if not gtin.isdigit() or len(gtin) not in [8, 12, 13, 14]:
                return False
            digits = list(map(int, gtin))
            total = sum(d * (3 if i % 2 else 1) for i, d in enumerate(reversed(digits[:-1])))
            check = (10 - total % 10) % 10
            return check == digits[-1]

        # Example
        print(is_valid_gtin("4006381333931"))  # True
        print(is_valid_gtin("1234567890128"))  # False
        ```

## Morse code

Morse code is a system for encoding letters, numbers, and symbols using short and long signals, known as "dots" (.) and "dashes" (-). It was invented in the 1830s for the telegraph, and is still used today in aviation, amateur radio, emergency signaling (SOS), and more.

- Each character (letter, digit, punctuation) is represented by a unique sequence of dots and dashes.
- Morse code can be sent using sound, light (flashing), or written symbols.
- There are two main standards: International Morse (ITU) and American Morse (rarely used today)

Comparing American Morse, Gerke and ITU:

| Feature       | American Morse         | Gerke/Continental | International (ITU)   |
| ------------- | ---------------------- | ----------------- | --------------------- |
| Signal types  | Dot, Dash, Long Dash   | Dot, Dash         | Dot, Dash             |
| Complexity    | More complex           | Less complex      | Simplest/Most regular |
| Adoption area | USA, Canada            | Europe            | Worldwide             |
| Use today     | Rare (historical)      | Historical        | Still widely used     |
| Code patterns | Inconsistent, variable | More regular      | Fully standardized    |

??? info "Morse Code Table"
        | Char | International Morse | American Morse  | Gerke/Continental | Mnemonic/Notes               |
        |------|---------------------|-----------------|-------------------|------------------------------|
        | A    | .-                  | .-              | .-                | Universal                    |
        | B    | -...                | -...            | -...              |                              |
        | C    | -.-.                | .-..            | -.-.              | Amer. = L int'l              |
        | D    | -..                 | -..             | -..               |                              |
        | E    | .                   | .               | .                 |                              |
        | F    | ..-.                | ..-.            | ..-.              |                              |
        | G    | --.                 | --.             | --.               |                              |
        | H    | ....                | ....            | ....              |                              |
        | I    | ..                  | ..              | ..                |                              |
        | J    | .---                | .---            | .---              |                              |
        | K    | -.-                 | -.-             | -.-               |                              |
        | L    | .-..                | .-...           | .-..              | Amer. = & int'l              |
        | M    | --                  | --              | --                |                              |
        | N    | -.                  | -.              | -.                |                              |
        | O    | ---                 | . .             | ---               | Amer. = EE int'l             |
        | P    | .--.                | .--.            | .--.              |                              |
        | Q    | --.-                | --.-            | --.-              |                              |
        | R    | .-.                 | . .             | .-.               | Amer. = EE int'l             |
        | S    | ...                 | ...             | ...               |                              |
        | T    | -                   | -               | -                 |                              |
        | U    | ..-                 | ..-             | ..-               |                              |
        | V    | ...-                | ...-            | ...-              |                              |
        | W    | .--                 | .--             | .--               |                              |
        | X    | -..-                | -..-            | -..-              |                              |
        | Y    | -.--                | -.--            | -.--              |                              |
        | Z    | --..                | --..            | --..              |                              |
        | 1    | .----               | .----           | .----             |                              |
        | 2    | ..---               | ..---           | ..---             |                              |
        | 3    | ...--               | ...--           | ...--             |                              |
        | 4    | ....-               | ....-           | ....-             |                              |
        | 5    | .....               | .....           | .....             |                              |
        | 6    | -....               | -....           | -....             |                              |
        | 7    | --...               | --...           | --...             |                              |
        | 8    | ---..               | ---..           | ---..             |                              |
        | 9    | ----.               | ----.           | ----.             |                              |
        | 0    | -----               | -----           | -----             |                              |
        | .    | .-.-.-              | .-.-.-          | .-.-.-            | Period                       |
        | ,    | --..--              | --..--          | --..--            | Comma                        |
        | ?    | ..--..              | ..--..          | ..--..            | Question mark                |
        | '    | .----.              | .----.          | .----.            | Apostrophe                   |
        | /    | -..-.               | -..-.           | -..-.             | Slash                        |
        | -    | -....-              | -....-          | -....-            | Hyphen                       |
        | @    | .--.-.              | (none)          | .--.-.            | At sign (modern, int'l)      |
        | SOS  | ...---...           | ...---...       | ...---...         | Universal distress signal    |

## Ten-Code (10-codes)

Ten-Code is a set of numeric radio codes used to represent common phrases in voice communication. These codes were developed in the 1930s and 1940s by law enforcement and public safety officials to make radio communication clearer, shorter, and more standardized.

??? info "Ten Code Table"
        | Ten-Code) |                     Procedure Word                     |
        |:---------:|:------------------------------------------------------:|
        |   10-0    |                      Use Caution                       |
        |   10-1    |            Unable to copy – change location            |
        |   10-3    |                   Stop transmitting                    |
        |   10-4    |                         Roger                          |
        |   10-5    |                         Relay                          |
        |   10-6    |                          Busy                          |
        |   10-7    |                       Out at...                        |
        |   10-8    |                         Clear                          |
        |   10-9    |                       Say again                        |
        |   10-12   |                        Stand by                        |
        |   10-13   |               Weather report/road report               |
        |   10-15   |                      Disturbance                       |
        |  10-17A   |                         Theft                          |
        |  10-17B   |                       Vandalism                        |
        |  10-17C   |                      Shoplifting                       |
        |   10-18   |                         Urgent                         |
        |   10-19   |                      Return to...                      |
        |   10-20   |                        Location                        |
        |   10-21   |                        Call...                         |
        |   10-22   |                       Disregard                        |
        |   10-23   |                        On scene                        |
        |   10-25   |                  Meet...or contact...                  |
        |   10-26   |              Detaining subject, expedite               |
        |   10-27   |           Drivers License information on...            |
        |   10-28   |             Registration information on...             |
        |   10-29   |                 Check for wanted on...                 |
        |  10-31A   |                        Burglary                        |
        |  10-31B   |                        Robbery                         |
        |  10-31C   |                        Homicide                        |
        |  10-31D   |                       Kidnapping                       |
        |  10-31E   |                        Shooting                        |
        |   10-38   |                   Traffic stop on...                   |
        |   10-42   |                        Off duty                        |
        |   10-44   |                     Request for...                     |
        |   10-46   |                    Assist motorist                     |
        |   10-49   |           East bound green light out (etc.)            |
        |   10-56   |                    Drunk pedestrian                    |
        |   10-63   |                    Prepare to copy                     |
        |   10-70   |                          Fire                          |
        |   10-74   |                        Negative                        |
        |   10-76   |                      En route...                       |
        |   10-77   |            ETA (Estimated time of arrival)             |
        |   10-78   |                   Request assistance                   |
        |   10-79   | Notify coroner (to be done by phone whenever possible) |
        |   10-80   |                         Chase                          |
        |   10-89   |                      Bomb threat                       |
        |   10-90   |                 Alarm (type of alarm)                  |
        |   10-91   |                    Pick up prisoner                    |
        |   10-92   |                   Parking complaint                    |
        |   10-95   |                  Prisoner in custody                   |
        |   10-97   |                  Check traffic signal                  |
        |   10-98   |                   Prison/jail break                    |
        |   10-99   |                     Wanted/stolen                      |

## ICD-10

The International Classification of Diseases (ICD) is a globally used diagnostic tool for epidemiology, health management and clinical purposes maintained by the World Health Organization (WHO). Here are some interesting ICD-10 codes:

??? info "ICD-10 examples"
    - V96.15 - Accident due to hang glider explosion
    - V95.43 - Accident due to spacecraft collision
    - V80.920 - Occupant of animal-drawn vehicle injured in transport accident with military vehicle
    - W58.12 - Struck by crocodile
    - W56.12 - Struck by sea lion
    - W59.22 - Struck by turtle, subsequent encounter
    - W61.33 - Pecked by chicken
    - W18.11 - Fall from or off toilet without subsequent striking against object
    - W56.32XA - Struck by other marine mammals, initial encounter
    - Y35.113 - Legal intervention involving injury by dynamite, suspect injured
    - W16.22 - Fall in (into) bucket of water
    - S30.870 - Superficial bite of left buttock
    - Z62.1 - Parental overprotection during upbringing
    - Z62.898 - Loss of love relationship in childhood
    - F22 - Delusional disorder: Lycanthropy
    - B04 - Monkeypox
    - D29.0 - Gutartige Neubildung der männlichen Genitalorgane (Penis)
    - V9107XA - Burn due to water-skis on fire
    - Y92146 - Hurt at swimming pool of prison as the place of occurrence
    - Y92253 - Hurt at the opera
    - X52 - Prolonged stay in weightless environment
    - W2202XA - Hurt walking into a lamppost
    - Y93D1 - Stabbed while crocheting
    - A20.0 - Bubonic plague
    - S10.87 - Other superficial bite of other specified part of neck, initial encounter aka vampire
    - W55.2 - Bitten by a cow

## PGP word list

??? info "PGP word list"
        | Hex | Even Word | Odd Word    |
        |-----|-----------|-------------|
        | 00  | aardvark  | adroitness  |
        | 01  | absurd    | adviser     |
        | 02  | accrue    | aftermath   |
        | 03  | acme      | aggregate   |
        | 04  | adrift    | alkali      |
        | 05  | adult     | almighty    |
        | 06  | afflict   | amulet      |
        | 07  | ahead     | amusement   |
        | 08  | aimless   | antenna     |
        | 09  | Algol     | applicant   |
        | 0A  | allow     | Apollo      |
        | 0B  | alone     | armistice   |
        | 0C  | ammo      | article     |
        | 0D  | ancient   | asteroid    |
        | 0E  | apple     | Atlantic    |
        | 0F  | artist    | atmosphere  |
        | 10  | assume    | autopsy     |
        | 11  | Athens    | Babylon     |
        | 12  | atlas     | backwater   |
        | 13  | Aztec     | barbecue    |
        | 14  | baboon    | belowground |
        | 15  | backfield | bifocals    |
        | 16  | backward  | bodyguard   |
        | 17  | banjo     | bookseller  |
        | 18  | beaming   | borderline  |
        | 19  | bedlamp   | bottomless  |
        | 1A  | beehive   | Bradbury    |
        | 1B  | beeswax   | bravado     |
        | 1C  | befriend  | Brazilian   |
        | 1D  | Belfast   | breakaway   |
        | 1E  | berserk   | Burlington  |
        | 1F  | billiard  | businessman |
        | 20  | bison     | butterfat   |
        | 21  | blackjack | Camelot     |
        | 22  | blockade  | candidate   |
        | 23  | blowtorch | cannonball  |
        | 24  | bluebird  | Capricorn   |
        | 25  | bombast   | caravan     |
        | 26  | bookshelf | caretaker   |
        | 27  | brackish  | celebrate   |
        | 28  | breadline | cellulose   |
        | 29  | breakup   | certify     |
        | 2A  | brickyard | chambermaid |
        | 2B  | briefcase | Cherokee    |
        | 2C  | Burbank   | Chicago     |
        | 2D  | button    | clergyman   |
        | 2E  | buzzard   | coherence   |
        | 2F  | cement    | combustion  |
        | 30  | chairlift | commando    |
        | 31  | chatter   | company     |
        | 32  | checkup   | component   |
        | 33  | chisel    | concurrent  |
        | 34  | choking   | confidence  |
        | 35  | chopper   | conformist  |
        | 36  | Christmas | congregate  |
        | 37  | clamshell | consensus   |
        | 38  | classic   | consulting  |
        | 39  | classroom | corporate   |
        | 3A  | cleanup   | corrosion   |
        | 3B  | clockwork | councilman  |
        | 3C  | cobra     | crossover   |
        | 3D  | commence  | crucifix    |
        | 3E  | concert   | cumbersome  |
        | 3F  | cowbell   | customer    |
        | 40  | crackdown | Dakota      |
        | 41  | cranky    | decadence   |
        | 42  | crowfoot  | December    |
        | 43  | crucial   | decimal     |
        | 44  | crumpled  | designing   |
        | 45  | crusade   | detector    |
        | 46  | cubic     | detergent   |
        | 47  | dashboard | determine   |
        | 48  | deadbolt  | dictator    |
        | 49  | deckhand  | dinosaur    |
        | 4A  | dogsled   | direction   |
        | 4B  | dragnet   | disable     |
        | 4C  | drainage  | disbelief   |
        | 4D  | dreadful  | disruptive  |
        | 4E  | drifter   | distortion  |
        | 4F  | dropper   | document    |
        | 50  | drumbeat  | embezzle    |
        | 51  | drunken   | enchanting  |
        | 52  | Dupont    | enrollment  |
        | 53  | dwelling  | enterprise  |
        | 54  | eating    | equation    |
        | 55  | edict     | equipment   |
        | 56  | egghead   | escapade    |
        | 57  | eightball | Eskimo      |
        | 58  | endorse   | everyday    |
        | 59  | endow     | examine     |
        | 5A  | enlist    | existence   |
        | 5B  | erase     | exodus      |
        | 5C  | escape    | fascinate   |
        | 5D  | exceed    | filament    |
        | 5E  | eyeglass  | finicky     |
        | 5F  | eyetooth  | forever     |
        | 60  | facial    | fortitude   |
        | 61  | fallout   | frequency   |
        | 62  | flagpole  | gadgetry    |
        | 63  | flatfoot  | Galveston   |
        | 64  | flytrap   | getaway     |
        | 65  | fracture  | glossary    |
        | 66  | framework | gossamer    |
        | 67  | freedom   | graduate    |
        | 68  | frighten  | gravity     |
        | 69  | gazelle   | guitarist   |
        | 6A  | Geiger    | hamburger   |
        | 6B  | glitter   | Hamilton    |
        | 6C  | glucose   | handiwork   |
        | 6D  | goggles   | hazardous   |
        | 6E  | goldfish  | headwaters  |
        | 6F  | gremlin   | hemisphere  |
        | 70  | guidance  | hesitate    |
        | 71  | hamlet    | hideaway    |
        | 72  | highchair | holiness    |
        | 73  | hockey    | hurricane   |
        | 74  | indoors   | hydraulic   |
        | 75  | indulge   | impartial   |
        | 76  | inverse   | impetus     |
        | 77  | involve   | inception   |
        | 78  | island    | indigo      |
        | 79  | jawbone   | inertia     |
        | 7A  | keyboard  | infancy     |
        | 7B  | kickoff   | inferno     |
        | 7C  | kiwi      | informant   |
        | 7D  | klaxon    | insincere   |
        | 7E  | locale    | insurgent   |
        | 7F  | lockup    | integrate   |
        | 80  | merit     | intention   |
        | 81  | minnow    | inventive   |
        | 82  | miser     | Istanbul    |
        | 83  | Mohawk    | Jamaica     |
        | 84  | mural     | Jupiter     |
        | 85  | music     | leprosy     |
        | 86  | necklace  | letterhead  |
        | 87  | Neptune   | liberty     |
        | 88  | newborn   | maritime    |
        | 89  | nightbird | matchmaker  |
        | 8A  | Oakland   | maverick    |
        | 8B  | obtuse    | Medusa      |
        | 8C  | offload   | megaton     |
        | 8D  | optic     | microscope  |
        | 8E  | orca      | microwave   |
        | 8F  | payday    | midsummer   |
        | 90  | peachy    | millionaire |
        | 91  | pheasant  | miracle     |
        | 92  | physique  | misnomer    |
        | 93  | playhouse | molasses    |
        | 94  | Pluto     | molecule    |
        | 95  | preclude  | Montana     |
        | 96  | prefer    | monument    |
        | 97  | preshrunk | mosquito    |
        | 98  | printer   | narrative   |
        | 99  | prowler   | nebula      |
        | 9A  | pupil     | newsletter  |
        | 9B  | puppy     | Norwegian   |
        | 9C  | python    | October     |
        | 9D  | quadrant  | Ohio        |
        | 9E  | quiver    | onlooker    |
        | 9F  | quota     | opulent     |
        | A0  | ragtime   | Orlando     |
        | A1  | ratchet   | outfielder  |
        | A2  | rebirth   | Pacific     |
        | A3  | reform    | pandemic    |
        | A4  | regain    | Pandora     |
        | A5  | reindeer  | paperweight |
        | A6  | rematch   | paragon     |
        | A7  | repay     | paragraph   |
        | A8  | retouch   | paramount   |
        | A9  | revenge   | passenger   |
        | AA  | reward    | pedigree    |
        | AB  | rhythm    | Pegasus     |
        | AC  | ribcage   | penetrate   |
        | AD  | ringbolt  | perceptive  |
        | AE  | robust    | performance |
        | AF  | rocker    | pharmacy    |
        | B0  | ruffled   | phonetic    |
        | B1  | sailboat  | photograph  |
        | B2  | sawdust   | pioneer     |
        | B3  | scallion  | pocketful   |
        | B4  | scenic    | politeness  |
        | B5  | scorecard | positive    |
        | B6  | Scotland  | potato      |
        | B7  | seabird   | processor   |
        | B8  | select    | provincial  |
        | B9  | sentence  | proximate   |
        | BA  | shadow    | puberty     |
        | BB  | shamrock  | publisher   |
        | BC  | showgirl  | pyramid     |
        | BD  | skullcap  | quantity    |
        | BE  | skydive   | racketeer   |
        | BF  | slingshot | rebellion   |
        | C0  | slowdown  | recipe      |
        | C1  | snapline  | recover     |
        | C2  | snapshot  | repellent   |
        | C3  | snowcap   | replica     |
        | C4  | snowslide | reproduce   |
        | C5  | solo      | resistor    |
        | C6  | southward | responsive  |
        | C7  | soybean   | retraction  |
        | C8  | spaniel   | retrieval   |
        | C9  | spearhead | retrospect  |
        | CA  | spellbind | revenue     |
        | CB  | spheroid  | revival     |
        | CC  | spigot    | revolver    |
        | CD  | spindle   | sandalwood  |
        | CE  | spyglass  | sardonic    |
        | CF  | stagehand | Saturday    |
        | D0  | stagnate  | savagery    |
        | D1  | stairway  | scavenger   |
        | D2  | standard  | sensation   |
        | D3  | stapler   | sociable    |
        | D4  | steamship | souvenir    |
        | D5  | sterling  | specialist  |
        | D6  | stockman  | speculate   |
        | D7  | stopwatch | stethoscope |
        | D8  | stormy    | stupendous  |
        | D9  | sugar     | supportive  |
        | DA  | surmount  | surrender   |
        | DB  | suspense  | suspicious  |
        | DC  | sweatband | sympathy    |
        | DD  | swelter   | tambourine  |
        | DE  | tactics   | telephone   |
        | DF  | talon     | therapist   |
        | E0  | tapeworm  | tobacco     |
        | E1  | tempest   | tolerance   |
        | E2  | tiger     | tomorrow    |
        | E3  | tissue    | torpedo     |
        | E4  | tonic     | tradition   |
        | E5  | topmost   | travesty    |
        | E6  | tracker   | trombonist  |
        | E7  | transit   | truncated   |
        | E8  | trauma    | typewriter  |
        | E9  | treadmill | ultimate    |
        | EA  | Trojan    | undaunted   |
        | EB  | trouble   | underfoot   |
        | EC  | tumor     | unicorn     |
        | ED  | tunnel    | unify       |
        | EE  | tycoon    | universe    |
        | EF  | uncut     | unravel     |
        | F0  | unearth   | upcoming    |
        | F1  | unwind    | vacancy     |
        | F2  | uproot    | vagabond    |
        | F3  | upset     | vertigo     |
        | F4  | upshot    | Virginia    |
        | F5  | vapor     | visitor     |
        | F6  | village   | vocalist    |
        | F7  | virus     | voyager     |
        | F8  | Vulcan    | warranty    |
        | F9  | waffle    | Waterloo    |
        | FA  | wallet    | whimsical   |
        | FB  | watchword | Wichita     |
        | FC  | wayside   | Wilmington  |
        | FD  | willow    | Wyoming     |
        | FE  | woodlark  | yesteryear  |
        | FF  | Zulu      | Yucatan     |

## NATO

Letters

| Symbol | Code word      | DIN 5009 (2022) IPA | ICAO (1950) IPA                | respelling                  |
|--------|----------------|---------------------|--------------------------------|-----------------------------|
| A      | Alfa  [sic]    | ˈalfa               | ˈælfa                          | AL fah                      |
| B      | Bravo          | ˈbravo              | ˈbraːˈvo  [sic]                | BRAH voh                    |
| C      | Charlie        | ˈtʃali or ˈʃali     | ˈtʃɑːli or ˈʃɑːli              | CHAR lee or SHAR lee        |
| D      | Delta          | ˈdɛlta              | ˈdeltɑ                         | DELL tah                    |
| E      | Echo           | ˈɛko                | ˈeko                           | ECK oh                      |
| F      | Foxtrot        | ˈfɔkstrɔt           | ˈfɔkstrɔt                      | FOKS trot                   |
| G      | Golf           | ˈɡɔlf               | ɡʌlf  [sic]                    | golf                        |
| H      | Hotel          | hoˈtɛl              | hoːˈtel                        | ho TELL                     |
| I      | India          | ˈɪndia              | ˈindi.ɑ                        | IN dee ah                   |
| J      | Juliett  [sic] | ˈdʒuliˈɛt           | ˈdʒuːli.ˈet                    | JEW lee ETT                 |
| K      | Kilo           | ˈkilo               | ˈkiːlo                         | KEY loh                     |
| L      | Lima           | ˈlima               | ˈliːmɑ                         | LEE mah                     |
| M      | Mike           | ˈmai̯k              | mɑik                           | mike                        |
| N      | November       | noˈvɛmba            | noˈvembə                       | no VEM ber                  |
| O      | Oscar          | ˈɔska               | ˈɔskɑ                          | OSS cah                     |
| P      | Papa           | paˈpa               | pəˈpɑ                          | pah PAH                     |
| Q      | Quebec         | keˈbɛk  [sic]       | keˈbek                         | keh BECK                    |
| R      | Romeo          | ˈromio              | ˈroːmi.o                       | ROW me oh                   |
| S      | Sierra         | siˈɛra              | siˈerɑ                         | see AIR rah                 |
| T      | Tango          | ˈtaŋɡo              | ˈtænɡo                         | TANG go                     |
| U      | Uniform        | ˈjunifɔm or ˈunifɔm | ˈjuːnifɔːm or ˈuːnifɔrm  [sic] | YOU nee form or OO nee form |
| V      | Victor         | ˈvɪkta              | ˈviktɑ                         | VIK tah                     |
| W      | Whiskey        | ˈwɪski              | ˈwiski                         | WISS key                    |
| X      | Xray, x-ray    | ˈɛksrei̯            | ˈeksˈrei  [sic]                | ECKS ray                    |
| Y      | Yankee         | ˈjaŋki              | ˈjænki                         | YANG key                    |
| Z      | Zulu           | ˈzulu               | ˈzuːluː                        | ZOO loo                     |

Numbers

| Symbol          | Code word            | English                        | French                 | CCEB 2016        | FAA            | ITU-R 2007 (WRC-07)     | IMO (French)        | U.S. Navy 1957 | U.S. Army           |
|-----------------|----------------------|--------------------------------|------------------------|------------------|----------------|-------------------------|---------------------|----------------|---------------------|
| 1               | One, unaone          | WUN /'wʌn/                     | OUANN [ˈwan]           | wun              | wun            | OO-NAH-WUN              | OUNA-OUANN          | wun            | wun, won (USMC)[24] |
| 2               | Two, bissotwo        | TOO /ˈtuː/                     | TOU [ˈtu]              | too              | too            | BEES-SOH-TOO            | BIS-SO-TOU          | too            | too                 |
| 3               | Three, terrathree    | TREE /ˈtriː/                   | TRI [ˈtri]             | tree             | tree           | TAY-RAH-TREE            | TÉ-RA-TRI           | thuh-ree       | tree                |
| 4               | Four, kartefour      | FOW-er /ˈfoʊ.ə/                | FO eur [ˈfo.ør]        | FOW-er           | fow-er         | KAR-TAY-FOWER           | KAR-TÉ-FO-EUR       | fo-wer         | fow-er              |
| 5               | Five, pantafive      | FIFE /ˈfaɪf/                   | FA ÏF  [sic] [ˈfaif]   | fife             | fife           | PAN-TAH-FIVE            | PANN-TA-FAIF        | fi-yiv         | fife                |
| 6               | Six, soxisix         | SIX /ˈsɪks/                    | SIKS [ˈsiks]           | six              | six            | SOK-SEE-SIX             | SO-XI-SICKS         | six            | six                 |
| 7               | Seven, setteseven    | SEV-en /ˈsɛv(ə)n/              | SÈV n [ˈsɛv.n]         | SEV-en           | sev-en         | SAY-TAY-SEVEN           | SÉT-TÉ-SEV'N  [sic] | seven          | sev-en              |
| 8               | Eight, oktoeight     | AIT /ˈeɪt/                     | EÏT [ˈeit]             | ait              | ait            | OK-TOH-AIT              | OK-TO-EIT           | ate            | ait                 |
| 9               | Nine, novenine[25]   | NIN-er /ˈnaɪnə/                | NAÏ neu [ˈnainø]       | NINE-er          | nin-er         | NO-VAY-NINER            | NO-VÉ-NAI-NEU       | niner          | nin-er              |
| 0               | Zero, nadazero       | ZE-RO[26] /ˈziːˈroʊ/           | ZI RO [ˈziˈro]         | ZE-ro            | ze-ro / zee-ro | NAH-DAH-ZAY-ROH[27][28] | NA-DA-ZE-RO[27][28] | zero           | ze-ro               |
| 00              | Hundred              | HUN-dred /ˈhʌndrɛd/            | HUN-dred [ˈhœ̃drɛd]    | (zero zero)      | (hundred)      |                         |                     | hun-dred       |                     |
| 000             | Thousand             | TOU-SAND[26] /ˈtaʊˈzænd/       | TAOU ZEND [ˈtauˈzɑ̃d]  | (zero zero zero) | (thousand)     |                         |                     | thow-zand      | tou-sand            |
| (decimal point) | Decimal, (FAA) point | DAY-SEE-MAL[26] /ˈdeɪˈsiːˈmæl/ | DÈ SI MAL [ˈdɛˈsiˈmal] | (decimal)        | (point)        | DAY-SEE-MAL             | DÉ-SI-MAL           |                |                     |

## Timezone Codes

| Time zone name     | Degrees longitude  | Designation  letter | Zone description | Offset              |
|--------------------|--------------------|---------------------|------------------|---------------------|
| Alfa Time Zone     | 7.5 E to 22.5 E    | A                   | -1               | UTC+01:00           |
| Bravo Time Zone    | 22.5 E to 37.5 E   | B                   | -2               | UTC+02:00           |
| Charlie Time Zone  | 37.5 E to 52.5 E   | C                   | -3               | UTC+03:00           |
| Delta Time Zone    | 52.5 E to 67.5 E   | D                   | -4               | UTC+04:00           |
| Echo Time Zone     | 67.5 E to 82.5 E   | E                   | -5               | UTC+05:00           |
| Foxtrot Time Zone  | 82.5 E to 97.5 E   | F                   | -6               | UTC+06:00           |
| Golf Time Zone     | 97.5 E to 112.5 E  | G                   | -7               | UTC+07:00           |
| Hotel Time Zone    | 112.5 E to 127.5 E | H                   | -8               | UTC+08:00           |
| India Time Zone    | 127.5 E to 142.5 E | I                   | -9               | UTC+09:00           |
| Kilo Time Zone     | 142.5 E to 157.5 E | K                   | -10              | UTC+10:00           |
| Lima Time Zone     | 157.5 E to 172.5 E | L                   | -11              | UTC+11:00           |
| Mike Time Zone     | 172.5 E to 180     | M                   | -12              | UTC+12:00           |
| November Time Zone | 7.5 W to 22.5 W    | N                   | +1 or -13        | UTC−01:00 UTC+13:00 |
| Oscar Time Zone    | 22.5 W to 37.5 W   | O                   | +2               | UTC−02:00           |
| Papa Time Zone     | 37.5 W to 52.5 W   | P                   | +3               | UTC−03:00           |
| Quebec Time Zone   | 52.5 W to 67.5 W   | Q                   | +4               | UTC−04:00           |
| Romeo Time Zone    | 67.5 W to 82.5 W   | R                   | +5               | UTC−05:00           |
| Sierra Time Zone   | 82.5 W to 97.5 W   | S                   | +6               | UTC−06:00           |
| Tango Time Zone    | 97.5 W to 112.5 W  | T                   | +7               | UTC−07:00           |
| Uniform Time Zone  | 112.5 W to 127.5 W | U                   | +8               | UTC−08:00           |
| Victor Time Zone   | 127.5 W to 142.5 W | V                   | +9               | UTC−09:00           |
| Whiskey Time Zone  | 142.5 W to 157.5 W | W                   | +10              | UTC−10:00           |
| X-ray Time Zone    | 157.5 W to 172.5 W | X                   | +11              | UTC−11:00           |
| Yankee Time Zone   | 172.5 W to 180     | Y                   | +12              | UTC−12:00           |
| Zulu Time Zone     | 7.5 W to 7.5 E     | Z                   | 0                | UTC+00:00           |

## Phone Codes

Android

- Testmenü öffnen: `*#0*#`
- Erweitertes Testmenü öffnen: `*#*#4636*#*#`
- Akkuinformationen anzeigen: `*#0228#`
- Servicemenü aufrufen: `*#197328640#`
- Firmware- Version abfragen: `*#1234#`
- Hardware- Version abfragen: `*#2222#`
- USB- Einstellungen: `*#0808#`
- Spezialeinstellungen: `3845#*855#`
- Spezialeinstellungen (D855): `*#546368#*855#`

iPhone

- Eigene Rufnummer abfragen (nur Telekom): `*135#`
- Eigene Rufnummer von SIM- Karte abfragen: `*#5005*74663#`
- SMS- Zentrale abfragen: `*#5005*7672#`
- Enhanced Full Rate- Modus aktivieren: `*3370#`
- Enhanced Full Rate- Modus deaktivieren: `#3370#`
- Half Rate- Modus aktivieren: `*4720#`
- Half Rate- Modus deaktivieren: `#4720#`
- Feldtestmodus aktivieren: `*3001#12345#*`
- SIM Clock Stop- Modus Status: `*#746025625#`
- Gerätedetails abfragen: `*#*#4636#*#*`
- internen Gerätenamen abfragen: `*#1111#`
- Hardware- Revision abfragen: `*#2222#`
- schnelles Herunterfahren aktivieren: `*#7594#`
- Mailboxeinstellungen abfragen: `*#5005*86#`

GSM Codes

- Auslesen der Handy- Seriennummer IMEI: `*#06#`
- PIN ändern: `**04*(alter PIN)*(neuer PIN)*(neuer PIN)#`
- SIM- Karte mit PUK entsperren: `**05*(PUK)*(neuer PIN)*(neuer PIN)#`
- PIN2 ändern: `**042*(alter PIN2)*(neuer PIN2)*(neuer PIN2)#`
- PIN2 mit PUK entsperren: `**052*(PUK)*(neuer PIN2)*(neuer PIN2)#`
