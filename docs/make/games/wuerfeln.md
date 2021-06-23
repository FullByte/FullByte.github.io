# Würfeln

```Würfeln ist Einstellungssache``` is a game of luck and high precision dice rolling. Tweak statistics to your advantage with the right mindset. Is your dice roll determination stronger than the one of your opponents? Play a game, bet on your roll attempts and show that you have mastered the art of rolling the die.

## How to play

### Setup

Challenge up to three opponents, three standard D6 dice (numbers 1-6) per player (idealy visually different), an einhorn and plenty of smooth rocks.

The poor mans option that works is any object that will resemble the einhorn and something to keep track of the score e.g. rocks, coins, etc. Pen and paper works but is a little more work and kills the flow.

Everyone starts with 6 rocks (=points). Roll all three die and the player with highest total number starts the game.

### Play

The current player decides to either predict the upcoming roll or not (passive roll) - then rolls all three dice once.

Based on the result add/remove points as follows:

| Result                | Rule / Dice combination                                                      | Correct | Wrong | Passive |
|-----------------------|------------------------------------------------------------------------------|---------|-------|---------|
| ⚰️ Das Unvermeidliche | ```n & n+1 & (!n / !n+1)```</br>Example: ⚀⚁⚃ or ⚂⚃⚀                          | +2      | -2    | -1      |
| 🎁 Wunsch             | ```2x n & !n```</br>Example: ⚀⚀⚁                                             | +1      | -1    | 0       |
| 🦄 Einhorn            | ```n & n+2 & (n+4 / n+5)```</br> ```n & n+3 & n+5```</br>Example: ⚀⚂⚄ or ⚀⚃⚅ | +5      | -5    | -5      |
| ☢️ Dreifaltigkeit     | ```3x n```</br>Example: ⚁⚁⚁ or ⚅⚅⚅                                           | +3      | -3    | +3      |

### Example round

If it is your turn, you bet on rolling 🎁(Wunsch) and you rolled 1,2,5 which is ⚰️(Das Unvermeidliche). Therefore, you lose 2 points. If this is the first round of the game, you started with 6 points and now have 4 points. Now it is the next players turn. The player choses to not predict anything and roll a 2,2,2 which is ☢️(Dreifaltigkeit). In this case the player gains 3 points and it is the next players turn. The third player predicts an 🦄(Einhorn) and roll a 1,3,6 and gains 5 points. (this never happens IRL, lol :D)

### 🦄 Einhorn

In case a player rolls an 🦄(Einhorn) the player then recieves the Einhorn. It doesn't matter if the prediction was correct, wrong or passiv. From this moment on the player may choose from where to take and give points: either the main rock stash from any other player. If the player with the Einhorn needs to give rocks back, those are given to any other player of choice. The 🦄(Einhorn) is passed once another player roles an 🦄(Einhorn) and returned once the round ends.

### How to win

The first player to reach 0 points (or less) loses the game. The game ends at this point and the player with the most points wins the game.

### Multiple games

Should you play multiple games note down all remaining points from the current game and add them to the total score.

Agree on how many games shall be played and after that game the player with the highest overall score wins.

On every new round you start again with 6 points but can add already gained points from previous matches into this game if you like. You can add your entire point stach if you want.

You do not keep the 🦄(Einhorn) over multiple games. After each game is over the 🦄(Einhorn) returns to the middle of the table and is called once an 🦄(Einhorn) is rolled.

The looser of the last round begins the new game.

### Multiple games example

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

    You can copy ```(6+3-1)!/(3!*(6-1)!)``` to wolframalpha to calculate it or use [this link](https://www.wolframalpha.com/input/?i=%286%2B3-1%29%21%2F%283%21*%286-1%29%21%29).

    These 56 combinations distribute as follows:

    | Result                |                                                                                                                                                                     | Amount | Percent |
    |-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|---------|
    | ⚰️ Das Unvermeidliche | ⚀⚁⚃, ⚀⚁⚄, ⚀⚁⚅, ⚁⚂⚀ </br> ⚁⚂⚄, ⚁⚂⚅, ⚂⚃⚀, ⚂⚃⚁</br>⚂⚃⚅, ⚃⚄⚀, ⚃⚄⚁, ⚃⚄⚂, </br> ⚄⚅⚀, ⚄⚅⚁, ⚄⚅⚂, ⚄⚅⚃                                                                        | 16     | 29 %    |
    | 🎁 Wunsch             | ⚀⚀⚁, ⚀⚀⚂, ⚀⚀⚃, ⚀⚀⚄, ⚀⚀⚅</br>⚁⚁⚀, ⚁⚁⚂, ⚁⚁⚃, ⚁⚁⚄, ⚁⚁⚅</br>⚂⚂⚀, ⚂⚂⚁, ⚂⚂⚃, ⚂⚂⚄, ⚂⚂⚅</br>⚃⚃⚀, ⚃⚃⚁, ⚃⚃⚂, ⚃⚃⚄, ⚃⚃⚅</br>⚄⚄⚀, ⚄⚄⚁, ⚄⚄⚂, ⚄⚄⚃, ⚄⚄⚅</br>⚅⚅⚀, ⚅⚅⚁, ⚅⚅⚂, ⚅⚅⚃, ⚅⚅⚄ | 30     | 54 %    |
    | 🦄 Einhorn            | ⚀⚂⚄, ⚀⚂⚅, ⚀⚃⚅, ⚁⚃⚅                                                                                                                                                  | 4      | 7 %     |
    | ☢️ Dreifaltigkeit     | ⚀⚀⚀, ⚁⚁⚁, ⚂⚂⚂</br>⚃⚃⚃, ⚄⚄⚄, ⚅⚅⚅                                                                                                                                     | 6      | 11 %    |

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
