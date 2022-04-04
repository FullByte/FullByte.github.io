# Statistics

## Roll outcome

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

With 3x D6 we get a total of 216 (6x6x6 or 6^3) possible outcomes.

Let us now look at unique rolls. To get all possible combinations we can use this formula for combination with repetition:

\begin{align}
    \frac{(n+k-1)!}{k!*(n-1)!}
\end{align}

To learn more read about [Binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient) and [combinatorics](https://en.wikipedia.org/wiki/Combinatorics).

With 3x D6 we get n = 6, k = 3 resulting in 56 combinations.

\begin{align}
    \frac{(6+3-1)!}{3!*(6-1)!} = 56
\end{align}

You can copy```(6+3-1)!/(3!*(6-1)!)``` to WolframAlpha to calculate it or use [this link](https://www.wolframalpha.com/input/?i=%286%2B3-1%29%21%2F%283%21*%286-1%29%21%29).

These 56 combinations distribute as follows:

| Result                |                                                                                                                                                                     | Amount | Percent |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------|
| ⚰️ Das Unvermeidliche | ⚀⚁⚃, ⚀⚁⚄, ⚀⚁⚅, ⚁⚂⚀ </br> ⚁⚂⚄, ⚁⚂⚅, ⚂⚃⚀, ⚂⚃⚁</br>⚂⚃⚅, ⚃⚄⚀, ⚃⚄⚁, ⚃⚄⚂, </br> ⚄⚅⚀, ⚄⚅⚁, ⚄⚅⚂, ⚄⚅⚃                                                                        | 16     | 29 %    |
| 🎁 Wunsch             | ⚀⚀⚁, ⚀⚀⚂, ⚀⚀⚃, ⚀⚀⚄, ⚀⚀⚅</br>⚁⚁⚀, ⚁⚁⚂, ⚁⚁⚃, ⚁⚁⚄, ⚁⚁⚅</br>⚂⚂⚀, ⚂⚂⚁, ⚂⚂⚃, ⚂⚂⚄, ⚂⚂⚅</br>⚃⚃⚀, ⚃⚃⚁, ⚃⚃⚂, ⚃⚃⚄, ⚃⚃⚅</br>⚄⚄⚀, ⚄⚄⚁, ⚄⚄⚂, ⚄⚄⚃, ⚄⚄⚅</br>⚅⚅⚀, ⚅⚅⚁, ⚅⚅⚂, ⚅⚅⚃, ⚅⚅⚄ | 30     | 54 %    |
| 🦄 Einhorn            | ⚀⚂⚄, ⚀⚂⚅, ⚀⚃⚅, ⚁⚃⚅                                                                                                                                                  | 4      | 7 %     |
| ☢️ Dreifaltigkeit     | ⚀⚀⚀, ⚁⚁⚁, ⚂⚂⚂</br>⚃⚃⚃, ⚄⚄⚄, ⚅⚅⚅                                                                                                                                     | 6      | 11 %    |

However, this is not the probability of each combination since the distinct combinations are not evenly distributed over the 216 possible outcomes.

I do not know how to calculate this, so I created a python script and analyzed of all possible outcomes. To view the full list, expand "Full list of possible dice combinations". The outcome is as follows:

| Result                | total      | distinct |
|-----------------------|------------|----------|
| ⚰️ Das Unvermeidliche | 96 (44,4%) | 16 (29%) |
| 🎁 Wunsch             | 90 (41,7%) | 30 (54%) |
| 🦄 Einhorn            | 24 (11,1%) | 4 (7%)   |
| ☢️ Dreifaltigkeit     | 6 (2,8%)   | 6 (11%)  |

The result shows that Das Unvermeidliche has less distinct variations than Wunsch but more possible combinations.

## All possible roll attempts

This python script calculates all possible dice results of the game Einhorn, counts the combinations and prints the probability of each of the four roll outcomes.

``` py
from itertools import product # pip install itertools
from collections import OrderedDict
import math

# Dice settings
diceFaces = 6
diceSmallestNumber = 1
diceHighestNumber = 6
diceAmount = 3

# Counter
Dreifaltigkeit = 0
Wunsch = 0
Unvermeidlich = 0
Einhorn = 0

# Create a list of all possible roll attempts
rolls = list(product(range(diceSmallestNumber,diceHighestNumber+1), repeat=diceAmount))

# Iterate roll attempts and check result
for roll in rolls:
    # Prepare list
    removedDoubleRoll = tuple(OrderedDict.fromkeys(roll).keys())
    sortedRoll = list(removedDoubleRoll)
    sortedRoll.sort() 

    # Count and print result
    if (len(sortedRoll)==2):
        print(roll, " Wunsch")
        Wunsch += 1
    elif (len(sortedRoll)==1):
        print(roll, " Dreifaltigkeit")
        Dreifaltigkeit += 1
    else:
        if ((sortedRoll[1]-sortedRoll[0]==1) or (sortedRoll[2]-sortedRoll[1]==1)):
            print(sortedRoll, " Das Unvermeidliche")
            Unvermeidlich += 1
        else:
            print(sortedRoll, " Einhorn")
            Einhorn += 1

# Print stats
print("\nTotal amount of possible rolls: ", len(rolls))
print("Total amount of distint rolls: ", int((math.factorial(diceFaces+diceAmount-1))/(math.factorial(diceAmount)*(math.factorial(diceFaces-1)))))
print("\nDreifaltigkeit: ", Dreifaltigkeit, "({:.1f}".format(Dreifaltigkeit / len(rolls) * 100), "%)")
print("Wunsch: ", Wunsch, "({:.1f}".format(Wunsch / len(rolls) * 100), "%)")
print("Das Unvermeidliche: ", Unvermeidlich, "({:.1f}".format(Unvermeidlich / len(rolls) * 100), "%)")
print("Einhorn: ", Einhorn, "({:.1f}".format(Einhorn / len(rolls) * 100), "%)")
```

## Full list of possible dice combinations

This is a full list of all possible roll combinations in this game and the result based on the described rules above.

| D1 | D2 | D3 | Result             |
|----|----|----|--------------------|
| 1  | 1  | 1  | Dreifaltigkeit     |
| 1  | 1  | 2  | Wunsch             |
| 1  | 1  | 3  | Wunsch             |
| 1  | 1  | 4  | Wunsch             |
| 1  | 1  | 5  | Wunsch             |
| 1  | 1  | 6  | Wunsch             |
| 1  | 2  | 1  | Wunsch             |
| 1  | 2  | 2  | Wunsch             |
| 1  | 2  | 3  | Das Unvermeidliche |
| 1  | 2  | 4  | Das Unvermeidliche |
| 1  | 2  | 5  | Das Unvermeidliche |
| 1  | 2  | 6  | Das Unvermeidliche |
| 1  | 3  | 1  | Wunsch             |
| 1  | 2  | 3  | Das Unvermeidliche |
| 1  | 3  | 3  | Wunsch             |
| 1  | 3  | 4  | Das Unvermeidliche |
| 1  | 3  | 5  | Einhorn            |
| 1  | 3  | 6  | Einhorn            |
| 1  | 4  | 1  | Wunsch             |
| 1  | 2  | 4  | Das Unvermeidliche |
| 1  | 3  | 4  | Das Unvermeidliche |
| 1  | 4  | 4  | Wunsch             |
| 1  | 4  | 5  | Das Unvermeidliche |
| 1  | 4  | 6  | Einhorn            |
| 1  | 5  | 1  | Wunsch             |
| 1  | 2  | 5  | Das Unvermeidliche |
| 1  | 3  | 5  | Einhorn            |
| 1  | 4  | 5  | Das Unvermeidliche |
| 1  | 5  | 5  | Wunsch             |
| 1  | 5  | 6  | Das Unvermeidliche |
| 1  | 6  | 1  | Wunsch             |
| 1  | 2  | 6  | Das Unvermeidliche |
| 1  | 3  | 6  | Einhorn            |
| 1  | 4  | 6  | Einhorn            |
| 1  | 5  | 6  | Das Unvermeidliche |
| 1  | 6  | 6  | Wunsch             |
| 2  | 1  | 1  | Wunsch             |
| 2  | 1  | 2  | Wunsch             |
| 1  | 2  | 3  | Das Unvermeidliche |
| 1  | 2  | 4  | Das Unvermeidliche |
| 1  | 2  | 5  | Das Unvermeidliche |
| 1  | 2  | 6  | Das Unvermeidliche |
| 2  | 2  | 1  | Wunsch             |
| 2  | 2  | 2  | Dreifaltigkeit     |
| 2  | 2  | 3  | Wunsch             |
| 2  | 2  | 4  | Wunsch             |
| 2  | 2  | 5  | Wunsch             |
| 2  | 2  | 6  | Wunsch             |
| 1  | 2  | 3  | Das Unvermeidliche |
| 2  | 3  | 2  | Wunsch             |
| 2  | 3  | 3  | Wunsch             |
| 2  | 3  | 4  | Das Unvermeidliche |
| 2  | 3  | 5  | Das Unvermeidliche |
| 2  | 3  | 6  | Das Unvermeidliche |
| 1  | 2  | 4  | Das Unvermeidliche |
| 2  | 4  | 2  | Wunsch             |
| 2  | 3  | 4  | Das Unvermeidliche |
| 2  | 4  | 4  | Wunsch             |
| 2  | 4  | 5  | Das Unvermeidliche |
| 2  | 4  | 6  | Einhorn            |
| 1  | 2  | 5  | Das Unvermeidliche |
| 2  | 5  | 2  | Wunsch             |
| 2  | 3  | 5  | Das Unvermeidliche |
| 2  | 4  | 5  | Das Unvermeidliche |
| 2  | 5  | 5  | Wunsch             |
| 2  | 5  | 6  | Das Unvermeidliche |
| 1  | 2  | 6  | Das Unvermeidliche |
| 2  | 6  | 2  | Wunsch             |
| 2  | 3  | 6  | Das Unvermeidliche |
| 2  | 4  | 6  | Einhorn            |
| 2  | 5  | 6  | Das Unvermeidliche |
| 2  | 6  | 6  | Wunsch             |
| 3  | 1  | 1  | Wunsch             |
| 1  | 2  | 3  | Das Unvermeidliche |
| 3  | 1  | 3  | Wunsch             |
| 1  | 3  | 4  | Das Unvermeidliche |
| 1  | 3  | 5  | Einhorn            |
| 1  | 3  | 6  | Einhorn            |
| 1  | 2  | 3  | Das Unvermeidliche |
| 3  | 2  | 2  | Wunsch             |
| 3  | 2  | 3  | Wunsch             |
| 2  | 3  | 4  | Das Unvermeidliche |
| 2  | 3  | 5  | Das Unvermeidliche |
| 2  | 3  | 6  | Das Unvermeidliche |
| 3  | 3  | 1  | Wunsch             |
| 3  | 3  | 2  | Wunsch             |
| 3  | 3  | 3  | Dreifaltigkeit     |
| 3  | 3  | 4  | Wunsch             |
| 3  | 3  | 5  | Wunsch             |
| 3  | 3  | 6  | Wunsch             |
| 1  | 3  | 4  | Das Unvermeidliche |
| 2  | 3  | 4  | Das Unvermeidliche |
| 3  | 4  | 3  | Wunsch             |
| 3  | 4  | 4  | Wunsch             |
| 3  | 4  | 5  | Das Unvermeidliche |
| 3  | 4  | 6  | Das Unvermeidliche |
| 1  | 3  | 5  | Einhorn            |
| 2  | 3  | 5  | Das Unvermeidliche |
| 3  | 5  | 3  | Wunsch             |
| 3  | 4  | 5  | Das Unvermeidliche |
| 3  | 5  | 5  | Wunsch             |
| 3  | 5  | 6  | Das Unvermeidliche |
| 1  | 3  | 6  | Einhorn            |
| 2  | 3  | 6  | Das Unvermeidliche |
| 3  | 6  | 3  | Wunsch             |
| 3  | 4  | 6  | Das Unvermeidliche |
| 3  | 5  | 6  | Das Unvermeidliche |
| 3  | 6  | 6  | Wunsch             |
| 4  | 1  | 1  | Wunsch             |
| 1  | 2  | 4  | Das Unvermeidliche |
| 1  | 3  | 4  | Das Unvermeidliche |
| 4  | 1  | 4  | Wunsch             |
| 1  | 4  | 5  | Das Unvermeidliche |
| 1  | 4  | 6  | Einhorn            |
| 1  | 2  | 4  | Das Unvermeidliche |
| 4  | 2  | 2  | Wunsch             |
| 2  | 3  | 4  | Das Unvermeidliche |
| 4  | 2  | 4  | Wunsch             |
| 2  | 4  | 5  | Das Unvermeidliche |
| 2  | 4  | 6  | Einhorn            |
| 1  | 3  | 4  | Das Unvermeidliche |
| 2  | 3  | 4  | Das Unvermeidliche |
| 4  | 3  | 3  | Wunsch             |
| 4  | 3  | 4  | Wunsch             |
| 3  | 4  | 5  | Das Unvermeidliche |
| 3  | 4  | 6  | Das Unvermeidliche |
| 4  | 4  | 1  | Wunsch             |
| 4  | 4  | 2  | Wunsch             |
| 4  | 4  | 3  | Wunsch             |
| 4  | 4  | 4  | Dreifaltigkeit     |
| 4  | 4  | 5  | Wunsch             |
| 4  | 4  | 6  | Wunsch             |
| 1  | 4  | 5  | Das Unvermeidliche |
| 2  | 4  | 5  | Das Unvermeidliche |
| 3  | 4  | 5  | Das Unvermeidliche |
| 4  | 5  | 4  | Wunsch             |
| 4  | 5  | 5  | Wunsch             |
| 4  | 5  | 6  | Das Unvermeidliche |
| 1  | 4  | 6  | Einhorn            |
| 2  | 4  | 6  | Einhorn            |
| 3  | 4  | 6  | Das Unvermeidliche |
| 4  | 6  | 4  | Wunsch             |
| 4  | 5  | 6  | Das Unvermeidliche |
| 4  | 6  | 6  | Wunsch             |
| 5  | 1  | 1  | Wunsch             |
| 1  | 2  | 5  | Das Unvermeidliche |
| 1  | 3  | 5  | Einhorn            |
| 1  | 4  | 5  | Das Unvermeidliche |
| 5  | 1  | 5  | Wunsch             |
| 1  | 5  | 6  | Das Unvermeidliche |
| 1  | 2  | 5  | Das Unvermeidliche |
| 5  | 2  | 2  | Wunsch             |
| 2  | 3  | 5  | Das Unvermeidliche |
| 2  | 4  | 5  | Das Unvermeidliche |
| 5  | 2  | 5  | Wunsch             |
| 2  | 5  | 6  | Das Unvermeidliche |
| 1  | 3  | 5  | Einhorn            |
| 2  | 3  | 5  | Das Unvermeidliche |
| 5  | 3  | 3  | Wunsch             |
| 3  | 4  | 5  | Das Unvermeidliche |
| 5  | 3  | 5  | Wunsch             |
| 3  | 5  | 6  | Das Unvermeidliche |
| 1  | 4  | 5  | Das Unvermeidliche |
| 2  | 4  | 5  | Das Unvermeidliche |
| 3  | 4  | 5  | Das Unvermeidliche |
| 5  | 4  | 4  | Wunsch             |
| 5  | 4  | 5  | Wunsch             |
| 4  | 5  | 6  | Das Unvermeidliche |
| 5  | 5  | 1  | Wunsch             |
| 5  | 5  | 2  | Wunsch             |
| 5  | 5  | 3  | Wunsch             |
| 5  | 5  | 4  | Wunsch             |
| 5  | 5  | 5  | Dreifaltigkeit     |
| 5  | 5  | 6  | Wunsch             |
| 1  | 5  | 6  | Das Unvermeidliche |
| 2  | 5  | 6  | Das Unvermeidliche |
| 3  | 5  | 6  | Das Unvermeidliche |
| 4  | 5  | 6  | Das Unvermeidliche |
| 5  | 6  | 5  | Wunsch             |
| 5  | 6  | 6  | Wunsch             |
| 6  | 1  | 1  | Wunsch             |
| 1  | 2  | 6  | Das Unvermeidliche |
| 1  | 3  | 6  | Einhorn            |
| 1  | 4  | 6  | Einhorn            |
| 1  | 5  | 6  | Das Unvermeidliche |
| 6  | 1  | 6  | Wunsch             |
| 1  | 2  | 6  | Das Unvermeidliche |
| 6  | 2  | 2  | Wunsch             |
| 2  | 3  | 6  | Das Unvermeidliche |
| 2  | 4  | 6  | Einhorn            |
| 2  | 5  | 6  | Das Unvermeidliche |
| 6  | 2  | 6  | Wunsch             |
| 1  | 3  | 6  | Einhorn            |
| 2  | 3  | 6  | Das Unvermeidliche |
| 6  | 3  | 3  | Wunsch             |
| 3  | 4  | 6  | Das Unvermeidliche |
| 3  | 5  | 6  | Das Unvermeidliche |
| 6  | 3  | 6  | Wunsch             |
| 1  | 4  | 6  | Einhorn            |
| 2  | 4  | 6  | Einhorn            |
| 3  | 4  | 6  | Das Unvermeidliche |
| 6  | 4  | 4  | Wunsch             |
| 4  | 5  | 6  | Das Unvermeidliche |
| 6  | 4  | 6  | Wunsch             |
| 1  | 5  | 6  | Das Unvermeidliche |
| 2  | 5  | 6  | Das Unvermeidliche |
| 3  | 5  | 6  | Das Unvermeidliche |
| 4  | 5  | 6  | Das Unvermeidliche |
| 6  | 5  | 5  | Wunsch             |
| 6  | 5  | 6  | Wunsch             |
| 6  | 6  | 1  | Wunsch             |
| 6  | 6  | 2  | Wunsch             |
| 6  | 6  | 3  | Wunsch             |
| 6  | 6  | 4  | Wunsch             |
| 6  | 6  | 5  | Wunsch             |
| 6  | 6  | 6  | Dreifaltigkeit     |
