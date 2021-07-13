# Würfeln

```Würfeln ist Einstellungssache``` is a game of luck and high precision dice rolling. Tweak statistics to your advantage with the right mindset. Is your dice roll determination stronger than the one of your opponents? Challenge up to five opponents, bet on your roll attempts and show that you have mastered the art of rolling the die.

## How to play

Bet on your role outcome and receive or pay rocks. Beware of the 🦄. The first player with 0 rocks loses the round. All other players keep their rocks. Bet on the 🦄 and play another rounds until all rocks are gone, a player has the agreed amount of rocks in their stash or see who has the most rocks after an agreed amount of rounds.

### Setup

Setup the game by providing 3 dice per player and at least 50 rocks. Ideally you have a bowl for the rocks and centrally placed place to roll the dice. Place the 🦄 next to the central rock stash.

Agree on how many rounds shall be played to determine the winner.

To start, each player gets

- 3 standard D6 (numbers 1-6) dice
- 6 rocks

Each player rolls all three die once and the player with highest total number starts the game. If there is a draw those players role again until a starting player is determined.

### Play

The current player decides to either predict the upcoming roll or not (passive roll) - then proceeds to roll all three die once.

There are 4 different predictable outcomes. Below is a list of all possible combinations and their probability:

| Result         | Rule / Example    | Total Combinations | Distinct Combinations |
|----------------|-------------------|--------------------|-----------------------|
| ⚰️ Unvermeidlich  | ```n & n+1 & (!n / !n+1)```  </br>Example: ⚀⚁⚃ or ⚂⚃⚀ | 97 (45%)           | 16 (29%)               |
| 🎁 Wunsch         | ```2x n & !n```   </br>Example: ⚀⚀⚁        | 89 (41%)           | 30 (54%)               |
| 🦄 Einhorn        | ```n & n+2 & (n+4 / n+5)```</br>```n & n+3 & n+5``` </br>Example: ⚀⚂⚄ or ⚀⚃⚅ | 24 (11%)           | 4 (7%)                 |
| ☢️ Dreifaltigkeit | ```3x n```  </br>Example: ⚁⚁⚁ or ⚅⚅⚅ | 6 (3%)             | 6 (11%)                |

For a list of all combinations and total possible combinations view the overview at the bottom.

Based on the result of the players role attempt add or remove rocks as follows:

| Result                | Correct | Wrong | Passive |
|-----------------------|---------|-------|---------|
| ⚰️ Das Unvermeidliche | +1      | -1    | -1      |
| 🎁 Wunsch             | +1      | -1    | 0       |
| 🦄 Einhorn            | +5      | -5    | -2      |
| ☢️ Dreifaltigkeit     | +9      | +3    | +6      |

In case the role result was a 🎁 go to that line in the table, then check if the prediction was correct/wrong or passive and add or remove rocks accordingly. It does not matter what prediction was made specificity. All that matters is if the prediction was correct, wrong or if no prediction was made.

### Einhorn

Additionally to the rocks earned/payed, a player that rolls an 🦄 receives the 🦄 figure.

Once a player receives the 🦄 figure:

- When rolling an 🦄 no rocks are earned/payed (nothing happens).
- A player with the 🦄 can give and take (depending on the roll attempt outcome) rocks either from the central stash or from any other player.
- The 🦄 is passed once another player roles an 🦄. The player gaining the 🦄 also receives one stone from the player loosing the 🦄.

Once the round ends the 🦄 is placed in the middle of the dice rolling area and all players bet with their personal rock stash (if available) to receive the 🦄 in the next round. It is recommended to not show how much you are bidding on the 🦄. You may bid zero rocks if you want. The 🦄 goes to the highest bidder but all bidders loose all the rocks used to bet for the 🦄 and place those rocks in the central stash. In case there is a tie all highest bidders role their 3 die and the player with the highest total sum receives the 🦄. If all bid zero, all must role the die. This step is repeated in case there is another tie. The player with the 🦄 starts the next round.

### How to win

The first player with no rocks left loses the round. The round ends at this point and all players put their remaining rocks in their rock stash.

All players then bet on the 🦄 und begin another round. (see above)

For the new round all players receive 6 rocks from the main stash. Players with a personal rock stash may choose to add rocks to their current game stash at this time only.

## Example game

The following is an example game play with three players:

All players agree to play 5 rounds.

- Player 1 starts the game and bets on rolling a 🎁. Player 1 then proceeds to roll 1,2,5 which is ⚰️ and therefore loses 1 rock. Player 1 started with 6 rocks and now has 5. Now it is the next players turn.
- The 2nd player predicts an 🦄 and rolls a 1,3,6 and therefore gains 5 rocks.
- The 3rd player choses to not predict anything and rolls 2,2,2 which is ☢️. In this case the player gains 6 rocks.
- It is player 1 turn again and predicts ⚰️, then rolls 3,1,4 which is ⚰️. Player 1 takes one rock from the central stash.
- Player 2 now has the 🦄 and predicts ⚰️ as well and rolls 4,5,6 which is ⚰️. Player 2 takes the rock from player 1 instead of the central stash.

