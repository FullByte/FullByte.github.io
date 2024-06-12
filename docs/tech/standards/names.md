# Names

Naming things is hard.

## Zooko's Triangle

Zooko's Triangle is a theory proposed by Zooko Wilcox-O'Hearn that suggests a namespace in a computer network can only simultaneously satisfy two out of the three properties of being decentralized, secure, and meaningful. These properties are desirable in large, public namespaces and are defined as follows:

- Decentralized: There is no central authority issuing names or deciding their validity. Instead, the namespace is managed by multiple authorities who do not fully trust each other. The key criterion is the absence of a hierarchical trust relationship, allowing for arbitrarily constructed trust networks.
- Secure: The integrity of name mappings is maintained, meaning that an attacker cannot manipulate a mapping without the attempt being detected. Security ensures that the connections between names and addresses or other values remain unaltered and trustworthy.
- Meaningful: A name's meaningfulness means it is human-readable and a person can derive significance from it. Meaningful names are user-chosen and comprehensible, as opposed to automatically generated, seemingly random strings.

The theory asserts that it is impossible to fully achieve all three properties simultaneously in a namespace. Therefore, only two of these properties can be optimized at the same time. For example:

- A system might be decentralized and secure, but the names might not be meaningful (e.g., cryptographic hashes).
- A system might be decentralized and meaningful, but it may lack security (e.g., a peer-to-peer network with user-defined names but inadequate security measures).
- A system might be secure and meaningful, but it would be centralized (e.g., a centrally managed domain name system where a central authority issues and manages names).

The challenge lies in finding practical solutions that offer a balanced compromise between these three properties.

## Falsehoods

### Addresses

#### Incorrect assumptions on addresses

Addressing is a fertile ground for incorrect assumptions, because everyone’s used to dealing with addresses and 99% of the time they seem so simple. Below are some incorrect assumptions:

- An address will start with, or at least include, a building number.
Counterexample: Royal Opera House, Covent Garden, London, WC2E 9DD, United Kingdom.
- When there is a building number, it will be all-numeric.
Counterexample: 1A Egmont Road, Middlesbrough, TS4 2HT
4-5 Bonhill Street, London, EC2A 4BX
- No buildings are numbered zero
Counterexample: 0 Egmont Road, Middlesbrough, TS4 2HT
- Well, at the very least no buildings have negative numbers
Guy Chisholm provided this counterexample: Minusone Priory Road, Newbury, RG14 7QS
(none of the databases I’ve checked render this as -1)
- We can put those funny numbers into the building name field, as no buildings have both a name and a funny number
Counterexample: Idas Court, 4-6 Princes Road, Hull, HU5 2RD
- When there’s a building name, there won’t be a building number (or vice-versa)
Counterexample: Flat 1.4, Ziggurat Building, 60-66 Saffron Hill, London, EC1N 8QX, United Kingdom
- A building number will only be used once per street
The difference between 50 Ammanford Road, Tycroes, Ammanford, SA18 3QJ and 50 Ammanford Road, Llandybie, Ammanford, SA18 3YF is about 4 miles (Google Maps).
- When there’s line with a number in an address, it’s the building number.
Counterexample: Flat 18, Da Vinci House, 44 Saffron Hill, London, EC1N 8FH, United Kingdom
You also get suite numbers, floor numbers, unit numbers, and organizations with numbers in their names.
Adrien Piérard contributes an address from Japan with fifteen digits in five separate numbers. The format is: 980 0804 (zip code), Miyagi-ken (prefecture) Sendai-shi (city) Aoba-ku (district) Kokubuncho (Subdistrict) 4-10-20 (Sub-sub-district-number block-number building-number) Sendai (building name) 401 (flat number).
- OK, the first line starting with a number then
Counterexample: 3 Store, 311-318 High Holborn, London, WC1V 7BN
- A building will only have one number
Benton Lam offers this address from the Hong Kong Special Administrative Region - it has both a number on its road (14) and in its group of buildings (3): 15/F, Cityplaza 3, 14 TaiKoo Wan Road, Island East, HKSAR
- A building name won’t also be a number
Ben Tilly reports on Ten Post Office Sq, Boston MA 02109 USA - which is not, reportedly, the same as 10 Post Office Sq, Boston MA 02109 USA.
- A street with a building A will not also have a building Alpha
Douglas Perreault reports he lived in a block within a condo association; it was a large association, with blocks A through Z then Alpha, Beta, Gamma, Delta, and Theta. Mail and deliveries were often misrouted from block Alpha to block A and vice-versa. His address at the time was: 14100 N 46th St., Alpha 39, Tampa, FL 33613
- When there’s a numbered street and a house number, there will be a separator between them
Another from Jan Jongboom: Gondel 2695, Lelystad, means area Gondel, street 26, number 95
- Street names always end in descriptors like ‘street’, ‘avenue’, ‘drive’, ‘square’, ‘hill’ or ‘view’
They don’t always - for example: Piccadilly, London, W1J 9PN
- OK, but when they do have a descriptor there will only be one
A street name can be entirely descriptors: 17 Hill Street, London, W1J 5LJ
- OK, but when they do have a descriptor it will be at the end
French addresses use prefix descriptors like ‘rue’, ‘avenue’, ‘place’ and ‘allee’.
- OK, but if there’s a descriptor it’ll be at the start or end of the street name.
Or the middle, like 3 Bishops Square Business Park, Hatfield, AL10 9NA
- OK, but at the very least you wouldn’t name a town Street
Actually there’s a town called Street in Somerset, UK.
- Street names don’t end in numbers
Jan Jongboom reports streets can be numbered in the Netherlands - for example, Plein 1944 in Nijmegen.
- Street numbers don’t contain fractions
Dan, Fred Kroon, David Underwood and Daniel Dickison submitted examples of fractional street numbers like 43rd ½ St, Pittsburgh, PA, and of fractional building numbers. These can be written in unicode (43rd ½ St), as a fraction with a slash (43 1/2) or as a decimal (43.5)
- Street names don’t reoccur in the same city
Here’s a map of the following addresses:
        ○ High Street, London, W3 6LJ
        ○ High Street, London, W5 5DB
        ○ High Street, London, N8 7PB
        ○ High Street, London, SE25 6EP
        ○ High Street, London, E13 0AJ
        ○ High Street, London, E17 7LD
        ○ High Street, London, NW10 4LX
        ○ Islington High Street, London, N1 9TR
        ○ Shoreditch High Street, London, E1 6PG
        ○ Camden High Street, London, NW1 0JH
        ○ Kensington High Street, London, W14 8NL
        ○ Lewisham High Street, London, SE13 6AD
        ○ High Street Wimbledon, London, SW19 5DX
        ○ High Street Wanstead, London, E11 2AJ
        ○ High Street Colliers Wood, London, SW19 2AE
        ○ High Street North, London, E6 2HJ
