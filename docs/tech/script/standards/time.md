# Time

![xkcd_iso_8601](https://imgs.xkcd.com/comics/iso_8601.png)

## Facts

- UTC: The time at zero degrees longitude (the Prime Meridian) is called Universal Coordinated Time (UTC).
- GMT: UTC used to be called Greenwich Mean Time (GMT) because the Prime Meridian was (arbitrarily) chosen to pass through the Royal Observatory in Greenwich.
- Other timezones can be written as an offset from UTC. Australian Eastern Standard Time is UTC+1000. e.g. 10:00 UTC is 20:00 EST on the same day.
- Daylight saving does not affect UTC. It's just a polity deciding to change its timezone (offset from UTC). For example, GMT is still used: it's the British national timezone in winter. In summer it becomes BST.
- Leap seconds: By international convention, UTC (which is an arbitrary human invention) is kept within 0.9 seconds of physical reality (UT1, which is a measure of solar time) by introducing a "leap second" in the last minute of the UTC year, or in the last minute of June.
- Leap seconds don't have to be announced much more than six months before they happen. This is a problem if you need second-accurate planning beyond six months.
- Unix time: Measured as the number of seconds since epoch (the beginning of 1970 in UTC). Unix time is not affected by time zones or daylight saving.
- According to POSIX.1, Unix time is supposed to handle a leap second by replaying the previous second. e.g.:
    ```POSIX
    59.00
    59.25
    59.50
    59.75
    59.00 ← replay
    59.25
    59.50
    59.75
    00.00 ← increment
    00.25
    ```

This is a trade-off: you can't represent a leap second, and your time is guaranteed to go backwards. On the other hand, every day is exactly 86,400 seconds long, and you don't need a table of all previous and future leap seconds in order to format Unix time as human-preferred hours-minutes-seconds.
ntpd is supposed to make the replay happen after it sees the "leap bits" from upstream timeservers, but I've also seen it do nothing: the system goes one second into the future, then slowly slews back to the correct time.

- Timezones are a presentation-layer problem!
- Most of your code shouldn't be dealing with timezones or local time, it should be passing Unix time around.
- When measuring time, measure Unix time. It's UTC. It's easy to obtain. It doesn't have timezone offsets or daylight saving (or leap seconds).
- When storing time, store Unix time. It's a single number.
- If you want to store a humanly-readable time (e.g. logs), consider storing it along with Unix time, not instead of Unix time.
- When displaying time, always include the timezone offset. A time format without an offset is useless.
- The system clock is inaccurate.
- You're on a network? Every other system's clock is differently inaccurate.
- The system clock can, and will, jump backwards and forwards in time due to things outside of your control. Your program should be designed to survive this.
- The number of "clock" seconds per "real" second is both inaccurate and variable. It mostly varies with temperature.
- Don't blindly use gettimeofday(). If you need a monotonic (always increasing) clock, have a look at clock_gettime().
ntpd can change the system time in two ways: 1) Step: making the clock jump backwards or forwards to the correct time instantaneously. 2) Slew: changing the frequency of the clock so that it slowly drifts toward the correct time. --> Slew is preferred because it's less disruptive, but it's only useful for correcting small offsets.
- Time passes at a rate of one second per second for every observer. The frequency of a remote clock relative to an observer is affected by velocity and gravity. The clocks inside GPS satellites are adjusted for relativistic effects.
- MySQL (at least 4.x and 5.x) stores DATETIME columns as a "YYYY-MM-DD HH:MM:SS" string. I'm not even kidding. If you care at all about storing timestamps, store them as integers and use the UNIX_TIMESTAMP() and FROM_UNIXTIME() functions.

## Dates

In search of the perfect date...

![perfect-date](_perfect-date.jpg)

All of these assumptions are wrong:

