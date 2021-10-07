# Einhorn

| Einhorn | TL;DR |
|------------------------------|------------------------------------------|
| ![einhorn.png](_einhorn.png) | Einhorn is a game for 2-6 players and takes about 30min to play. The rules are rather simple, the game is fast paced and luck is a main factor to winning the game. </br> </br> Each player starts with six stones. Bet on your roll outcome and receive or pay stones. The first player with no stones left loses and the game ends. All other players keep their stones. Bet on the Einhorn to steal stones from other players. After ten games, the player with the most stones wins. |

Below is an overview of how the game is setup and played.

![wuerfeln](wuerfeln.drawio.svg)

## Prepare the game

**Setup the game**

- Put all stones in a bowl. (also called "central stash")
- Place the dice tray centrally.
- Place the game counter dice (D10) in the center and set it to 1.
- Place the Einhorn-figure centrally between dice tray and central stash.
- Each player receives 3x six sided dice (D6), a card with the roll-result overview and 6 stones.

**Agree on the win condition**

- Agree on how many games shall be played to determine the winner (default is 10)

**Determine who starts**

- All players roll all three dice once and the player with highest sum starts the game.
- If there is a draw, those players roll again until a starting player is determined.
- The player that starts the game receives an additional stone.

This is an example setup for 4 players:

![wuerfeln-setup](wuerfeln-setup.drawio.svg)

### Understanding the stone stashes

Understand the difference between game stones, players stones stash and the central stone stash:

| Term          | Explanation |
|---------------|----------------------------------------|
| Game stones   | Stones a player has for the [current game](#play). </br> If a player has no more stones the [game ends](#game-ends).                                                                                                                                                                         |
| Player stash  | Stones a player has won in previous games. </br> Only usable when [betting on the unicorn](#bidding-on-the-einhorn) and </br> when [adding stones](#receive-6-stones) to the six game stones at the beginning of a new game.</br>The player with the most stones in this stash wins the game. |
| Central stash | All stones remaining in the game. </br> [Take stones or return stones](#take-or-return-stones) depending on your roll prediction outcome.                                                                                                                                                    |

## Play

This section explains the actions in a players turn and how one game is played. One game may be as fast as 1min but can also take 10min depending on how fast one player looses all stones. Play 10 games for a standard match.

### Predict outcome or remain silent

The current player decides to either predict the upcoming roll attempt or to remain silent and do a passive roll, then proceeds to roll all three dice once in the dice tray.

There are 4 predictable outcomes. Below is a list of all possible results and their probability (percent of "total combinations"):

| Result                | Rule                                                                       | Example                                                                         | Combinations           |
|-----------------------|----------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------|
| ⚰️ Das Unvermeidliche | A number and that number +1 and </br> something else which is not one of the two | ```n & n+1 & (!n / !n+1)``` </br> Example: ⚀⚁⚃ or ⚂⚃⚀                           | 96 of 216 </br> (44,4%) |
| 🎁 Wunsch             | Two of a kind and something else </br> which is not that number                  | ```2x n & !n``` </br> Example: ⚀⚀⚁ or ⚁⚃⚁                                       | 90 of 216 </br> (41,7%) |
| 🦄 Einhorn            | All numbers must be at least 2 apart                                       | ```n & n+2 & (n+4 / n+5)``` </br> ```n & n+3 & n+5``` </br> Example: ⚀⚂⚄ or ⚀⚃⚅ | 24 of 216 </br> (11,1%) |
| ☢️ Dreifaltigkeit     | Three of a kind.                                                           | ```3x n``` </br> Example: ⚁⚁⚁ or ⚅⚅⚅                                            | 6 of 216 </br> (2,8%)   |

### Take or return stones

Based on the players roll attempt and the prediction made, there is one possible result that leads to adding or removing stones from the players game stash. E.g., in case the roll result was a `Wunsch`, read that line in your roll-result overview card, then check if the prediction was correct, wrong or passive, then add or remove stones accordingly.

| Result                | Correct                        | Wrong | Passive |
|-----------------------|--------------------------------|-------|---------|
| ⚰️ Das Unvermeidliche | +2                             | -2    | -1      |
| 🎁 Wunsch             | +2                             | -2    | -1      |
| 🦄 Einhorn            | +5                             | -5    | +1      |
| ☢️ Dreifaltigkeit     | [WIN](#rolling-dreifaltigkeit) | +1    | +5      |

As you can see from the table above, the most common roll results are `Das Unvermeidliche` and `Wunsch`. The improbable results `Einhorn` and `Dreifaltigkeit` promise higher rewards.

Please note:

- It doesn't matter what prediction was made specifically. What matters is if the prediction was correct, wrong or if no prediction was made. In other words: The stones added or removed are determined by the result rolled, not by what was predicted. E.g., if a `Wunsch` is rolled, it doesn't matter if `Das Unvermeidliche`, `Einhorn` or `Dreifaltigkeit` were predicted, all three are wrong and the player must return 2 stones to the central stash.
- If a player forgets to make a prediction or mentions the prediction too late and rolls the dice this is dealt as a passive roll.

Remember to first take or give stones, then put your dice back from the dice tray. With this action your turn ends and it's the next players turn.

#### Rolling Einhorn

When rolling an `Einhorn` this player additionally receives the Einhorn-figure.

The Einhorn-figure has the following effects:

- When rolling an `Einhorn` no stones are earned/paid = nothing happens.
- The player can give or take stones not only from the central stash, but also from any other player. However, whether the player can take stones still depends on the roll attempt outcome!
- The Einhorn-figure is passed if another player rolls an `Einhorn`.

#### Rolling Dreifaltigkeit

If you roll `Dreifaltigkeit` you will always receive stones (see [overview)](#take-or-return-stones). However, if you predict `Dreifaltigkeit` correctly (2,8% chance), you receive all game stones from all players (player stash excluded!) and therewith instantly [end the current game](#game-ends).

### Game ends

Once a player has no stones left the game ends.

- If this was the last game (e.g. game #10) or if all stones from the central stash are gone, proceed to [determine the winner](#determine-the-winner).
- Else, proceed with the steps to [prepare the next game](#prepare-next-game).

## Prepare next game

To prepare for the next game, follow these steps:

- All players take their current stones and add them to their stash.
- The Einhorn is returned to the center of the dice tray.
- The game counter is updated and layed next to Einhorn.
- All players [bid on the Einhorn](#bidding-on-the-einhorn) and all stones used for bidding return to the central stash.
- Everyone [receives 6 stones](#receive-6-stones) from the central stash and players may add more stones from their stash.
- A [new game](play) begins and the owner of the Einhorn starts.

### Bidding on the Einhorn

All players can now bet on the Einhorn with their stones available from their own stash as described above.

Bidding on the Einhorn works as follows:

- Place the Einhorn in the middle of the dice tray.
- All players bet with their personal stone stash (if available) to receive the Einhorn in the next game. You may bid zero stones if you want but you have to bid!
- Do not show how much you are bidding until all reveal their bet at the same time.
- All players put their stones used for the bid in the central stash.
- The Einhorn goes to the highest bidder. In case there is a tie all highest bidders roll their 3 dice and the player with the highest total sum receives the Einhorn-figure. E.g., if all bid zero, all must roll their dice. In case there is another tie the remaining players re-roll the dice until a winner can be determined.

### Receive 6 stones

- All players receive 6 stones from the central stash.
- Players with a personal stone stash may choose to add stones to their stones for the current game at this time only.
- You can only loose stones added to the current game. Stones in a players personal stash can only be used to bet on the Einhorn and add stones for the next game.

## Determine the winner

All players put their remaining stones in their own stone stash.

Winner of the game is the player with most stones. In case of a tie, all tied players are ranked 1 place.

## Extras

This is not needed to understand or play the game.

??? check "Example game"
    The following is an example game play with three players:

    Preparing the game:

    - All players agree to play the default of 10 games.
    - All players take 3 dice and 6 stones.
    - Player 1 rolls the highest total number with 3 dice (1+4+5=10) and may start the game. Player 1 receives an extra stone.

    First game:

    - Player 1 starts the game and bets on rolling a `Wunsch`. Player 1 then proceeds to roll 1,2,5 which is `das unvermeidliche` and therefore loses 2 stones. Player 1 started with 7 stones and now has 5. Now it is the next players turn.
    - The 2nd player predicts an `Einhorn` and rolls a 1,3,6 and therefore gains 5 stones as well as the Einhorn-figure.
    - The 3rd player choses to not predict anything and rolls 2,2,2 which is `Dreifaltigkeit`. In this case the player gains one stone.
    - It is player 1 turn again and predicts `das unvermeidliche`, then rolls 3,1,4 which is `das unvermeidliche`. Player 2 takes one stone from the central stash.
    - Player 2 now has the `Einhorn` and predicts `das unvermeidliche` as well and rolls 4,5,6 which is `das unvermeidliche`. Player 2 takes the 2 stones from player 1 instead of the central stash.

    The game goes on like this until, in our example, player 2 loses the first game. At this point player 1 has 8 stones and player 3 has 4 stones.

    The `Einhorn` is now returned (player 3 had it last) and placed on the dice tray. The `Einhorn` is now open for auction. Since this is the first game and player 2 lost the game there are no stones to bet with for this player. Player 1 bets 3 stones and player 3 bets 1 stone. Both players put the stones they bet in the central stash and player 1 receives the Einhorn-figure. Player 1 now has 8-3=5 stones in their own stone stash and player 3 has 4-1 stones in their stash.

    All players now receive 6 new stones. Player 1 decides to add 2 stones from the own stash to the current play stash. Player 1 now has 4 stones remaining in their own stash and 6+2=8 stones to play with in this game as well as the Einhorn-figure. Both other players do not add stones and start with 6 stones.

    Player 1 with the Einhorn-figure starts the new game and the game continues.

    At the end of game 10 player 1 has 20 stones, player 2 has 15 stones and player 3 has 22 stones. Player 3 therefore wins the game.

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

??? warning "Warning: Math"
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

    You can copy ```(6+3-1)!/(3!*(6-1)!)``` to WolframAlpha to calculate it or use [this link](https://www.wolframalpha.com/input/?i=%286%2B3-1%29%21%2F%283%21*%286-1%29%21%29).

    These 56 combinations distribute as follows:

    | Result                |                                                                                                                                                                     | Amount | Percent |
    |-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------|
    | ⚰️ Das Unvermeidliche | ⚀⚁⚃, ⚀⚁⚄, ⚀⚁⚅, ⚁⚂⚀ </br> ⚁⚂⚄, ⚁⚂⚅, ⚂⚃⚀, ⚂⚃⚁</br>⚂⚃⚅, ⚃⚄⚀, ⚃⚄⚁, ⚃⚄⚂, </br> ⚄⚅⚀, ⚄⚅⚁, ⚄⚅⚂, ⚄⚅⚃                                                                        | 16     | 29 %    |
    | 🎁 Wunsch             | ⚀⚀⚁, ⚀⚀⚂, ⚀⚀⚃, ⚀⚀⚄, ⚀⚀⚅</br>⚁⚁⚀, ⚁⚁⚂, ⚁⚁⚃, ⚁⚁⚄, ⚁⚁⚅</br>⚂⚂⚀, ⚂⚂⚁, ⚂⚂⚃, ⚂⚂⚄, ⚂⚂⚅</br>⚃⚃⚀, ⚃⚃⚁, ⚃⚃⚂, ⚃⚃⚄, ⚃⚃⚅</br>⚄⚄⚀, ⚄⚄⚁, ⚄⚄⚂, ⚄⚄⚃, ⚄⚄⚅</br>⚅⚅⚀, ⚅⚅⚁, ⚅⚅⚂, ⚅⚅⚃, ⚅⚅⚄ | 30     | 54 %    |
    | 🦄 Einhorn            | ⚀⚂⚄, ⚀⚂⚅, ⚀⚃⚅, ⚁⚃⚅                                                                                                                                                  | 4      | 7 %     |
    | ☢️ Dreifaltigkeit     | ⚀⚀⚀, ⚁⚁⚁, ⚂⚂⚂</br>⚃⚃⚃, ⚄⚄⚄, ⚅⚅⚅                                                                                                                                     | 6      | 11 %    |

    However, this is not the probability of each combination since the distinct combinations are not evenly distributed over the 216 possible outcomes.

    I do not know how to calculate this, so I created a python script and analyzed of all possible outcomes. To view the full list, expand "Full list of possible dice combinations". The outcome is as follows:

    | Result               | total      | distinct |
    |----------------------|------------|----------|
    | ⚰️ Das Unvermeidlich | 96 (44,4%) | 16 (29%) |
    | 🎁 Wunsch            | 90 (41,7%) | 30 (54%) |
    | 🦄 Einhorn           | 24 (11,1%) | 4 (7%)   |
    | ☢️ Dreifaltigkeit    | 6 (2,8%)   | 6 (11%)  |

    The result shows that Das Unvermeidliche has less distinct variations than Wunsch but more possible combinations.

??? note "Script to analyze all possible roll attempts"
    Here is the python script I wrote to calculate the result:

    ```py
    # Check groups for Einhorn game:
    # Step 1 create all possible options for 3x D6 dice
    # Step 2 remove doubles -> if total is 1 = Dreifaltigkeit, 2 = Wunsch
    # Step 3 with all remaining sort numbers and count min distance between all three values. If min distance is 1 = Unvermeidlich, else Einhorn

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
                print(sortedRoll, " Unvermeidlich")
                Unvermeidlich += 1
            else:
                print(sortedRoll, " Einhorn")
                Einhorn += 1

    # Print stats
    print("\nTotal amount of possible rolls: ", len(rolls))
    print("Total amount of distint rolls: ", int((math.factorial(diceFaces+diceAmount-1))/(math.factorial(diceAmount)*(math.factorial(diceFaces-1)))))

    print("\nDreifaltigkeit: ", Dreifaltigkeit, "({:.1f}".format(Dreifaltigkeit / len(rolls) * 100), "%)")
    print("Wunsch: ", Wunsch, "({:.1f}".format(Wunsch / len(rolls) * 100), "%)")
    print("Unvermeidlich: ", Unvermeidlich, "({:.1f}".format(Unvermeidlich / len(rolls) * 100), "%)")
    print("Einhorn: ", Einhorn, "({:.1f}".format(Einhorn / len(rolls) * 100), "%)")
    ```

??? tip "Creating the game"
    **Dice tray**

    - Option 1: Laser cut from boxes.py: You can create a simple box using [boxes.py](https://www.festi.info/boxes.py) with these [settings](https://www.festi.info/boxes.py/TwoPiece?FingerJoint_angle=90.0&FingerJoint_style=rectangular&FingerJoint_surroundingspaces=2.0&FingerJoint_edge_width=1.0&FingerJoint_finger=2.0&FingerJoint_play=0.0&FingerJoint_space=2.0&FingerJoint_width=1.0&x=182&y=182&h=65&hi=0.0&outside=0&play=0.15&thickness=3.0&format=svg&tabs=0.0&debug=0&labels=0&labels=1&reference=100&burn=0.1&render=1). I used [these settings](_wuerfeln.jpg). Here are the files for the laser cutter: [SVG](_wuerfeln.svg), [CDR-part1](_wuerfeln.cdr) and [CDR-part2](_wuerfeln2.cdr). This box is perfect for 6 foldable dice trays, D6 and D10 dice, stones and unicorn. In this setup i recommend using one sack for the stones and one for everything else.
    - Option 2: Laser cut from thingiverse: I found a great design on [thingiverse](https://www.thingiverse.com) called [Octagonal Dice Tray, Laser Cut](https://www.thingiverse.com/thing:3694820) by [Patrik Grip-Jansson (kap42)](https://www.thingiverse.com/kap42/designs).
    - Option 3: Buy a dice tray:  Try to find a dice tray with a top/lid. There are some nice but expensive octagonal shaped dice trays available. I even found one with a unicorn artwork :)
    
    **Dice**

    There are no real options here. Buy some nice dice: You need 3 dice of the same color and 6 different colors so a total of 18x D6. 12mm is a good size for a dice. I prefer the numbers written on the sides instead of the dots but both is perfectly fine. Additionally, you need a D10 to count the games played. As always, it is cheaper to buy in bulk and dice packs are available in a 36x dice box as well as mixed color option for 50x dice and 100x dice. This way you should spend about 7 Euro for all dice.

    **Stones**

    - Option 1: Go outside and collect stones. Paint them with acrylic paint if you like.
    - Option 2: Drum stones feel and look great and this what i went with. You can save a lot of money when buying in bulk (e.g. 5kg), mixed stones and avoid terms like esoteric, etc. However, anything can be used as long as enough fit in the dice tray and are more or less the same size. I tried different stone sizes and 1-2cm work best in my opinion. stone costs vary a lot but I spent about 6 Euro for the stones needed for one game.
    - Other options that could work are marbles (but round things may be annoying during play) or any small glass objects, coins, poker chips, ...    

    **Unicorn figure**

    - Option 1: You can print this [unicorn](https://www.thingiverse.com/thing:182335) design i found on [thingiverse](https://www.thingiverse.com) by [Yahoo! JAPAN](https://www.thingiverse.com/yahoojapan/designs) and color it with spray paint and acrylic paint.
    - Option 2: I found a set of 10 unicorns used to decorate cakes for 10 Euro. The quality is not the best but it fits the purpose. Since I will be creating a few games I think I can use the extra unicorns (and they make a good small present as well) so I spent about 1 Euro on the unicorn.

??? info  "Full list of possible dice combinations"
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