- But street names don’t recurr in close proximity
Julian Fleischer provides an example from Bocholt in Germany showing several roads in close proximity all called Up de Welle.
- An address will be comprised of road names
Kirk Kerekes spent several years using an address of the form "2 mi N then 3 mi W of Jennings, OK 74038" which regularly got successful deliveries. Mike Riley used to mail the Very Large Array radio telescope at "50 miles (80 km) West of Socorro, New Mexico, USA"
Sam pointed me to Menomonee Falls where houses are addressed using Milwaukee County’s grid system instead of house numbers - giving addresses like N88 W16541 Foobar St.
Andy Monat sent the following address example, from a semester abroad program at Tulane University: CIAPA, 50 meters north of the Hypermas/Walmart of Curridabat, San Jose, Costa Rica. Adrien Piérard and Luke Allardyce point out street names are seldom used in Japan - instead, districts and blocks numbers are used. A 2002 World Press Review report gave this sample address: From where the Chinese restaurant used to be, two blocks down, half a block toward the lake, next door to the house where the yellow car is parked, Managua, Nicaragua. Stig Brautaset pointed out a BBC article about post in Kabul gives this example: "Hamid Jaan, behind Darul-Aman palace". Nathan Fellman reports similar addressing is used in Nicaragua and Costa Rica.
Paul Puschmann and Tibor Schütz pointed out the city of Mannheim in Germany is sometimes called Quadratestadt (City of Squares) as the city centre is arranged in a grid, with blocks assigned a letter (along the north-south axis) and a number (along the east-west axis) then buildings numbered by block number. So an example address at numbers 6 to 13 on block R 5 would be: Institut für Deutsche Sprache, R 5, 6-13, D-68161 Mannheim
Leoni Lubbinge gives an example of a South African address: Part 84, Strydfontein 306 JR, Pretoria which means the 84th plot of the farm Strydfontein 306 JR.
- A road will have a name
Plenty of roads like driveways, onramps and the aisles of carparks don’t have names.
- A road will only have one name
Many different roads, from Goswell Road in London to Regent Road in Edinburgh, make up the 410 mile A1. And while there may only be one "1 Goswell Road" and only one "1 Regent Road" there are multiple buildings numbered 1 on the road designated A1.
Roads may also be named in multiple languages. For example, in Ireland roads may be named in both English and Irish
- Addresses will only have one street
The Royal Mail have what they call a ‘dependent street’ - for example: 6 Elm Avenue, Runcorn Road, Birmingham, B12 8QX, United Kingdom (Runcorn Road is the street, Elm Avenue is the stubby ‘dependent street’ and isn’t unique within the city. Google Maps )
Another counterexample: Rogue Hair, 1 Hopton Parade, Streatham High Road, London, SW16 6EP (Streatham High Road is the street. Hopton Parade is a little row of shops on the road - Google Maps )
- Addresses will have a street
The Royal Mail will deliver to certain premises by name, such as farms and cottages. Example: Oakland, Fairseat, Sevenoaks, TN15 7LT, United Kingdom (Fairseat is the town - this is actually on Vigo Road. Google Maps )
- An address will include a state in the US sense.
Counterexample: Any address in the United Kingdom.
- Addresses will have something other than the organization and city name.
Large recipients of mail are sometimes addressed by organization alone - for example: Electoral Reform Society Ltd, London, N1 1RS, United Kingdom
- An address will have a county
Iain Parris and Naath both pointed out that, while many websites ask users for a county, not all countries use them in addressing. For example, the Royal Mail stopped using postal counties in 1996.
Yves Daoust reports that in Belgium an address only requires a street, postcode and city; example: Boulevard Frère Orban, 27, 4000 Liège. Erik Engheim reports that in Norway Oslo is a By (city), Tettsted (urban area), Kommune (municipality) and Fylke (county) but it usually only appears once in a written address.
- An address require both a city and a country
jzwinck points out Singapore is a city-state, leading to addresses like Singapore, Singapore - or even Singapore, Singapore, Singapore if you demand a city, county and country.
- You can’t have two towns cities with the same name in the same country
Sure you can - for example the UK has three towns called Newport.
Jan Jongboom reports from the Netherlands, where there are two cities called Eursinge - in the same province!
- OK, but those cities won’t have duplicate street names
        ○ 10 High Street, Newport, PO30 1SS
        ○ 10 High Street, Newport, NP20 1FQ
        ○ 10 High Street, Newport, TF10 7AN