- There are always 24 hours in a day.
- Months have either 30 or 31 days.
- Years have 365 days.
- February is always 28 days long.
- Any 24-hour period will always begin and end in the same day (or week, or month).
- A week always begins and ends in the same month.
- A week (or a month) always begins and ends in the same year.
- The machine that a program runs on will always be in the GMT time zone.
- The Time zone in which a program has to run will never change.
- There will never be a change to the time zone in which a program hast to run in production.
- The system clock will always be set to the correct local time.
- The system clock will always be set to a time that is not wildly different from the correct local time.
- If the system clock is incorrect, it will at least always be off by a consistent number of seconds.
- The server clock and the client clock will always be set to the same time.
- The server clock and the client clock will always be set to around the same time.
- The time on the server clock and time on the client clock would never be different by a matter of decades.
- If the server clock and the client clock are not in synch, they will at least always be out of synch by a consistent number of seconds.
- The server clock and the client clock will use the same time zone.
- The system clock will never be set to a time that is in the distant past or the far future.
- Time has no beginning and no end.
- One minute on the system clock has exactly the same duration as one minute on any other clock
- The duration of one minute on the system clock will be pretty close to the duration of one minute on most other clocks.
- The duration of one minute on the system clock would never be more than an hour.
- The smallest unit of time is one second.
- It will never be necessary to set the system time to any value other than the correct local time.
- Testing might require setting the system time to a value other than the correct local time but it will never be necessary to do so in production.
- Time stamps will always be specified in a commonly-understood format like 1339972628 or 133997262837.
- Time stamps will always be specified in the same format.
- Time stamps will always have the same level of precision.
- A time stamp of sufficient precision can safely be considered unique.
- A timestamp represents the time that an event actually occurred.
- Human-readable dates can be specified in universally understood formats such as 05/07/11.
- The offsets between two time zones will remain constant.
- OK, historical oddities aside, the offsets between two time zones won’t change in the future.
- Changes in the offsets between time zones will occur with plenty of advance notice.
- Daylight saving time happens at the same time every year.
- Daylight saving time happens at the same time in every time zone.
- Daylight saving time always adjusts by an hour.
- Months have either 28, 29, 30, or 31 days.
- The day of the month always advances contiguously from N to either N+1 or 1, with no discontinuities.
- There is only one calendar system in use at one time.
- There is a leap year every year divisible by 4.
- Non leap years will never contain a leap day.
- It will be easy to calculate the duration of x number of hours and minutes from a particular point in time.
- The same month has the same number of days in it everywhere!
- Unix time is completely ignorant about anything except seconds.
- Unix time is the number of seconds since Jan 1st 1970.
- The day before Saturday is always Friday.
- Contiguous timezones are no more than an hour apart. (aka we don’t need to test what happens to the avionics when you fly over the International Date Line)
- Two timezones that differ will differ by an integer number of half hours.
- Okay, quarter hours.
- Okay, seconds, but it will be a consistent difference if we ignore DST.
- If you create two date objects right beside each other, they’ll represent the same time. (a fantastic Heisenbug generator)
- You can wait for the clock to reach exactly HH:MM:SS by sampling once a second.
- If a process runs for n seconds and then terminates, approximately n seconds will have elapsed on the system clock at the time of termination.
- Weeks start on Monday.
- Days begin in the morning.
- Holidays span an integer number of whole days.
- The weekend consists of Saturday and Sunday.
- It’s possible to establish a total ordering on timestamps that is useful outside your system.
- The local time offset (from UTC) will not change during office hours.
- Thread.sleep(1000) sleeps for 1000 milliseconds.
- Thread.sleep(1000) sleeps for >= 1000 milliseconds.
- There are 60 seconds in every minute.
- Timestamps always advance monotonically.
- GMT and UTC are the same timezone.
- Britain uses GMT.
- Time always goes forwards.
- The difference between the current time and one week from the current time is always 7 \* 86400 seconds.
- The difference between two timestamps is an accurate measure of the time that elapsed between them.
- 24:12:34 is an invalid time
- Every integer is a theoretical possible year
- If you display a datetime, the displayed time has the same second part as the stored time
- Or the same year
- But at least the numerical difference between the displayed and stored year will be less than 2
- If you have a date in a correct YYYY-MM-DD format, the year consists of four characters
- If you merge two dates, by taking the month from the first and the day/year from the second, you get a valid date
- But it will work, if both years are leap years
- If you take a w3c published algorithm for adding durations to dates, it will work in all cases.
- The standard library supports negative years and years above 10000.
- Time zones always differ by a whole hour
- If you convert a timestamp with millisecond precision to a date time with second precision, you can safely ignore the millisecond fractions
- But you can ignore the millisecond fraction, if it is less than 0.5
- Two-digit years should be somewhere in the range 1900-2099
- If you parse a date time, you can read the numbers character for character, without needing to backtrack
- But if you print a date time, you can write the numbers character for character, without needing to backtrack
- You will never have to parse a format like ---12Z or P12Y34M56DT78H90M12.345S
- There are only 24 time zones
- Time zones are always whole hours away from UTC
- Daylight Saving Time (DST) starts/ends on the same date everywhere
- DST is always an advancement by 1 hour
- Reading the client’s clock and comparing to UTC is a good way to determine their timezone
- The software stack will/won’t try to automatically adjust for timezone/DST
- My software is only used internally/locally, so I don’t have to worry about timezones
- My software stack will handle it without me needing to do anything special
- I can easily maintain a timezone list myself
- All measurements of time on a given clock will occur within the same frame of reference.
- The fact that a date-based function works now means it will work on any date.
- Years have 365 or 366 days.
- Each calendar date is followed by the next in sequence, without skipping.
- A given date and/or time unambiguously identifies a unique moment.
- Leap years occur every 4 years.
- You can determine the time zone from the state/province.
- You can determine the time zone from the city/town.
- Time passes at the same speed on top of a mountain and at the bottom of a valley.
- One hour is as long as the next in all time systems.
- You can calculate when leap seconds will be added.
- The precision of the data type returned by a getCurrentTime() function is the same as the precision of that function.
- Two subsequent calls to a getCurrentTime() function will return distinct results.
- The second of two subsequent calls to a getCurrentTime() function will return a larger result.
- The software will never run on a space ship that is orbiting a black hole.

