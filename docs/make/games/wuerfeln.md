# Würfeln

```Würfeln ist Einstellungssache``` is a game of luck and high precision dice rolling. Tweak statistics to your advantage with the right mindset. Is your dice roll determination stronger than the one of your opponents? Challenge up to five opponents, bet on your roll attempts and show that you have mastered the art of rolling the die.

## How to play

Bet on your role outcome and receive or pay rocks. Beware of the unicorn. The first player with 0 rocks loses the round. All other players keep their rocks. Bet on the unicorn and play another rounds until all rocks are gone, a player has the agreed amount of rocks in their stash or see who has the most rocks after an agreed amount of rounds.

### Setup

Setup the game by providing 3 dice per players and at least 50 rocks. Ideally you have a bowl for the rocks and centrally placed place to roll the dice. Place the unicorn next to the central rock stash.

Agree on how many rounds shall be played to determine the winner.

To start, each player gets

- 3 standard D6 (numbers 1-6) dice
- 6 rocks

Each player rolls all three die once and the player with highest total number starts the game. If there is a draw those players role again until a starting player is determined.

### Play

The current player decides to either predict the upcoming roll or not (passive roll) - then proceeds to roll all three die once.

There are 4 different predictable outcomes. Below is a list of all possible combinations and their probability:

| Result         | Rule                                                 | Example    | Total combinations | distinct  combinations |
|----------------|------------------------------------------------------|------------|--------------------|------------------------|
| Unvermeidlich  | ```n & n+1 & (!n / !n+1)```                          | ⚀⚁⚃ or ⚂⚃⚀ | 97 (45%)           | 16 (29%)               |
| Wunsch         | ```2x n & !n```                                      | ⚀⚀⚁        | 89 (41%)           | 30 (54%)               |
| Einhorn        | ```n & n+2 & (n+4 / n+5)```</br> ```n & n+3 & n+5``` | ⚀⚂⚄ or ⚀⚃⚅ | 24 (11%)           | 4 (7%)                 |
| Dreifaltigkeit | ```3x n```                                           | ⚁⚁⚁ or ⚅⚅⚅ | 6 (3%)             | 6 (11%)                |

For a list of all combinations and total possible combinations view the overview at the bottom.

Based on the result of the players role attempt add or remove rocks (points) as follows:

| Result                | Correct | Wrong | Passive |
|-----------------------|---------|-------|---------|
| ⚰️ Das Unvermeidliche | +2      | -2    | -1      |
| 🎁 Wunsch             | +1      | -1    | 0       |
| 🦄 Einhorn            | +5      | -5    | -5      |
| ☢️ Dreifaltigkeit     | +3      | -3    | +3      |

In case the role result was a 🎁(Wunsch) go to that line in the table, then check if the prediction was correct/wrong or passive and add or remove rocks accordingly. It does not matter what prediction was made specificity. All that matters is if the prediction was correct, wrong or if no prediction was made.

### 🦄 Einhorn

Additionally to the rocks earned/payed, a player that rolls an 🦄(Einhorn) receives the Einhorn. If the player already has the Einhorn no rocks are earned/payed for rolling an Einhorn (nothing happens).

Normally all players can only take rocks from the central stash and put rocks back to the central stash depending on their role and prediction outcome. A player with the Einhorn can give and take rocks either from the central stash or from any other player. Of course a player with the Einhorn still needs to pay for mistakes from the own stash (but can give the rocks to some other player instead of putting it in the central stash if desired).

The 🦄(Einhorn) is passed once another player roles an 🦄(Einhorn).

Once the round ends the Einhorn is placed in the middle of the dice rolling area and all players bet with their personal rock stash (if available) to receive the Einhorn in the next round. It is recommended to not show how much you are bidding on the Einhorn. The Einhorn goes to the highest bidder but all bidders loose all the rocks used to bet for the Einhorn and place those rocks in the central stash. In case there is a tie all highest bidders role their 3 die and the player with the highest total sum receives the Einhorn. This step is repeated in case there is another tie. The player with the unicorn starts the next round.

### How to win

The first player with 0 rocks loses the round. The game round ends at this point and all players but their remaining rocks in their rock stash. All players then bet on the unicorn und start another rounds. For the new round all players receive 6 rocks from the main stash. Players with a personal rock stash may choose to add rocks to their current game stash at this time only.

## Example game (todo)

- If it is your turn, you bet on rolling 🎁(Wunsch) and you rolled 1,2,5 which is ⚰️(Das Unvermeidliche). Therefore, you lose 2 rocks. If this is your first round of the game, then since you started with 6 rocks and now have 4 rocks. Now it is the next players turn.
- The next player choses to not predict anything and roll a 2,2,2 which is ☢️(Dreifaltigkeit). In this case the player gains 3 points and it is the next players turn.
- The third player predicts an 🦄(Einhorn) and roll a 1,3,6 and gains 5 points.

This is the score board of an example session with 4 games and 3 players:

| Game | Player 1</br>Points -> Score | Player 2</br>Points -> Score | Player 3</br>Points -> Score |
|------|------------------------------|------------------------------|------------------------------|
| 1    | 11 -> 11+0 = 11              | 0 -> 0+0 = 0                 | 2 -> 2+0 = 2                 |
| 2    | 5 -> 5+11 = 16               | 6 -> 6+0 = 6                 | 0 -> 0+2 = 2                 |
| 3    | 0 -> 0+16 = 16               | 8 -> 8+6 = 14                | 16 -> 16+2 = 18              |
| 4    | 3 -> 3+16 = 19               | 2 -> 2+14 = 16               | 0 -> 0+18 = 18               |

Player 1 takes the lead in round one with 11 points and can continue the lead in round 2.

Player 3 gets 16 points in round three adding to 18 points in total and taking the lead.

Player 1 wins the game at the end of round 4 with a total of 19 points.

### Extras

Have a look at the math part to see all possible combinations and possibly the rules without words are interesting as well :)

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

    | Result         | total    | distinct |
    |----------------|----------|----------|
    | Das Unvermeidlich  | 97 (45%) | 16 (29%) |
    | Wunsch         | 89 (41%) | 30 (54%) |
    | Einhorn        | 24 (11%) | 4 (7%)   |
    | Dreifaltigkeit | 6 (3%)   | 6 (11%)  |

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

??? dice "Rules without words"
    👱🧔🧕

    | 👱  | 🎲 | ☑  |
    |-----|----|----|
    | 2-4 | 3  | +6 |

    🎲🎲🎲

    | =  | 🎲∑                                                  | 🎲🎲🎲                                                                                                                                                              | #  | %  |
    |----|------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|----|----|
    | ⚰️ | ```n & n+1 & (!n / !n+1)```                          | ⚀⚁⚃, ⚀⚁⚄, ⚀⚁⚅, ⚁⚂⚀ </br> ⚁⚂⚄, ⚁⚂⚅, ⚂⚃⚀, ⚂⚃⚁</br>⚂⚃⚅, ⚃⚄⚀, ⚃⚄⚁, ⚃⚄⚂, </br> ⚄⚅⚀, ⚄⚅⚁, ⚄⚅⚂, ⚄⚅⚃                                                                        | 16 | 29 |
    | 🎁 | ```2x n & !n```                                      | ⚀⚀⚁, ⚀⚀⚂, ⚀⚀⚃, ⚀⚀⚄, ⚀⚀⚅</br>⚁⚁⚀, ⚁⚁⚂, ⚁⚁⚃, ⚁⚁⚄, ⚁⚁⚅</br>⚂⚂⚀, ⚂⚂⚁, ⚂⚂⚃, ⚂⚂⚄, ⚂⚂⚅</br>⚃⚃⚀, ⚃⚃⚁, ⚃⚃⚂, ⚃⚃⚄, ⚃⚃⚅</br>⚄⚄⚀, ⚄⚄⚁, ⚄⚄⚂, ⚄⚄⚃, ⚄⚄⚅</br>⚅⚅⚀, ⚅⚅⚁, ⚅⚅⚂, ⚅⚅⚃, ⚅⚅⚄ | 30 | 54 |
    | 🦄 | ```n & n+2 & (n+4 / n+5)```</br> ```n & n+3 & n+5``` | ⚀⚂⚄, ⚀⚂⚅, ⚀⚃⚅, ⚁⚃⚅                                                                                                                                                  | 4  | 7  |
    | ☢️ | ```3x n```                                           | ⚀⚀⚀, ⚁⚁⚁, ⚂⚂⚂</br>⚃⚃⚃, ⚄⚄⚄, ⚅⚅⚅                                                                                                                                     | 6  | 11 |

    | =  | 🎲∑                                                  | ☑  | ☒  | ☐  |
    |----|------------------------------------------------------|----|----|----|
    | ⚰️ | ```n & n+1 & (!n / !n+1)```                          | +2 | -2 | 0  |
    | 🎁 | ```2x n & !n```                                      | +1 | -1 | 0  |
    | 🦄 | ```n & n+2 & (n+4 / n+5)```</br> ```n & n+3 & n+5``` | +5 | -5 | -5 |
    | ☢️ | ```3x n```                                           | +3 | -3 | +3 |

    🏁

    | 🏁 | P1 👱           | P2 🧔          | P3 🧕           |
    |----|-----------------|----------------|-----------------|
    | 1  | 11 -> 11+0 = 11 | 0 -> 0+0 = 0   | 2 -> 2+0 = 2    |
    | 2  | 5  -> 5+11 = 16 | 6 -> 6+0 = 6   | 0 -> 0+2 = 2    |
    | 3  | 0  -> 0+16 = 16 | 8 -> 8+6 = 14  | 16 -> 16+2 = 18 |
    | 4  | 3 -> 3+16 = 19  | 2 -> 2+14 = 16 | 0 -> 0+18 = 18  |

    P1👱=19 > P3🧕=18 > P2🧔=16

    P1👱 = 🥇