- An address will have a postcode
Richard Fletcher, Lee Hosty, Paul O’Nolan, Simon Diab, Tony Finn, Donal Maccarthy, mark lynch and Donovan all pointed out countries like the Republic of Ireland have addresses without postcodes, or only have postcodes in certain parts of the country. Danny Angus points out this is also the case in Hong Kong.
Jessica Enders points out the post-paid address of the AEC: Australian Electoral Commission, Reply Paid 9867, your capital city
- The user will know their postal code/zip code.
Most users will, of course, but I’ve seen incorrect postcodes on corporate letterheads! Misreading handwritten postcodes seems like a common one.
- A single postcode will be larger than a single building
Although zip codes in the US usually cover very large areas, Anthony Elizondo points out some buildings have their own zip codes - like the Empire State Building (10118)
In the UK, alphanumeric postcodes are typically much more precise than US zip codes.
- OK, but you don’t get multiple postcodes per building
Graham Lee points out DVLA Swansea (that’s the whole address), where different departments are identified by postcode: V5Cs are processed at SA99 1BA, driving licences at SA99 1AB and so on.
Malcolm Gilbert points out this example, with five postcodes for five departments:
        ○ London Borough of Enfield, Civic Centre, Silver Street, ENFIELD, EN1 3ES
        ○ Returning Officer, London Borough of Enfield, Civic Centre, Silver Street, ENFIELD, EN1 9SA
        ○ Edmonton, London Borough of Enfield, Civic Centre, Silver Street, ENFIELD, EN1 9SB
        ○ Enfield North, London Borough of Enfield, Civic Centre, Silver Street, ENFIELD, EN1 9SD
        ○ Enfield Southgate, London Borough of Enfield, Civic Centre, Silver Street, ENFIELD, EN1 3ZW
        ○ But the Enfield council website contact page lists their postcode as EN1 3XY - which the Royal Mail think is a PO Box at the sorting office.