Some source credited to <http://infiniteundo.com/post/25326999628/falsehoods-programmers-believe-about-time>

## Time zone

Some links to time zone standards:

- ISO 8601 Wikipedia <https://en.wikipedia.org/wiki/ISO_8601>
- ISO 8601 <https://www.iso.org/obp/ui/#iso:std:iso:8601:-1:ed-1:v1:en>
- ISO Weekdate Wikipedia <https://en.wikipedia.org/wiki/ISO_week_date>
- RFC 3339 <https://tools.ietf.org/html/rfc3339>
- Extended Date/Time Format (EDTF): <https://www.loc.gov/standards/datetime/>

A list of time zones:

| INDEX | NAME OF Time                    | ZONE Time   | IANA                                                    | Time ZONE                      |
|-------|---------------------------------|-------------|---------------------------------------------------------|--------------------------------|
| 10    | Azores Standard Time            | (GMT-01:00) | Azores                                                  | Atlantic/Azores                |
| 12    | Cape Verde Standard Time        | (GMT-01:00) | Cape Verde Islands                                      | Atlantic/Cape_Verde            |
| 43    | Mid-Atlantic Standard Time      | (GMT-02:00) | Mid-Atlantic                                            | Atlantic/South_Georgia         |
| 27    | E. South America Standard Time  | (GMT-03:00) | Brasilia                                                | America/Sao_Paulo              |
| 58    | SA Eastern Standard Time        | (GMT-03:00) | Buenos Aires, Georgetown                                | America/Argentina/Buenos_Aires |
| 35    | Greenland Standard Time         | (GMT-03:00) | Greenland                                               | America/Godthab                |
| 51    | Newfoundland Standard Time      | (GMT-03:30) | Newfoundland and Labrador                               | America/St_Johns               |
| 06    | Atlantic Standard Time          | (GMT-04:00) | Atlantic Time (Canada)                                  | America/Halifax                |
| 60    | SA Western Standard Time        | (GMT-04:00) | Caracas, La Paz                                         | America/La_Paz                 |
| 17    | Central Brazilian Standard Time | (GMT-04:00) | Manaus                                                  | America/Cuiaba                 |
| 54    | Pacific SA Standard Time        | (GMT-04:00) | Santiago                                                | America/Santiago               |
| 59    | SA Pacific Standard Time        | (GMT-05:00) | Bogota, Lima, Quito                                     | America/Bogota                 |
| 28    | Eastern Standard Time           | (GMT-05:00) | Eastern Time (US and Canada)                            | America/New_York               |
| 70    | US Eastern Standard Time        | (GMT-05:00) | Indiana (East)                                          | America/Indiana/Indianapolis   |
| 15    | Central America Standard Time   | (GMT-06:00) | Central America                                         | America/Costa_Rica             |
| 21    | Central Standard Time           | (GMT-06:00) | Central Time (US and Canada)                            | America/Chicago                |
| 22    | Central Standard Time (Mexico)  | (GMT-06:00) | Guadalajara, Mexico City, Monterrey                     | America/Monterrey              |
| 11    | Canada Central Standard Time    | (GMT-06:00) | Saskatchewan                                            | America/Edmonton               |
| 71    | US Mountain Standard Time       | (GMT-07:00) | Arizona                                                 | America/Phoenix                |
| 45    | Mountain Standard Time (Mexico) | (GMT-07:00) | Chihuahua, La Paz, Mazatlan                             | America/Chihuahua              |
| 44    | Mountain Standard Time          | (GMT-07:00) | Mountain Time (US and Canada)                           | America/Denver                 |
| 55    | Pacific Standard Time           | (GMT-08:00) | Pacific Time (US and Canada), Tijuana                   | America/Tijuana                |
| 02    | Alaskan Standard Time           | (GMT-09:00) | Alaska                                                  | America/Anchorage              |
| 38    | Hawaiian Standard Time          | (GMT-10:00) | Hawaii                                                  | Pacific/Honolulu               |
| 61    | Samoa Standard Time             | (GMT-11:00) | Midway Island, Samoa                                    | Pacific/Apia                   |
| 36    | Greenwich Standard Time         | (GMT)       | Casablanca, Monrovia                                    | Africa/Monrovia                |
| 34    | GMT Standard Time               | (GMT)       | Greenwich Mean Time : Dublin, Edinburgh, Lisbon, London | Europe/London                  |
| 75    | W. Europe Standard Time         | (GMT+01:00) | Amsterdam, Berlin, Bern, Rome, Stockholm, Vienna        | Europe/Berlin                  |
| 18    | Central Europe Standard Time    | (GMT+01:00) | Belgrade, Bratislava, Budapest, Ljubljana, Prague       | Europe/Belgrade                |
| 56    | Romance Standard Time           | (GMT+01:00) | Brussels, Copenhagen, Madrid, Paris                     | Europe/Paris                   |
| 19    | Central European Standard Time  | (GMT+01:00) | Sarajevo, Skopje, Warsaw, Zagreb                        | Europe/Belgrade                |
| 74    | W. Central Africa Standard Time | (GMT+01:00) | West Central Africa                                     | Africa/Lagos                   |
| 37    | GTB Standard Time               | (GMT+02:00) | Athens, Bucharest, Istanbul                             | Europe/Istanbul                |
| 29    | Egypt Standard Time             | (GMT+02:00) | Cairo                                                   | Africa/Cairo                   |
| 64    | South Africa Standard Time      | (GMT+02:00) | Harare, Pretoria                                        | Africa/Harare                  |
| 32    | FLE Standard Time               | (GMT+02:00) | Helsinki, Kiev, Riga, Sofia, Tallinn, Vilnius           | Europe/Riga                    |
| 41    | Israel Standard Time            | (GMT+02:00) | Jerusalem                                               | Asia/Jerusalem                 |
| 26    | E. Europe Standard Time         | (GMT+02:00) | Minsk                                                   | Europe/Minsk                   |
| 48    | Namibia Standard Time           | (GMT+02:00) | Windhoek                                                | Africa/Windhoek                |
| 05    | Arabic Standard Time            | (GMT+03:00) | Baghdad                                                 | Asia/Baghdad                   |
| 03    | Arab Standard Time              | (GMT+03:00) | Kuwait, Riyadh                                          | Asia/Kuwait                    |
| 57    | Russian Standard Time           | (GMT+03:00) | Moscow, St. Petersburg, Volgograd                       | Europe/Moscow                  |
| 24    | E. Africa Standard Time         | (GMT+03:00) | Nairobi                                                 | Africa/Nairobi                 |
| 40    | Iran Standard Time              | (GMT+03:30) | Tehran                                                  | Asia/Tehran                    |
| 04    | Arabian Standard Time           | (GMT+04:00) | Abu Dhabi, Muscat                                       | Asia/Muscat                    |
| 09    | Azerbaijan Standard Time        | (GMT+04:00) | Baku                                                    | Asia/Baku                      |
| 33    | Georgian Standard Time          | (GMT+04:00) | Tblisi                                                  | Asia/Tbilisi                   |
| 13    | Caucasus Standard Time          | (GMT+04:00) | Yerevan                                                 | Asia/Yerevan                   |
| 01    | Afghanistan Standard Time       | (GMT+04:30) | Kabul                                                   | Asia/Kabul                     |
| 30    | Ekaterinburg Standard Time      | (GMT+05:00) | Ekaterinburg                                            | Asia/Yekaterinburg             |
| 76    | West Asia Standard Time         | (GMT+05:00) | Islamabad, Karachi, Tashkent                            | Asia/Tashkent                  |
| 39    | India Standard Time             | (GMT+05:30) | Chennai, Kolkata, Mumbai, New Delhi                     | Asia/Calcutta                  |
| 49    | Nepal Standard Time             | (GMT+05:45) | Kathmandu                                               | Asia/Kathmandu                 |
| 47    | N. Central Asia Standard Time   | (GMT+06:00) | Almaty, Novosibirsk                                     | Asia/Novosibirsk               |
| 16    | Central Asia Standard Time      | (GMT+06:00) | Astana, Dhaka                                           | Asia/Almaty                    |
| 65    | Sri Lanka Standard Time         | (GMT+06:00) | Sri Jayawardenepura                                     | Asia/Colombo                   |
| 46    | Myanmar Standard Time           | (GMT+06:30) | Yangon (Rangoon)                                        | Asia/Rangoon                   |
| 62    | SE Asia Standard Time           | (GMT+07:00) | Bangkok, Hanoi, Jakarta                                 | Asia/Bangkok                   |
| 53    | North Asia Standard Time        | (GMT+07:00) | Krasnoyarsk                                             | Asia/Krasnoyarsk               |
| 23    | China Standard Time             | (GMT+08:00) | Beijing, Chongqing, Hong Kong SAR, Urumqi               | Asia/Shanghai                  |
| 52    | North Asia East Standard Time   | (GMT+08:00) | Irkutsk, Ulaanbaatar                                    | Asia/Irkutsk                   |
| 63    | Singapore Standard Time         | (GMT+08:00) | Kuala Lumpur, Singapore                                 | Asia/Singapore                 |
| 73    | W. Australia Standard Time      | (GMT+08:00) | Perth                                                   | Australia/Perth                |
| 66    | Taipei Standard Time            | (GMT+08:00) | Taipei                                                  | Asia/Taipei                    |
| 68    | Tokyo Standard Time             | (GMT+09:00) | Osaka, Sapporo, Tokyo                                   | Asia/Tokyo                     |
| 42    | Korea Standard Time             | (GMT+09:00) | Seoul                                                   | Asia/Seoul                     |
| 78    | Yakutsk Standard Time           | (GMT+09:00) | Yakutsk                                                 | Asia/Yakutsk                   |
| 14    | Cen. Australia Standard Time    | (GMT+09:30) | Adelaide                                                | Australia/Adelaide             |
| 07    | AUS Central Standard Time       | (GMT+09:30) | Darwin                                                  | Australia/Darwin               |
| 25    | E. Australia Standard Time      | (GMT+10:00) | Brisbane                                                | Australia/Brisbane             |
| 08    | AUS Eastern Standard Time       | (GMT+10:00) | Canberra, Melbourne, Sydney                             | Australia/Sydney               |
| 77    | West Pacific Standard Time      | (GMT+10:00) | Guam, Port Moresby                                      | Pacific/Guam                   |
| 67    | Tasmania Standard Time          | (GMT+10:00) | Hobart                                                  | Australia/Hobart               |
| 72    | Vladivostok Standard Time       | (GMT+10:00) | Vladivostok                                             | Asia/Vladivostok               |
| 20    | Central Pacific Standard Time   | (GMT+11:00) | Magadan, Solomon Islands, New Caledonia                 | Pacific/Guadalcanal            |
| 50    | New Zealand Standard Time       | (GMT+12:00) | Auckland, Wellington                                    | Pacific/Auckland               |
| 31    | Fiji Standard Time              | (GMT+12:00) | Fiji Islands, Kamchatka, Marshall Islands               | Pacific/Fiji                   |
| 69    | Tonga Standard Time             | (GMT+13:00) | Nuku'alofa                                              | Pacific/Tongatapu              |