The game goes on like this for a while until in this case player 2 looses the first round. At this point player 1 has 6 rocks and player 3 has 4 rocks.

The 🦄 is now open for auction. Since this is the 1st round and player 2 lost the game there are no rocks to bet with for this player. Player 1 bets 3 rocks and player 3 bets 1 rock. Both players put the rocks they bet in the center stash and player 1 receives the 🦄.

All players now receive 6 new rocks. Player 1 decides to add 2 rocks from the own stash to the current player stash. Player 1 now has 1 rock remaining in the stash and 8 rocks to play with for the round as well as the 🦄 figure. Both other players do not add rocks and start with 6 rocks.

Player 1 with the 🦄 starts the new round and the game continues.

At the end of round 5 player 1 has 20 rocks, player 2 has 15 rocks and player 3 has 22 rocks. Player 3 wins the game.

## Extras

This is not needed to understand or play the game. If you are interested have a look at the math part or see all possible dice combinations :)

<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>

??? warning "Warning: Math"
    With 3x D6 we get a total of 216 (6x6x6 or 6^3) possible outcomes.

    Let us now look at unique roles. To get all possible combinations we can use this formula for combination with repetition:

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

    I do not know how to calculate this so I created a list of all possible outcomes. To view the full list expand "Full list of possible die combinations". The outcome is as follows:

    | Result               | total    | distinct |
    |----------------------|----------|----------|
    | ⚰️ Das Unvermeidlich | 97 (45%) | 16 (29%) |
    | 🎁 Wunsch            | 89 (41%) | 30 (54%) |
    | 🦄 Einhorn           | 24 (11%) | 4 (7%)   |
    | ☢️ Dreifaltigkeit    | 6 (3%)   | 6 (11%)  |

    The result shows that Das Unvermeidliche has less distinct variations than Wunsch but more possible combinations.