- A single postcode will only cover a few tens of addresses / customers
Mostly this is reasonable in the UK, but there are certain exceptions. For example CV4 7AL is the postcode of the University of Warwick - one postcode for 6,000 students living on campus, and academics/administrators working on campus.
Also, if your customers get things delivered to them when they’re on holiday, lots of customers may have the same holiday parks on their accounts.
Some addresses correspond to ‘flexible office spaces’ and organizations that offer PO Boxes that sound like fancy offices. The Royal Mail lists more than 90 organizations operating out of Tower 42, 25 Old Broad Street, London, EC2N 1HQ. Holiday parks and cottages may also appear on many customers’ accounts.
Victor Nicollet contributes the example of French postcode 75015, representing the XVth arrondissement of Paris, which covers over 230,000 people.
- A zip code corresponds to a single city
Mike Cohen reports zip code 33334 covers 3 cities: Oakland Park, Wilton Manors, and Fort Lauderdale, all in Florida.
- Zip codes don’t start with a zero
Some Brazilian zip codes do according to speeder, as do Israeli postcodes for army units. Jessica Enders and Frank Malcolm pointed out postcodes in the Northern Territory of Australia start with 08; for example the postcode for the city Darwin is 0800. Morsillo Lindsay, Thomas Norris and Jerry B. Altzman point out American addresses in the north east have zip codes starting with zero, for example Ten Post Office Sq, Boston MA 02109, USA; and some zip codes start with two zeros. Mikael Vejdemo-Johansson reports the zip code of Jena in Germany is 07737.
Antti Vikman and Johan Myréen tell me all postcodes in Helsinki, the capital of Finland, all start with two zeroes. Some special codes even start with four zeroes (00002 HELSINKI). Andrew Jones reports the initial digits of French postcodes are the department, and may use a leading zero. Post addressed to 06130 Grasse is correctly delivered to the town in district 06, Alpes Maritimes - but post addressed to 6130 Grasse is first routed to department 61, Orne. klez reports Italian Codice di Avviamento Postale (CAP) numbers can have a leading zero.
- Addresses will have a reasonable number of characters - less than 100, say.
Not when organization and department names can be included in addresses! For example: Department For Environment Food & Rural Affairs (D E F R A), State Veterinary Service, Animal Health Office, Hadrian House, Wavell Drive, Rosehill Industrial Estate, Carlisle, CA1 2TB, United Kingdom
Another example: The Gynaecology Cancer Research Unit, Department of Obstetrics & Gynaecology, St. Bartholomews & The Royal School of Medicine & Dentistry, Charterhouse Square, London, EC1M 6GR, United Kingdom
- But street names will be reasonably short - certainly less than 50 characters
Susanne Schmidt provides the longest street name in Germany: Bischöflich-Geistlicher-Rat-Josef-Zinnbauer-Straße in 84130 Dingolfing, Bavaria
Graham Rhind suggests this 89-character street name in Bihac, Bosnia: Aleja Alije Izetbegovića Prvig Predsjednika Predsjedništva Republika Bosna i Hercegovina
- Five lines and country will cover all cases.
You’ll need 8 lines and country to deliver to: GB Technical Services, Unit W7a, Warwick House, 18 Forge Lane, Minworth Industrial Park, Minworth, Sutton Coldfield, B76 1AH, United Kingdom
- Addresses don’t contain commas (so I can replace newlines with commas then commas with newlines and get back to where I was)
Addresses can contain organization names, and organization names can contain commas. For example: Society of College, National & University Libraries, 102 Euston Street, London, NW1 2HA
- But they don’t contain commas, brackets, apostrophes, hyphens, ampersands, dots or exclamation marks
St. Judes & St. Pauls C of E (Va) Primary School, 10 Kingsbury Road, London, N1 4AZ
1 Acre View, Bo’ness, EH51 9RQ
1 Highview Terrace, Westward Ho!, Bideford, EX39 1AQ (exclamation mark is omitted in some databases)
Flat 1.4, Ziggurat Building, 60-66 Saffron Hill, London, EC1N 8QX, United Kingdom
Kirkland, Lane, Mathias & Perry, North Muskham Prebend Church Street, Southwell, NG25 0HQ
Mark Wallace tells us The Hague in the Netherlands is has multiple official names, one of which is ’s-Gravenhage (not a plural, literally a city name starting apostrophe s and with a hyphen)
Signposts for Station Road East, Grantham, NG31 6HX render it as STATION ROAD (EAST).
More generally, addresses can contain organization names, and organizations can have names like Yahoo! with an exclamation mark. Legislation on company sets out the allowable characters for the UK and it permits company names including ! LTD (company 08209948); @ LTD (company 08209882); $ LTD (company 08209885) and % LTD (company 04487680) as well as a variety of other names I don’t have examples for as the companies house website won’t let me search for them.
- An address will exist in the country’s postal service’s database
Simon Westcott points out databases are only released periodically, so it’s not unusual for new buildings to be omitted.
- An address in the country’s postal service’s database will exist
Royal Mail and Ordnance Survey data can contain demolished buildings, and buildings currently under construction. The Royal Mail even have a database product called Not Yet Built. Temporary postcodes can even be assigned to building sites!
- The address from the postal service database is sufficient to deliver
Christopher Allen points out that people in new blocks of flats and houseboats in boatyards sometimes need to prefix their official address with a boat name or flat number.
- Every address can be expressed in a way that will pass all validators
XaspR8d must have been exasperated by the fact his road is variously known as "S Hwy X", "Highway X" and "South County Rd X" - and related a story of being unable to buy a product as the only addresses that passed a vendor’s address validation wouldn’t pass his bank’s address validation and vice-versa.
Jon Peterson lives in an apartment community that is divided into Quail Ridge Cir, Quail Ridge East Lane and Quail Ridge West Lane. Only the USPS and the city electric utility seem to recognize the "Lane". Everyone else requires it be shortened to "Quail Rdg E" (or W) and reportedly when UPS turns a package over to the USPS it gets returned as undeliverable-no such address.
Susannah Fleming lived on the road the Royal Mail call Top O’The Lane, Brindle, Chorley, PR6 8PA. She reports representations in different databases include:
        ○ Top o’ th’ Lane
        ○ Top o’th’ Lane
        ○ Top oth Lane
        ○ Top o’ the Lane
        ○ Top of the Lane
        ○ Workhouse Lane (a historical name of the road)
        ○ Denham Lane (name of the road continuation)
