# Rules

Chessault is a chess variant in which figures can be purchased. Killing the enemy king ends the game. Points are earned for various actions that can be used to purchase figures and actions. There are abilities that enable special attack or protection moves for a given figure. Each player has 3 actions per turn and rolls dice to determine which figures can be moved.

## Chess board

The chessboard is that of a regular chess board (8x8) extend by a 1x8 field on each side for recruiting new figures.

There are additional zones:

- Recruitment zone
- Setup zone
- Spawn quarter
- Middle line

And there are fields with icons

- Explode
- Convert

![chessault_overview](_overview.drawio.svg)

## Game Setup

To start the game, each player receives:

- 2x pawns
- 1x king
- 1x queen
- 9 points

White starts the game and places a figure on the board in the setup zone.

Players then go turn by turn and can either place a figure or purchase a figure.

- In this phase all figures are placed directly in the first 2 lines of the playing field.
- Once placed, the king receives a protect ability.
- At the end of the setup all figures are placed. It is however not required to spend all points.
- If one player is done early the other player can finish all remaining actions at once.

## Actions

Once the game is setup, white starts that game. On every turn a player has 3 actions. There are 2 types of actions possible:

- Move a figure
- Purchase a figure

Once all three actions are done the player earns points from certain actions:

| Action                | Points  | Comment                                                                                                                                   |
|-----------------------|---------|-------------------------------------------------------------------------------------------------------------------------------------------|
| Figure moved          | +1       | If a figure moves to attack anonther figure but this figure has a protection ability this counts as move (but not as kill)                   |
| Converted figure      | +1       |                                                                                                                                           |
| Enemy killed          | +2       | If a figure with a protect ability is successfully attacked this does not account for "kill an enemy figure" and is not awareded with points |
| Reached enemy endzone | -1 / +1 | Steal 1 from your enemy. If your enemy has no points left you get nothing.                                                                |

These points can be spent in the next round.

### Move a Figure

Roll all 3 dice. The dice show which figures can be moved in this turn. If you can move a figure you must move it. If non of the rolled dice show a figure you can move this action is over.

A figure can only move once per turn.

If you move a figure that has an ability (explode or convert) you may use this ability after moving.

If you initially move a figure from the requirement line the figure must stay within the red-lined quarter.

In case your king is in check you can optionally move the king as an action once. In this case there is no need to roll the dice.

### Purchase Figures

The king can not be purchased. Any other figure can be purchased as described below. Purchasing a figure as an action includes choosing a figure, spending the points and playing it at any free space on the recruitment line.

| Figure   | Cost           | Comments |
|----------|----------------|-|
| Queen    | 7 + sacrifice* |The queen can be purchased like any other figure but requires a sacrifice. The sacrifice can be any own figure already in the game, except the king (duh!) and the pawn. The queen can also be purchased by bringing a pawn to the enemy end line. The pawn then converts into a queen (if still available). A player can have a maximum of 2 qeens in the game. If a queen (or any other figure) is killed and is no longer available for purchase/recruitment it can be resurected (see purchase actions).|
| Rook     | 5              ||
| Bishop   | 3              ||
| Knight   | 3              ||
| Pawn     | 1              ||
| Resurect | 2              |Any figure killed can be resurected. Once resurected can be purchased again (additional action). Resurecting figures doesn't revive them on the battle field nor does this directly put them in the requiruitment area. This is only to make them available for purchase.|

## Abilities

What are abilities?

- Abilities can be added to figures (except pawns) to enhance their attack or defense.
- There are three kinds of abilities: protect, explode, convert.
- Each abilities exists 3 times and each figure can only have one additional abilities assigned at a time. An exception is the protect ability which is available 5x but two protect are assigned during setup to the kings of each side. Once the king is attacked this protect ability can be re-used.

How to obtain abilities?

- The abilities "explode" and "convert" are picked up when accessing a given field on the board.
- The "protect" ability is rewarded when killing an enemy.
- If a player with an ability (explode or convert) is killed the ability is passed on to the killer figure.
- If there are no abilities left (all 3 are assinged) the figure does not gain the ability.

How to use abilities?

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

- If this figure does not move out of the radius in the next turn this figure is converted. The figure is removed (just like killed) and replaced by the same typ of figure of the other color. In case this figure is no longer the player may choose to resurect the figure at this point in time or else the figure simply is killed.
- If the figure manages to escape it may keep the convert ability,
- Every figure can be converted. If the king is converted the game is over.

Examples:

TODO
