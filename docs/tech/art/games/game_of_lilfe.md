# Game of life

## FFMPEG

This FFmpeg filter generates a life-like grid pattern based on a generalization of John Conway’s Game of Life. Each pixel in the output video represents a cell, which can be either alive or dead, and cells evolve according to a user-defined rule. The rule determines how many alive neighbors a cell needs to survive or be born.

[Details here](https://ffmpeg.org/ffmpeg-filters.html#life)

By configuring these parameters, you can create visually dynamic patterns that evolve frame by frame, producing a captivating visualization within your video:

- filename (-f): Specifies a file with the initial grid state, where any non-whitespace character marks an alive cell. If no file is provided, the grid is randomly generated.
- rate (-r): Sets the frame rate of the output video. Default is 25 fps.
- size (-s): Defines the resolution of the output video. If a file is used, the size defaults to the file’s dimensions; otherwise, it defaults to 320x240.
- random_fill_ratio, random_seed: Adjust how the random initial grid is generated.
- rule: Lets you specify custom survival and birth conditions, either in a textual format (e.g., S23/B3) or as an integer.
- life_color, death_color, mold_color: Control the appearance of living, dead, and “moldy” cells.
- stitch, mold: Add visual or logical effects, such as wrapping grid edges or creating a mold effect for dead cells.

Example:

Simple version:

```sh
ffmpeg -f lavfi -i life=size=640x480:rate=30 -frames:v 300 _ffmpeg_game_of_life1.mp4
```

Using colors:

```sh
ffmpeg -f lavfi -i "life=s=960x540:mold=10:r=60:ratio=0.1:death_color=#C83232:life_color=#00ff00,scale=960:540:flags=16" -c:v libx264 -crf 41 -frames:v 1800 -r 60 -t 30 _ffmpeg_game_of_life2.mp4
```

The grid represents a two-dimensional layout of cells that evolve over time based on a rule set. It’s essentially a canvas where each cell interacts with its neighbors, following rules to determine whether it stays alive, dies, or is born. Over time, the grid’s pattern changes, creating a dynamic and visually interesting effect.

Use this example

```sh
ffmpeg -f lavfi -i life=f=somekindof.grid:size=640x480:rate=30:random_fill_ratio=0.3:random_seed=123:rule=S34/B23:stitch=0:life_color=0xff0000:death_color=0x000000:mold_color=0x777777:mold=1 -frames:v 300 _ffmpeg_game_of_life3.mp4
```

With these example grids:

Example 1: [Glider](_ffmpeg_gol_grid_glider.grid)

```txt
.O.
..O
OOO
```

Example 2: [Small Exploder](_ffmpeg_gol_grid_exploder.grid)

```txt
.O.
.OO
O.O
```

Example 3: [Oscillator](_ffmpeg_gol_grid_oscillator.grid)

```txt
OOO
...
...

Example 4: [Random](_ffmpeg_gol_grid_random.grid)

```txt
O.OO.O
.O.O..
..OO.O
```

Example 5: [Square Block](_ffmpeg_gol_grid_square.grid)

```txt
OO
OO
```

Example 6: [x](_ffmpeg_gol_grid_x.grid)

```txt
XX  XX
  XX  
 XX XX
```

Examples can bee seen here:

<iframe width="560" height="315" src="https://youtu.be/_iM5B3cQudU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