- Customers will have a fixed address with a fixed location
A developer just a few seats from me recently brought a house boat with the intention of using it as her primary residence. Needless to say, boats can move - including between towns and even countries!
fr0sty points out the State of Illinois catch-all approach to addresses: "IF YOU HAVE NO STREET ADDRESS, below describe your home: list the name of subdivision; cross streets; roads; landmarks; mileage and/or neighbors’ names."
Sharon Freas has dealt with systems supporting "Snowbird" clients, who alternate between addresses with the changing seasons.
- But written addresses don’t change
Addresses can move between counties and administrative districts. For example, I used to live in the county Gwent, but that no longer exists. Addresses may also be assigned new postcodes.
Susanne Schmidt points out cities, streets and entire countries were renamed in eastern europe - for example, when Lenin fell out of favour as a street name. Addresses can be in disputed territories, or even war zones.
Douglas Perreault reports owning a condo that changed address three times; first it was 14100 N 46th St., Alpha 39, Lutz, FL 33549; then a new post office was built and it became 14100 N 46th St., Alpha 39, Tampa, FL 33612; then the ZIP Code changed giving 14100 N 46th St., Alpha 39, Tampa, FL 33613; then the condo association changed to a less error-prone block naming scheme, giving 14410 Hanging Moss Circle, #101, Tampa, FL 33613.
- Postal, traditional and administrative counties all line up, right?
As you can learn from wikipedia’s page on postal counties, even when the Royal Mail used postal counties, they didn’t always line up with administrative counties. And of course administrative regions come and go with changes to local government structures - for example, the county I was born in in no longer exists.
- Military addresses are just like regular addresses
Peter Bailey points out several countries have special military mail to deal with the complexities of delivering to soldiers deployed to other countries, ships at sea and similar; and their addresses don’t always follow conventional address formats. For example, the address BFPO, BF1 4FB is the address of the navy vessel HMS Example.
Ed Schiebel reports the postcodes allocated to Israeli army units roam around with the units.
- An address corresponds to the recipient’s location.
Addresses such as PO boxes are often only as precise as the recipient’s city or sorting office. Jessica Enders tells me the Australian post service Reply Paid addresses (no stamp needed); PO Boxes (Post Office Boxes); GPO Boxes (General Post Office Boxes, in the middle of capital cities only); locked bags; private bags; parcel lockers; parcel collect; "Care of Post Office"; CMA (Community Mail Agent); CPA (Community Postal Agent); CMB (Community Mail Bag) and Mail Service (MS)!
Tibor Schütz points out many post offices have novelty handling of mail to Santa Claus, even going as far as to allocate special postcodes. For example: Santa Claus Nordpolen, Julemandes Postkontor, DK-3900 Nuuk
- An address can be expressed with a single country
Matthieu Valleton got in touch to point out his address on Kerguelen Island (Google Map), a French territory in the Indian Ocean, his address was District de Kerguelen (island), Terres Australes et Antarctiques Françaises (territory), via la Réunion (indicates where the mail should be routed through), France (country)
- Overseas territories aren’t (or are) always included in the postal code system
Monty points out that uncommon political hierarchies can lead to uncommon postal addresses. For example, the entire of the Falkland Islands shares postal code FIQQ 1ZZ. On the other hand, the British Virgin Islands have their own postal code system.
- All addresses with a box number are PO Boxes
David Kuder pointed me to a 1990 article: Risks Digest correspondent Tim Kay had problems getting mail sent to his university campus pigeon hole: Timothy L. Kay, Box 256-80, Pasadena, CA 91125. Reportedly automatic systems changed his zip code to 91102. David Kuder identified this was because all Pasadena PO Boxes were in box 91102.
- Addresses will be written in ASCII or at least Latin characters
Alastair Houghton reminds us the Greek tax office’s address is Χανδρή 1 & Θεσσαλονίκης, Τ.Κ. 18346, Αθήνα
Wikipedia has a photo of a parcel where a Russian/Cyrillic address was displayed on a computer with the wrong character encoding, and transcribed from that. Reportedly a russian postal worker was able to reverse the mapping and deliver the parcel.
@shyhoof wrote an poem about an address label with ó converted, via latin1 and two rounds of HTML entities, into &ATILDE;&SUP3;
- Addresses will be written in the character set of the destination country
Alastair Houghton points out addresses may be written in the character set of the source country.
- But people at least use the same character set for the entire address?
International mail may specify the country in both the source and destination countries’ character sets, so it can be read by postal workers on both ends.
- Addresses will be written from most to least specific
Alastair Houghton provided this example of a Japanese address: 〒100-8994 (zip code), 東京 (tokyo) 都中央区(Chuo-ku) 八重洲一丁目 (Yaesu Chome) 5番3号 (area-block 5 subblock 3), 東京中央郵便局 (Tokyo central post office)
- OK, but they’ll either be in either ascending or descending specificity
Erik Engheim and Jan Jongboom report in Norway and the Netherlands the building number (within street) comes after the street name, but before the town name.
Douglas Perreault reports units within American condo associations may be written below the street name. For example: 14100 (position of condo association on street) N 46th St. (street name), Alpha (block within condo association) 39 (unit within block), Lutz (city), FL (state) 33549 (zip). Likewise, when mailing an individual at a company some people put the person’s name after the company name, but before the street name.
- OK, but at least the same address will always be written in the same order
György Farkas tells me Hungarian addresses can be written in different orders depending on how many lines are available. If you write the address on one line, it’s expressed from less specific to more specific:
{zip} {town}, {street} {buildingNr}.
If there are more lines available, the address starts with the street, and if the country is specified, it comes after the town name:
{street} {buildingNr}.
{zip} {town}, {country}
And if there are no set number of lines, like on an envelope, it’s a bit different again:
{street} {buildingNr}.
{town}
{zip}
{country}
- Building numbers appear before street names
In some countries this is reversed - such as in the Netherlands. For example, Plein 1944 85 D (where Plein 1944 identifies the street, 85 the building and D the flat/apartment).
- Flat names/numbers names appear before building numbers
Toni Cornelissen points out addresses in the The Netherlands, such as: Vroomstraat 1a Rood, 2021HL Haarlem where Vroomstaat is the street, 1a is the building number, and Rood (literally translated as Red) indicates the upper part of the building.
- A building will be within a few hundred meters of a public road
Buildings like farms and country houses can be at the end of a private road or driveway several hundred meters long.
- An address with a street name is always closer to that street than any other
Lots of examples of this. For example: The National Museum of Computing, Bletchley Park, Sherwood Drive, Bletchley, Milton Keynes, MK3 6EB. 70m from Roche Gardens, 346m from Sherwood Drive, but only accessible by entering Bletchley Park from Sherwood Drive.
- The number of buildings is the difference between the highest and lowest building numbers
Tibor Schütz points out building numbers may be skipped - for example, on a street where even-numbered buildings are on one side, odd numbers on the other; multiple buildings sharing the same number (such as where a new house has been built) and buildings with more than one number.
- Real place names won’t contain rude words
It’s not just Middlesex and Scunthorpe you have to check for; Gary Gale has compiled a map of rude-sounding place names.
- A customer will only want reminders mailed to single address
John Dye reports that many doctors’ offices, dentists and so on are unable to mail both of a child’s divorced parents.
- Each person has exactly one address
Tibor Schütz points out people often have a different home and work address.