## Lunar Standard Time (LST)

The Lunar year consists of twelve days, named after the first men who walked on the Moon. Each day is divided into 30 cycles of time, with each cycle being divided into 24 moon-hours. Each moon-hour then has 60 moon-minutes, which in turn of course are made up of 60 moon-seconds each. The inverted triangle ∇ is the LST symbol, and if used it suffixes date and prefixes time. The standard notation is: Year-Day-Cycle ∇ Hour:Minute:Second example: 55-11-14 ∇ 14:36:49

| Measure | Terrestrial Time       | Lunar Time       |
|---------|------------------------|------------------|
| seconds | 1                      | 0.9843529666671  |
| minute  | 60 terrestrial seconds | 60 lunar seconds |
| hour    | 60 terrestrial minutes | 60 lunar minutes |
| day     | 24 terrestrial hours   | 30 lunar cycles* |
| year    | 365 days               | 12 lunar days    |

*Each is day named after one of the twelve men that walked on the Moon during the Apollo projects:

| Day    | Name      | Days |
|--------|-----------|------|
| Day 1  | Armstrong | 1-30 |
| Day 2  | Aldrin    | 1-30 |
| Day 3  | Conrad    | 1-30 |
| Day 4  | Bean      | 1-30 |
| Day 5  | Shepard   | 1-30 |
| Day 6  | Mitchell  | 1-30 |
| Day 7  | Scott     | 1-30 |
| Day 8  | Irwin     | 1-30 |
| Day 9  | Young     | 1-30 |
| Day 10 | Duke      | 1-30 |
| Day 11 | Cernan    | 1-30 |
| Day 12 | Schmitt   | 1-30 |

