# Rules

Chessault is a chess variant in which figures have abilities and new figures can be recruited for credits earned during the game. Each turn a player has 3 actions and can recruit or move figures. To move figures the player must roll three dice to determine which figures can be moved, then select one of the available options. Recruited figures start at the end of each board and come into play when first moved. Killing an enemy enables the protect ability. The explosion and convert abilities are picked up on the marked places on the board. credits are earned for various actions that can be used to recruit new figures. Killing the enemy king ends the game.

## Chess board

The chess board is that of a regular chess board (8x8) extend by a 1x8 field on each side for recruiting new figures.

There are additional zones:

- Recruitment zone
- Setup zone
- Spawn quarter
- Middle line

Addtionally there are spcial fields accross the board:

- Explode
- Convert

Figures are either active on the board, in the recruitment area, recuitable or dead:

- **Active figures** can move freely across the board acording to their abilities
- Figures in the **recruitment area** must move on the board within their board quarter.
- **Recuitable figures** can be recruited as an action if you have enough credits
- **Dead figures** can be resurected as an action. Otherwise these figures can no longer be used.

![chessault_overview](_overview.drawio.svg)

## Setup

To start the game, each player receives:

- 2x pawns
- 1x king
- 1x queen
- 9 credits

White starts the game and places a figure on the board in the setup zone.

Players then go turn by turn and can either place a figure or purchase a figure.

- In this phase all figures are placed directly in the setup zone (first 2 lines of the playing field).
- Once placed, the king receives a protect ability.

The setup ends once both players have placed all figures and do not want recruit any further figures. It not required to spend all credits. If one player is done early the other player can finish all remaining actions at once.

Once setup is done white starts with the first regular turn:

## Actions

On every turn a player has 3 actions.

There are 2 types of actions possible:

- Move
- Recruit

Once all three actions are done the player earns credits from certain actions:

| Action                | credits  | Comment                                                                                                                                                                                   |
|-----------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Figure moved          | +1      | For each figure moved 1 credit is awareded. If a figure moves to attack another figure but this figure has a protection ability this counts as move (but not as kill)                      |
| Converted figure      | +1      | A converted ememy is awarded with 1 credit. credits are rewareded after the turn in which the enemy was converted; not in the turn the conversion started.                                  |
| Conversion failed     | -1 / +1 | If the enemy successfully escapes from the conversion the enmy gains 1 credit and the player initiating the conversino looses 1 credit.                                                     |
| Enemy killed          | +2      | Each enemy killed is rewarded with 2 credits. If a figure with a protect ability is successfully attacked this does not account for `enemy killed` and is not awareded with credits |
| Reached enemy endzone | -1 / +1 | Steal 1 from your enemy. If your enemy has no credits left you get nothing.                                                                                                                |

credits earned at the end of turn can be spent in the next turn.

### Move

Roll all 3 dice. The dice show which figures can be moved in this turn.

- If you can move a figure you must move it.
- If non of the rolled dice show a figure you can move this action is over.

A figure can only move once per turn.

- Figures move just like in regular chess across the 8x8 board.
- If you move a figure that has an ability (explode or convert) you may use this ability after moving.
- If you initially move a figure from the recruitment line the figure must stay within the red-lined quarter.

In case your king is in check you can optionally move the king as an action once.

- In this case there is no need to roll the dice.
- If you moved the king in a prior action through a dice roll you may move the king again.

### Recruit

The king can not be recruited. Any other figure can be recruited as described below:

| Figure   | Cost           | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|----------|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Queen    | 7 + sacrifice* | The queen can be purchased like any other figure but requires a sacrifice. The sacrifice can be any own figure already in the game, except the king (duh!) and the pawn. The queen can also be purchased by bringing a pawn to the enemy end line. The pawn then converts into a queen (if still available). A player can have a maximum of 2 qeens in the game. If a queen (or any other figure) is killed and is no longer available for purchase/recruitment it can be resurected (see purchase actions). |
| Rook     | 5              | When leaving the recruitment line must stay within their spawn quarter. The figure may attack enemy figures within this range directly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Bishop   | 3              | When leaving the recruitment line must stay within their spawn quarter. The figure may attack enemy figures within this range directly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Knight   | 3              | When leaving the recruitment line must stay within their spawn quarter. The figure may attack enemy figures within this range directly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Pawn     | 1              | Pawns can move 2 fields once when leaving the recruitment line.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Resurect | 2              | Any figure killed can be resurected. Once resurected this figure can be purchased again (additional action). Resurecting figures doesn't revive them on the battle field nor does this directly put them in the requiruitment area. This is only to make them available for purchase. Resurecting a figure is an action by itself. To recruit a killed figure 2 actions are required. |

Recruiting a figure as an action includes:

- Choosing a figure
- Spending the credits
- Placing the figure at any free space on the recruitment line

## Abilities

Abilities can be added to figures (except pawns) to enhance their attack or defense.

There are three kinds of abilities:

- Protect
- Explode
- Convert

Each abilities exists 3 times and each figure can only have one additional abilities assigned at a time. An exception is the protect ability which is available 5x, however 2 protect abilities are assigned during setup to the kings of each side. Once the king is attacked and the protect ability is lost this protect ability can be re-used.

Obtain abilities:

- The abilities `explode` and `convert` are picked up when accessing a given field on the board.
- The `protect` ability is rewarded when killing an enemy.
- If a player with an ability (`explode` or `convert`) is killed the ability is passed on to the killer figure.
- If a player already has an ability they may choose which one to keep.
- If there are no abilities left (all 3 are assinged) the figure does not gain the ability.

Use abilities:

- Abilities can be activated if the figure was moved. Activating an ability is not an extra action.

### Protect

If a figure kills another figure it earns the protect ability. This figure now requires 2 hits to get killed.

If a figure attacks a figure with the protect ability the figure can not stay where it moved since the figure is not killed. The figure will stay where it started.

Examples:

TODO

### Explode

Once activated this will kill all figures (own and enemy) within the radius.

Exception are figures with the protect ability. These figures will simply loose their protect ability.

Examples:

![Explode_Killzone](_killzone1.drawio.svg)

The player with the explosion ability can use the explosion optionally after moving. In this case all figures are hit within the radius.

![Explode_Killzone](_killzone2.drawio.svg)

Although figures can not attack the recruitment area, an explosion will kill all figures in range including the recruitment area.

### Convert

Once activated an enemy figure within the radius must be chosen. This figure will recieve the convert ability.

- If this figure does not move out of the radius in the next turn this figure is converted. The figure is removed (just like killed) and replaced by the same typ of figure of the other color. In case this figure is no longer the player may choose to resurect the figure at this credit in time or else the figure simply is killed.
- If the figure manages to escape it may keep the convert ability,
- Every figure can be converted. If the king is converted the game is over.

Examples:

TODO
