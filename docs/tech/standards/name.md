# Names

## Wrong assumptions about names

So, as a public service, I’m going to list assumptions your systems probably make about names.  All of these assumptions are wrong.  Try to make less of them next time you write a system which touches names.

All of these assumptions are wrong:

- People have exactly one canonical full name.
- People have exactly one full name which they go by.
- People have, at this point in time, exactly one canonical full name.
- People have, at this point in time, one full name which they go by.
- People have exactly N names, for any value of N.
- People’s names fit within a certain defined amount of space.
- People’s names do not change.
- People’s names change, but only at a certain enumerated set of events.
- People’s names are written in ASCII.
- People’s names are written in any single character set.
- People’s names are all mapped in Unicode code points.
- People’s names are case sensitive.
- People’s names are case insensitive.
- People’s names sometimes have prefixes or suffixes, but you can safely ignore those.
- People’s names do not contain numbers.
- People’s names are not written in ALL CAPS.
- People’s names are not written in all lower case letters.
- People’s names have an order to them.  Picking any ordering scheme will automatically result in consistent ordering among all systems, as long as both use the same ordering scheme for the same name.
- People’s first names and last names are, by necessity, different.
- People have last names, family names, or anything else which is shared by folks recognized as their relatives.
- People’s names are globally unique.
- People’s names are almost globally unique.
- Alright alright but surely people’s names are diverse enough such that no million people share the same name.
- My system will never have to deal with names from China... Or Japan.. Or Korea.
- Or Ireland, the United Kingdom, the United States, Spain, Mexico, Brazil, Peru, Russia, Sweden, Botswana, South Africa, Trinidad, Haiti, France, or the Klingon Empire, all of which have “weird” naming schemes in common use.
- I can safely assume that this dictionary of bad words contains no people’s names in it.
- People’s names are assigned at birth ... or at least pretty close to birth.. or within a year or so of birth.
- Two different systems containing data about the same person will use the same name for that person.
- Two different data entry operators, given a person’s name, will by necessity enter bitwise equivalent strings on any single system, if the system is well-designed.
- People whose names break my system are weird outliers. They should have had solid, acceptable names, like 田中太郎.
- People have names
