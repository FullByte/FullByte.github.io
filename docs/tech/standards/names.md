# Names

So, as a public service, I’m going to list assumptions your systems probably make about names.  All of these assumptions are wrong.  Try to make less of them next time you write a system which touches names.

All of these assumptions are wrong:

1. People have exactly one canonical full name.
2. People have exactly one full name which they go by.
3. People have, at this point in time, exactly one canonical full name.
4. People have, at this point in time, one full name which they go by.
5. People have exactly N names, for any value of N.
6. People’s names fit within a certain defined amount of space.
7. People’s names do not change.
8. People’s names change, but only at a certain enumerated set of events.
9. People’s names are written in ASCII.
10. People’s names are written in any single character set.
11. People’s names are all mapped in Unicode code points.
12. People’s names are case sensitive.
13. People’s names are case insensitive.
14. People’s names sometimes have prefixes or suffixes, but you can safely ignore those.
15. People’s names do not contain numbers.
16. People’s names are not written in ALL CAPS.
17. People’s names are not written in all lower case letters.
18. People’s names have an order to them.  Picking any ordering scheme will automatically result in consistent ordering among all systems, as long as both use the same ordering scheme for the same name.
19. People’s first names and last names are, by necessity, different.
20. People have last names, family names, or anything else which is shared by folks recognized as their relatives.
21. People’s names are globally unique.
22. People’s names are almost globally unique.
23. Alright alright but surely people’s names are diverse enough such that no million people share the same name.
24. My system will never have to deal with names from China... Or Japan.. Or Korea.
25. Or Ireland, the United Kingdom, the United States, Spain, Mexico, Brazil, Peru, Russia, Sweden, Botswana, South Africa, Trinidad, Haiti, France, or the Klingon Empire, all of which have “weird” naming schemes in common use.
26. I can safely assume that this dictionary of bad words contains no people’s names in it.
27. People’s names are assigned at birth ... or at least pretty close to birth.. or within a year or so of birth.
28. Two different systems containing data about the same person will use the same name for that person.
29. Two different data entry operators, given a person’s name, will by necessity enter bitwise equivalent strings on any single system, if the system is well-designed.
30. People whose names break my system are weird outliers. They should have had solid, acceptable names, like 田中太郎.
31. People have names