On the moon you have about 15 days of continuous daylight and then 15 days of total darkness. So, a "day" on the Moon, would correspond to about a month or 29.5 Earth-days. Once, about every 29 days, you have a full moon, which is "noon" on the center of the disk. This is also called the synodic month. So a day on the moon, counting from noon to noon, lasts about 29.27 to 29.83 Earth days. Neil Armstrong set foot on the Moon surface on July 21th 1969 at 02:56:15 UT, and this is the obvious choice for a point in time for the calendar to start. So, this is Year 1, day 1 cycle 1, 00:00:00.

You can use this tool to convert a time to lunar time: <http://lunarclock.org/convert-to-lunar-standard-time.php>

Sources:

- <http://lunarclock.org/>

## Metric Time

| Measure | Time as we Know it                          | Metric Time Usage                            |
|---------|---------------------------------------------|----------------------------------------------|
| day     | 24 hours or 1,440 minutes or 86,400 seconds | 10 hours or 1,000 minutes or 100,000 seconds |
| hour    | 60 minutes or 3,600 seconds                 | 100 minutes or 10,000 seconds                |
| minute  | 60 seconds                                  | 100 seconds                                  |

Sources:

- <https://en.wikipedia.org/wiki/Metric_time>
- <https://timeity.com/metric-time/>