#### Places have only one official name

- Buildings do not move. In Zürich, a 6200 ton building was moved by 60 meters to make way for railway tracks
- Countries have capitals. Switzerland does not. The government is currently in Bern, but the city is not the capital.
- Language codes will match the country code of the country they are associated with. The country code for Japan is jp, the language code is ja.
- Place names are usually old, often created before the language and their rules have been stabilised, so this does not hold. For instance, the rule says in german the sequence "ue" is equivalent to "ü". This rule works because the "üe" sound has died out in german. The hill over Zürich is named "Üetliberg" (and pronounced as such).
- Place names can be written with the exhaustive character set of a country. That would be true if street where never named after foreigners with strange accents in their names. There is a Béla Bartók square in Paris. The "ó" is not valid in French.
- Place names can be written with the usual character set of a country. One of the Kergelen islands (part of France) is called Île de Croÿ, most french persons have no clue how to type the "ÿ" character.
- Places have only one official address. There is a dam in Geneva than span the Rhône and therefore the border. The dam has two street addresses, one in Switzerland, one in France.
- Places have only one official name per language. That might be true in an ultra-centralized state which never changes its mind. The hill behind my flat has two different names, depending on the maps. On the topographic maps (used by the army) the name is "Äntlisberg", while on the city map, the name is "Entlisberg", both are official. In Taipei, the romanized street names used to use different romanisation rules depending on the quarter, so the official street name changes.
- Some places have multiple languages, so multiple names, which can be quite different: Genève, Genf, Ginevra.
- Street adresses contain street names. In many remote places in Europe, the hamlet name is considered a sufficient address.
Place names follow the character rules of the language

### Names

#### Wrong assumptions about names

So, as a public service, I’m going to list assumptions your systems probably make about names.  All of these assumptions are wrong.  Try to make less of them next time you write a system which touches names.

All of these assumptions are wrong:

- Alright alright but surely people’s names are diverse enough such that no million people share the same name.
- I can safely assume that this dictionary of bad words contains no people’s names in it.
- My system will never have to deal with names from China... Or Japan.. Or Korea.
- Or Ireland, the United Kingdom, the United States, Spain, Mexico, Brazil, Peru, Russia, Sweden, Botswana, South Africa, Trinidad, Haiti, France, or the Klingon Empire, all of which have "weird" naming schemes in common use.
- People have exactly N names, for any value of N.
- People have exactly one canonical full name.
- People have exactly one full name which they go by.
- People have last names, family names, or anything else which is shared by folks recognized as their relatives.
- People have names
- People have, at this point in time, exactly one canonical full name.
- People have, at this point in time, one full name which they go by.
- People whose names break my system are weird outliers. They should have had solid, acceptable names, like 田中太郎.
- People’s first names and last names are, by necessity, different.
- People’s names are all mapped in Unicode code points.
- People’s names are almost globally unique.
- People’s names are assigned at birth ... or at least pretty close to birth.. or within a year or so of birth.
- People’s names are case insensitive.
- People’s names are case sensitive.
- People’s names are globally unique.
- People’s names are not written in ALL CAPS.
- People’s names are not written in all lower case letters.
- People’s names are written in any single character set.
- People’s names are written in ASCII.
- People’s names change, but only at a certain enumerated set of events.
- People’s names do not change.
- People’s names do not contain numbers.
- People’s names fit within a certain defined amount of space.
- People’s names have an order to them.  Picking any ordering scheme will automatically result in consistent ordering among all systems, as long as both use the same ordering scheme for the same name.
- People’s names sometimes have prefixes or suffixes, but you can safely ignore those.
- Two different data entry operators, given a person’s name, will by necessity enter bitwise equivalent strings on any single system, if the system is well-designed.
- Two different systems containing data about the same person will use the same name for that person.

Source: <https://www.kalzumeus.com/2010/06/17/falsehoods-programmers-believe-about-names/>

### Email

Here are some common falsehoods about email:

