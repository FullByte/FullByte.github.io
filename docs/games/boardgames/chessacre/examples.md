# Examples

## Explode

Once activated, the explosion will kill all figures (own and enemy) within the radius. Exception are figures with the protect ability. These figures will loose their protect ability.

![Explode_Killzone](_example_explode1.drawio.svg)

The player with the explosion ability can use the explosion optionally after moving. In this case all figures are hit within the radius. In this example 3 figures would be killed (black pawn, black knight, white pawn). The attacking player doesn't recieve a protection ability for this attack but recives 2x2 credits (2 credits for each enemy kill) once the turn is over.

![Explode_Killzone](_example_explode2.drawio.svg)

Although figures can not attack the recruitment area, an explosion will kill all figures in range including the recruitment area. In this exmaple the white queen kills the recruited black bishop as well as the two black pawns within range. The attacking queen doesn't recieve a protection ability for this attack but the player recives 3x2 credits (2 credits for each enemy kill) once the turn is over.

## Convert

Once activated an enemy figure within the radius must be chosen. This figure will recieve the convert ability. If this figure does not move out of the radius in the next turn this figure is converted. The figure is then killed and replaced by the same typ of figure of the other color from the recruitment area. In case this figure is not available the figure is killed without replacement. If the figure manages to escape it may keep the convert ability. Enemys with the protect ability can not be converted. If the king has no protection and is converted the game is over. If the king is attacked with conversion the king is in check and the special moving rules apply.

TODO Examples!

![example_convert](_example_convert1.drawio.svg)

![example_convert](_example_convert2.drawio.svg)

## Protect

If a figure kills another figure it earns the protect ability. This figure now requires 2 hits to get killed. 2 protect abilities are assigned during setup to the kings of each side. Once the king is attacked and the protect ability is lost this protect ability can be re-used.

TODO Examples!

![example_protect](_example_protect1.drawio.svg)

![example_protect](_example_protect2.drawio.svg)