??? info "Full list of possible die combinations"
    This is a full list of all possible die throws in this game and the result based on the described rules above.

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
    | 1  | 3  | 2  | Das Unvermeidliche |
    | 1  | 3  | 3  | Wunsch             |
    | 1  | 3  | 4  | Das Unvermeidliche |
    | 1  | 3  | 5  | Einhorn            |
    | 1  | 3  | 6  | Einhorn            |
    | 1  | 4  | 1  | Wunsch             |
    | 1  | 4  | 2  | Das Unvermeidliche |
    | 1  | 4  | 3  | Das Unvermeidliche |
    | 1  | 4  | 4  | Wunsch             |
    | 1  | 4  | 5  | Das Unvermeidliche |
    | 1  | 4  | 6  | Einhorn            |
    | 1  | 5  | 1  | Wunsch             |
    | 1  | 5  | 2  | Das Unvermeidliche |
    | 1  | 5  | 3  | Einhorn            |
    | 1  | 5  | 4  | Das Unvermeidliche |
    | 1  | 5  | 5  | Wunsch             |
    | 1  | 5  | 6  | Das Unvermeidliche |
    | 1  | 6  | 1  | Wunsch             |
    | 1  | 6  | 2  | Das Unvermeidliche |
    | 1  | 6  | 3  | Einhorn            |
    | 1  | 6  | 4  | Einhorn            |
    | 1  | 6  | 5  | Das Unvermeidliche |
    | 1  | 6  | 6  | Wunsch             |
    | 2  | 1  | 1  | Wunsch             |
    | 2  | 1  | 2  | Wunsch             |
    | 2  | 1  | 3  | Das Unvermeidliche |
    | 2  | 1  | 4  | Das Unvermeidliche |
    | 2  | 1  | 5  | Das Unvermeidliche |
    | 2  | 1  | 6  | Das Unvermeidliche |
    | 2  | 2  | 1  | Wunsch             |
    | 2  | 2  | 2  | Dreifaltigkeit     |
    | 2  | 2  | 3  | Wunsch             |
    | 2  | 2  | 4  | Wunsch             |
    | 2  | 2  | 5  | Wunsch             |
    | 2  | 2  | 6  | Wunsch             |
    | 2  | 3  | 1  | Das Unvermeidliche |
    | 2  | 3  | 2  | Wunsch             |
    | 2  | 3  | 3  | Wunsch             |
    | 2  | 3  | 4  | Das Unvermeidliche |
    | 2  | 3  | 5  | Das Unvermeidliche |
    | 2  | 3  | 6  | Das Unvermeidliche |
    | 2  | 4  | 1  | Das Unvermeidliche |
    | 2  | 4  | 2  | Wunsch             |
    | 2  | 4  | 3  | Das Unvermeidliche |
    | 2  | 4  | 4  | Wunsch             |
    | 2  | 4  | 5  | Das Unvermeidliche |
    | 2  | 4  | 6  | Einhorn            |
    | 2  | 5  | 1  | Das Unvermeidliche |
    | 2  | 5  | 2  | Wunsch             |
    | 2  | 5  | 3  | Das Unvermeidliche |
    | 2  | 5  | 4  | Das Unvermeidliche |
    | 2  | 5  | 5  | Wunsch             |
    | 2  | 5  | 6  | Das Unvermeidliche |
    | 2  | 6  | 1  | Das Unvermeidliche |
    | 2  | 6  | 2  | Wunsch             |
    | 2  | 6  | 3  | Das Unvermeidliche |
    | 2  | 6  | 4  | Einhorn            |
    | 2  | 6  | 5  | Das Unvermeidliche |
    | 2  | 6  | 6  | Wunsch             |
    | 3  | 1  | 1  | Wunsch             |
    | 3  | 1  | 2  | Das Unvermeidliche |
    | 3  | 1  | 3  | Wunsch             |
    | 3  | 1  | 4  | Das Unvermeidliche |
    | 3  | 1  | 5  | Einhorn            |
    | 3  | 1  | 6  | Einhorn            |
    | 3  | 2  | 1  | Das Unvermeidliche |
    | 3  | 2  | 2  | Wunsch             |
    | 3  | 2  | 3  | Wunsch             |
    | 3  | 2  | 4  | Das Unvermeidliche |
    | 3  | 2  | 5  | Das Unvermeidliche |
    | 3  | 2  | 6  | Das Unvermeidliche |
    | 3  | 3  | 1  | Wunsch             |
    | 3  | 3  | 2  | Wunsch             |
    | 3  | 3  | 3  | Dreifaltigkeit     |
    | 3  | 3  | 4  | Wunsch             |
    | 3  | 3  | 5  | Wunsch             |
    | 3  | 3  | 6  | Wunsch             |
    | 3  | 4  | 1  | Das Unvermeidliche |
    | 3  | 4  | 2  | Das Unvermeidliche |
    | 3  | 4  | 3  | Wunsch             |
    | 3  | 4  | 4  | Das Unvermeidliche |
    | 3  | 4  | 5  | Das Unvermeidliche |
    | 3  | 4  | 6  | Das Unvermeidliche |
    | 3  | 5  | 1  | Einhorn            |
    | 3  | 5  | 2  | Das Unvermeidliche |
    | 3  | 5  | 3  | Wunsch             |
    | 3  | 5  | 4  | Das Unvermeidliche |
    | 3  | 5  | 5  | Wunsch             |
    | 3  | 5  | 6  | Das Unvermeidliche |
    | 3  | 6  | 1  | Einhorn            |
    | 3  | 6  | 2  | Das Unvermeidliche |
    | 3  | 6  | 3  | Wunsch             |
    | 3  | 6  | 4  | Das Unvermeidliche |
    | 3  | 6  | 5  | Das Unvermeidliche |
    | 3  | 6  | 6  | Wunsch             |
    | 4  | 1  | 1  | Wunsch             |
    | 4  | 1  | 2  | Das Unvermeidliche |
    | 4  | 1  | 3  | Das Unvermeidliche |
    | 4  | 1  | 4  | Wunsch             |
    | 4  | 1  | 5  | Das Unvermeidliche |
    | 4  | 1  | 6  | Einhorn            |
    | 4  | 2  | 1  | Das Unvermeidliche |
    | 4  | 2  | 2  | Wunsch             |
    | 4  | 2  | 3  | Das Unvermeidliche |
    | 4  | 2  | 4  | Wunsch             |
    | 4  | 2  | 5  | Das Unvermeidliche |
    | 4  | 2  | 6  | Einhorn            |
    | 4  | 3  | 1  | Das Unvermeidliche |
    | 4  | 3  | 2  | Das Unvermeidliche |
    | 4  | 3  | 3  | Wunsch             |
    | 4  | 3  | 4  | Wunsch             |
    | 4  | 3  | 5  | Das Unvermeidliche |
    | 4  | 3  | 6  | Das Unvermeidliche |
    | 4  | 4  | 1  | Wunsch             |
    | 4  | 4  | 2  | Wunsch             |
    | 4  | 4  | 3  | Wunsch             |
    | 4  | 4  | 4  | Dreifaltigkeit     |
    | 4  | 4  | 5  | Wunsch             |
    | 4  | 4  | 6  | Wunsch             |
    | 4  | 5  | 1  | Das Unvermeidliche |
    | 4  | 5  | 2  | Das Unvermeidliche |
    | 4  | 5  | 3  | Das Unvermeidliche |
    | 4  | 5  | 4  | Wunsch             |
    | 4  | 5  | 5  | Wunsch             |
    | 4  | 5  | 6  | Das Unvermeidliche |
    | 4  | 6  | 1  | Einhorn            |
    | 4  | 6  | 2  | Einhorn            |
    | 4  | 6  | 3  | Das Unvermeidliche |
    | 4  | 6  | 4  | Wunsch             |
    | 4  | 6  | 5  | Das Unvermeidliche |
    | 4  | 6  | 6  | Wunsch             |
    | 5  | 1  | 1  | Wunsch             |
    | 5  | 1  | 2  | Das Unvermeidliche |
    | 5  | 1  | 3  | Einhorn            |
    | 5  | 1  | 4  | Das Unvermeidliche |
    | 5  | 1  | 5  | Wunsch             |
    | 5  | 1  | 6  | Das Unvermeidliche |
    | 5  | 2  | 1  | Das Unvermeidliche |
    | 5  | 2  | 2  | Wunsch             |
    | 5  | 2  | 3  | Das Unvermeidliche |
    | 5  | 2  | 4  | Das Unvermeidliche |
    | 5  | 2  | 5  | Wunsch             |
    | 5  | 2  | 6  | Das Unvermeidliche |
    | 5  | 3  | 1  | Einhorn            |
    | 5  | 3  | 2  | Das Unvermeidliche |
    | 5  | 3  | 3  | Wunsch             |
    | 5  | 3  | 4  | Das Unvermeidliche |
    | 5  | 3  | 5  | Wunsch             |
    | 5  | 3  | 6  | Das Unvermeidliche |
    | 5  | 4  | 1  | Das Unvermeidliche |
    | 5  | 4  | 2  | Das Unvermeidliche |
    | 5  | 4  | 3  | Das Unvermeidliche |
    | 5  | 4  | 4  | Wunsch             |
    | 5  | 4  | 5  | Wunsch             |
    | 5  | 4  | 6  | Das Unvermeidliche |
    | 5  | 5  | 1  | Wunsch             |
    | 5  | 5  | 2  | Wunsch             |
    | 5  | 5  | 3  | Wunsch             |
    | 5  | 5  | 4  | Wunsch             |
    | 5  | 5  | 5  | Dreifaltigkeit     |
    | 5  | 5  | 6  | Wunsch             |
    | 5  | 6  | 1  | Das Unvermeidliche |
    | 5  | 6  | 2  | Das Unvermeidliche |
    | 5  | 6  | 3  | Das Unvermeidliche |
    | 5  | 6  | 4  | Das Unvermeidliche |
    | 5  | 6  | 5  | Wunsch             |
    | 5  | 6  | 6  | Wunsch             |
    | 6  | 1  | 1  | Wunsch             |
    | 6  | 1  | 2  | Das Unvermeidliche |
    | 6  | 1  | 3  | Einhorn            |
    | 6  | 1  | 4  | Einhorn            |
    | 6  | 1  | 5  | Das Unvermeidliche |
    | 6  | 1  | 6  | Wunsch             |
    | 6  | 2  | 1  | Das Unvermeidliche |
    | 6  | 2  | 2  | Wunsch             |
    | 6  | 2  | 3  | Das Unvermeidliche |
    | 6  | 2  | 4  | Einhorn            |
    | 6  | 2  | 5  | Das Unvermeidliche |
    | 6  | 2  | 6  | Wunsch             |
    | 6  | 3  | 1  | Einhorn            |
    | 6  | 3  | 2  | Das Unvermeidliche |
    | 6  | 3  | 3  | Wunsch             |
    | 6  | 3  | 4  | Das Unvermeidliche |
    | 6  | 3  | 5  | Das Unvermeidliche |
    | 6  | 3  | 6  | Wunsch             |
    | 6  | 4  | 1  | Einhorn            |
    | 6  | 4  | 2  | Einhorn            |
    | 6  | 4  | 3  | Das Unvermeidliche |
    | 6  | 4  | 4  | Wunsch             |
    | 6  | 4  | 5  | Das Unvermeidliche |
    | 6  | 4  | 6  | Wunsch             |
    | 6  | 5  | 1  | Das Unvermeidliche |
    | 6  | 5  | 2  | Das Unvermeidliche |
    | 6  | 5  | 3  | Das Unvermeidliche |
    | 6  | 5  | 4  | Das Unvermeidliche |
    | 6  | 5  | 5  | Wunsch             |
    | 6  | 5  | 6  | Wunsch             |
    | 6  | 6  | 1  | Wunsch             |
    | 6  | 6  | 2  | Wunsch             |
    | 6  | 6  | 3  | Wunsch             |
    | 6  | 6  | 4  | Wunsch             |
    | 6  | 6  | 5  | Wunsch             |
    | 6  | 6  | 6  | Dreifaltigkeit     |