- A reply to an email sent to address X will come from X (this is the mistake made by things that say “Reply with REMOVE to unsubscribe”)
- All email clients support HTML attachments
- All email clients support HTML message bodies
- All email clients support MIME encoding
- All email comes from a .com, .net, .edu, or .org address
- All email is accessed via webmail
- All email is accessed via webmail or IMAP
- All email is accessed via webmail, IMAP, or POP3
- All email is hosted by a centralized system
- All email is sent via SMTP
- All email is sent via SMTP over IP
- All email is sent via SMTP over TCP/IP
- All email is sent via SMTP over TCP/IP port 25
- All email servers support the various vendor extensions by the current “everyone uses this vendor” vendor (Microsoft, Google, etc.)
- All universities provide an .edu address
- An address which is valid will always be valid, and an address which is invalid will always be invalid
- An email address like ^_^@example.com or +&#@example.com is invalid
- An email address never changes
- An email can only have one From: address
- Any one email address refers to only one single person
- Anyone with a .edu address is a student
- Anyone with a .edu address is a student or faculty
- Domains will be handled uniformly between email and HTTP
- Email addresses are case-sensitive / can be compared by == or strcmp
- Email addresses only contain letters
- Email addresses only contain letters and numbers
- Email addresses only contain letters, numbers, and a handful of common punctuation marks (e.g. ., _, and -)
- Email addresses will have at least one letter in them
- Email attachment size will be accurate to the storage size of the attachment; relatedly, attachment filenames are the correct filenames for those file types, and that it’s safe to extract attachments to those filenames
- Email is a reliable transport
- Email is an instantaneous transport
- Email is secure
- Emails will be received soon after they’re sent
- Emails will be sent within a few days of their scheduling
- Emails will be sent within a few hours of their scheduling
- Emails will be sent within a few minutes of their scheduling
- Encrypted email is secure
- Everyone has an email address
- Everyone has exactly one email address
- Having a particular ccTLD means that you prefer to receive communications in that country’s native language (for example, .fr → French)
- If an email bounces, the address is invalid
- If an email doesn’t bounce, the address is valid
- If you receive email at address X, you are capable of sending email whose From header is X.
- If you send a url in an email, the user will be the first to click it
- It is valid to remove +suffixes from email addresses (e.g. john+doe@example.com → john@example.com)
- Nobody uses email anymore
- Only the owner of an address can send mail from that address
- Students and faculty will use their .edu address to sign up for all of their Internet accounts
- The Date: header on a message is legitimate
- The Received: headers will always be no earlier than the Date: header
- Unique strings of characters all map to different addresses
- Users actually know their own email address
- When an email is sent it immediately goes to its destination server
- When email is sent by a user at a domain, it is sent by a server whose address matches that domain
- When email is sent to a user at a domain, it is delivered to a server whose address matches that domain
- Whenever an address does change, it’s because the user specifically requested it to happen
- Whenever an address does change, it’s under that user’s control
- Whenever an address does change, the old address will continue to work/exist
- You can filter out email based on the TLD or ccTLD from which it originates

Sources:

- <https://beesbuzz.biz/code/439-Falsehoods-programmers-believe-about-email>

### Phone Numbers