## Calendar

List of calendars: <https://en.wikipedia.org/wiki/List_of_calendars>

Representation in various calendars of the year 2021

| Calendar                     | Year 2021                                                                                         |
|------------------------------|---------------------------------------------------------------------------------------------------|
| Gregorian calendar           | 2021 MMXXI                                                                                        |
| Ab urbe condita              | 2774                                                                                              |
| Armenian calendar            | 1470 ԹՎ ՌՆՀ                                                                                       |
| Assyrian calendar            | 6771                                                                                              |
| Bahá'í calendar              | 177–178                                                                                           |
| Balinese saka calendar       | 1942–1943                                                                                         |
| Bengali calendar             | 1428                                                                                              |
| Berber calendar              | 2971                                                                                              |
| British Regnal year          | 69 Eliz. 2 – 70 Eliz. 2                                                                           |
| Buddhist calendar            | 2565                                                                                              |
| Burmese calendar             | 1383                                                                                              |
| Byzantine calendar           | 7529–7530                                                                                         |
| Chinese calendar             | 庚子年 (Metal Rat) 4717 or 4657 — to — 辛丑年 (Metal Ox) 4718 or 4658                             |
| Coptic calendar              | 1737–1738                                                                                         |
| Discordian calendar          | 3187                                                                                              |
| Ethiopian calendar           | 2013–2014                                                                                         |
| Hebrew calendar              | 5781–5782                                                                                         |
| Hindu calendar Vikram Samvat | 2077–2078                                                                                         |
| Hindu calendar Shaka Samvat  | 1942–1943                                                                                         |
| Hindu calendar Kali Yuga     | 5121–5122                                                                                         |
| Holocene calendar            | 12021                                                                                             |
| Igbo calendar                | 1021–1022                                                                                         |
| Iranian calendar             | 1399–1400                                                                                         |
| Islamic calendar             | 1442–1443                                                                                         |
| Japanese calendar            | Reiwa 3 (令和３年)                                                                                 |
| Javanese calendar            | 1954–1955                                                                                         |
| Juche calendar               | 110                                                                                               |
| Julian calendar              | Gregorian minus 13 days                                                                           |
| Korean calendar              | 4354                                                                                              |
| Minguo calendar              | ROC 110 民國110年                                                                                 |
| Nanakshahi calendar          | 553                                                                                               |
| Thai solar calendar          | 2564                                                                                              |
| Tibetan calendar             | 阳金鼠年 (male Iron-Rat) 2147 or 1766 or 994 — to — 阴金牛年 (female Iron-Ox) 2148 or 1767 or 995 |
| Unix time                    | 1609459200 – 1640995199                                                                           |

## Non 7-day weeks

| Tradition                  | week length |
|----------------------------|-------------|
| Bali                       | various     |
| Korea                      | 5 days      |
| Java                       | 5 days      |
| Discordian                 | 5 days      |
| Akan                       | 6 days      |
| Ancient Rome               | 8 days      |
| Burmese                    | 8 days      |
| Celtic                     | 8 days      |
| Baltic                     | 9 days      |
| Chinese                    | 10 days     |
| Egyptian Calendar          | 10 days     |
| French Republican Calendar | 10 days     |
| Aztecs                     | 13 days     |

## Fun facts

A **moment** was a medieval unit of time. The movement of a shadow on a sundial covered 40 moments in a solar hour. An hour in this case meant one twelfth of the period between sunrise and sunset. The length of a solar hour depended on the length of the day, which in turn varied with the season, so the length of a moment in modern seconds was not fixed, but on average, a moment corresponded to 90 seconds.

Fictional calendars

- [Discworld](https://en.wikipedia.org/wiki/Discworld_(world)#Calendar)
- [Middle-earth](https://en.wikipedia.org/wiki/History_of_Arda)
- [Star Trek (Stardates)](https://en.wikipedia.org/wiki/Stardate)

## Links

- 120 years of timezones: <https://blog.scottlogic.com/2021/09/14/120-years-timezone.html>
- <https://en.wikipedia.org/wiki/ISO_3166-1>
- <https://www.timeanddate.com/time/zones/>
- <https://www.iana.org/time-zones>
- <https://www.ibm.com/docs/en/workload-scheduler/8.6.0?topic=zones-complete-table-time-variable-length-notation>

Wikipedia on time, calendars and dates

- <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>
- <https://en.wikipedia.org/wiki/List_of_dates_predicted_for_apocalyptic_events>
- <https://en.wikipedia.org/wiki/List_of_unusual_units_of_measurement#Time>
- <https://en.wikipedia.org/wiki/Soviet_calendar>
- <https://en.wikipedia.org/wiki/Hanke%E2%80%93Henry_Permanent_Calendar>