[Falsehoods Programmers Believe About Phone Numbers](https://github.com/google/libphonenumber/blob/master/FALSEHOODS.md)

- **An individual has a phone number**. Some people do not own phones, or do not wish to provide you with their telephone number when asked. Do not require a user to provide a phone number unless it is essential, and whenever possible try to provide a fallback to accommodate these users.
- **You can make a call to any phone number**. Some devices such as EFTPOS terminals, fax machines and mobile internet dongles may not support receiving calls. In addition, some people can not use their phones for phone calls. This may be permanent (such as a hearing disability), temporary (temporary hearing loss) or situational (when the user is in a noisy environment).
- **An individual has only one phone number**.
- **A phone number uniquely identifies an individual**. It wasn't even that long ago that mobile phones didn't exist, and it was common for an entire household to share one fixed-line telephone number. In some parts of the world, this is still true, and relatives (or even friends) share a single phone number. Many phone services (especially for businesses) allow multiple inbound calls to or outbound calls from the same phone number.
- **Phone numbers cannot be re-used**. Old phone numbers are recycled and get reassigned to other people.
- **Phone numbers that are valid today will always be valid. Phone numbers of a certain type today (e.g., mobile) will never be reassigned to another type.** A phone number which connects today may be disconnected tomorrow. A number which is free to call today may cost money to call tomorrow. The phone company may decide to expand the range of available phone numbers by inserting a digit into an existing number.
- **Each country calling code corresponds to exactly one country** Example: The USA, Canada, and several Caribbean islands share the country calling code +1. Russia and Kazakhstan share +7.
- **Each country has only one country calling code**. As of this present moment (in Mar. 2016), phones in the disputed territory and partially recognised state of Kosovo may be reached by dialing the country calling code for Serbia (+381), Slovenia (+386), or Monaco (+377), depending on where and when one obtained the number.
- **A phone number is dialable from anywhere** Some numbers can only be dialed within the country. Some can only be dialled from within a subset of countries, such as the +800 [Universal International Freephone Numbers](https://en.wikipedia.org/wiki/Toll-free_telephone_number#Universal_International_Freephone_Service). Some may be dialable only if the caller is a subscriber to a particular telecom company.
- **You can send a text message to any phone number**. A lot of people still only have a fixed-line telephone, which typically cannot send or receive text messages.
- **Only mobile phones can receive text messages**. Some service providers support sending and receiving text messages to fixed-line numbers. There are also online services like Skype that can send and receive text messages.
- **There are only two ways to dial a phone number: domestically and from overseas**. Some numbers may need different prefixes depending on: the carrier you are using; what device you are dialling from/to; whether you are inside or outside a particular geographical region.Examples: In Brazil, to dial numbers internally but across a certain geographical boundary, a carrier code must be explicitly dialed to say which carrier you will use to pay for the call. In Nepal, the leading zero in national format is omitted depending on whether the originating phone is mobile or fixed-line. In New Zealand, you need to dial the area-code (e.g. 03) even if the number is within the same area-code region as you are, unless it is "close" (something approximating city/district boundaries), in which case it shouldn’t be dialled.
- **To make a number dialable, you only need to change the prefix** In Argentina, to dial a mobile number domestically, the digits "15" need to be inserted *after* the area code but *before* the local number, and the "9" after the country code (54) needs to be removed. This transforms +54 9 2982 123456 into 02982 15 123456.
- **No prefix of a valid phone number can be a valid phone number** In some countries, it's possible to connect to a different endpoint by dialing more digits after a number. So "12345678" may not reach the same person as dialing "123456".
- **An invalid number will not reach an endpoint** In some countries, or on some phones, extra digits are thrown away. Hence,    1-800-MICROSOFT is an invalid number - but it still connects to Microsoft, since any later digits are ignored. Numbers such as "911" can be reached by dialling "911 123" in some countries: but not in others. In other countries, invalid numbers may be "fixed" by a carrier, e.g., adding a mobile token if they know it is a mobile number, such that it connects.
- **All valid phone numbers follow the ITU specifications** ITU-T specifies that a phone number cannot be longer than fifteen digits,   with one to three digits reserved for the country calling code, but valid numbers in Germany have been assigned that are longer than this.
- **All valid phone numbers belong to a country** There are many "country calling codes" issued to non-geographical entities, such as satellite services, and the "800" code for [Universal International Freephone Numbers](https://en.wikipedia.org/wiki/Toll-free_telephone_number#Universal_International_Freephone_Service).
- **Phone numbers contain only digits** In Israel, certain advertising numbers start with a `*`. In New Zealand, non-urgent traffic incidents can be reported by calling `*555` from a mobile phone. Alpha characters may also be used in phone numbers, such as in `1-800-Flowers`.
- **Phone numbers are always written in ASCII** In Egypt, it is common for phone numbers to be written in native digits.
- **Phone numbers have only one prefix (area code or national destination code) at a given time** In the mid-90s in Iceland, phone numbers changed from 5 and 6 digits to 7 digits. The old system had regional prefixes, but the new one doesn't. During the transition period, phone numbers could be reached by the old area code or the new 7 digit number (a different prefix). For example, a Reykjavik phone number could be dialed with `nnnnn` and `55nnnnn` inside the region, and `91-nnnnn` and `55nnnnn` from outside.
- **A leading zero in numbers formatted for domestic usage can always be discarded when dialing from abroad** In some countries, people write the national prefix in brackets (typically `(0)`) after the country calling code to indicate that it should be discarded when dialing internationally. In Italy, since 1998, the prefix was "fixed" to the phone numbers, so that `(01) 2345` became `012345` and should be dialed (internationally) as `+39012345` (including the leading zero).
- **The country or area code of a phone number indicates the user's location, place of residence, time-zone, or preferred language** There are many reasons for someone to have a phone number issued in a state or region other than where they reside or hold citizenship. These include, but are not limited to:*Moving within a country*: In countries with phone number portability, you may retain your number when moving, even in some cases if it is a fixed-line number and even if it has an area code (see *[xkcd](https://xkcd.com/1129/)* for a US example.) *Moving to another country*: Some people keep their mobile phones when they move to another country.*Geopolitical turmoil*: Sometimes countries change their borders, cease to exist, or come into existence.*Business, family, and friends*: A business may have many customers in a neighbouring country, or a person may have many family and friends there.*Wanting cheaper rates*: VoIP is often cheaper than regular calls. People traveling around Europe may get a SIM card from one country and have a roaming plan. Note that geographical area codes are assigned in some countries to mobile phones.
- **The plus sign in front of phone numbers in international format is optional, or can always be replaced by `00`** The plus sign is part of the [E.164 format](https://en.wikipedia.org/wiki/E.164) for international telephone numbers. It can be replaced with the [international call prefix](https://en.wikipedia.org/wiki/List_of_international_call_prefixes) when dialing internationally. Note that while `00` is a common international call prefix, this actually varies by country. In North America, which has a country calling code of `+1`, it is a common error to drop the `+` in front of the number and write it like `1-555-123-4567`. This is technically incorrect. To call this number from Japan, where the international call prefix is `010`, one may dial either `+1 555 123 4567` or `010 1 555 123 4567`.
- **Users will only store phone numbers in your product's phone number fields** Some users use their contact lists to store things like birthdays or other information. Unless a piece of user-supplied data has actually been verified to be a phone number, it should be stored as-is as entered by the user.
- **Phone numbers are numbers** Never try to store phone numbers as an int or any other kind of numeric data type. You can't do arithmetic on them, and while 007, 07 and 7 are the same number they are not necessarily the same phone number - in some countries a leading 0 is significant and forms part of the number itself (see *A leading zero in numbers formatted for domestic usage can always be discarded when dialing from abroad*). Moreover, a phone number may contain other diallable characters (see *Phone numbers contain only digits*) or an
    extension portion, dialled after waiting for a tone.
- **Phone numbering plans published by governments or telecoms represent reality** National numbering plans, such as those administered by the [ITU](http://www.itu.int/oth/T0202.aspx?parent=T0202), represent the intentions of the government or telecom. These may be published before, during, or after the actual implementation of numbering plan changes in the real world. The actual date on which a phone number range becomes active may not always adhere to official announcements.
