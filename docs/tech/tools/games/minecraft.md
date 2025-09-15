# Minecraft

## Save Data

Save Data on Windows is located here:

```txt
%LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds
```

For Java Edition:

```txt
%APPDATA%\.minecraft\saves
```

## Technical Details

### World Generation

- **Seed**: 64-bit integer that determines world generation
- **Chunks**: 16x16 block sections, loaded/unloaded dynamically
- **World Height**: -64 to 320 blocks (1.18+), total height of 384 blocks
- **Bedrock Layer**: Y=-64 (bottom of world)
- **Build Limit**: Y=320 (top of world)

### Performance & Optimization

#### JVM Arguments for Java Edition

```bash
java -Xmx4G -Xms4G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1
```

#### Server Properties Optimization

```properties
# server.properties
view-distance=10
simulation-distance=10
max-tick-time=60000
spawn-protection=0
enable-command-block=false
enforce-whitelist=true
```

### NBT Data Format

Minecraft uses Named Binary Tag (NBT) format for data storage:

- **TAG_Byte**: Single signed byte
- **TAG_Short**: Signed 16-bit integer
- **TAG_Int**: Signed 32-bit integer
- **TAG_Long**: Signed 64-bit integer
- **TAG_Float**: IEEE 754 single precision
- **TAG_Double**: IEEE 754 double precision
- **TAG_String**: UTF-8 string
- **TAG_List**: List of unnamed tags
- **TAG_Compound**: List of named tags

### Redstone Engineering

#### Signal Strength

- **Power Level**: 0-15 (redstone dust weakens by 1 every block)
- **Maximum Range**: 15 blocks without repeater
- **Repeater Delay**: 1-4 redstone ticks (0.1-0.4 seconds)

#### Logic Gates

```txt
NOT Gate: Redstone torch + block
AND Gate: Two inputs into single output
OR Gate: Multiple inputs merged
XOR Gate: Combination of AND/OR/NOT gates
```

### Server Administration

#### Essential Commands

```bash
# Performance monitoring
/tps                    # Server TPS (20 = perfect)
/lag                    # Check server lag
/mspt                   # Milliseconds per tick

# World management
/gamerule randomTickSpeed 3    # Default tick speed
/gamerule doDaylightCycle false # Stop time
/weather clear 1000000         # Clear weather

# Backup
/save-all              # Force save all chunks
/save-off              # Disable auto-save
/save-on               # Enable auto-save
```

### Security

```properties
# Prevent griefing
spawn-protection=16
enable-command-block=false
broadcast-rcon-to-ops=false

# Performance protection
max-players=20
rate-limit=0
max-world-size=29999984
```

### Useful Tools

- **MCA Selector**: Edit region files directly
- **NBTExplorer**: View/edit NBT data
- **Chunky**: Pre-generate world chunks
- **WorldEdit**: In-game world editing
- **Litematica**: Schematic mod for building

## Creative Mode Cheat Codes

### Basic Cheats

```bash
# Game Mode Changes
/gamemode creative          # Switch to creative mode
/gamemode survival          # Switch to survival mode
/gamemode spectator         # Switch to spectator mode
/gamemode adventure         # Switch to adventure mode

# Time & Weather
/time set day               # Set time to day (1000)
/time set noon              # Set time to noon (6000)
/time set night             # Set time to night (13000)
/time set midnight          # Set time to midnight (18000)
/weather clear              # Clear weather
/weather rain               # Make it rain
/weather thunder            # Make it storm

# Player Management
/heal                       # Heal to full health
/feed                       # Fill hunger bar
/fly                        # Toggle flight mode
/god                        # Toggle god mode (invincibility)
/give @p minecraft:diamond 64    # Give 64 diamonds
/xp add @p 1000             # Add 1000 XP points

# World Manipulation
/fill ~-5 ~-1 ~-5 ~5 ~-1 ~5 minecraft:glass    # Create glass platform
/setblock ~ ~-1 ~ minecraft:bedrock             # Place bedrock below you
/clone 0 0 0 10 10 10 20 20 20                 # Copy area
/tp @p 0 100 0              # Teleport to coordinates
/tp @p ~ ~10 ~              # Teleport 10 blocks up
```

### Advanced Cheats

```bash
# Enchanted Items
/give @p minecraft:diamond_sword{Enchantments:[{id:"sharpness",lvl:32767}]}
/give @p minecraft:bow{Enchantments:[{id:"infinity",lvl:1},{id:"power",lvl:10}]}
/give @p minecraft:elytra{Enchantments:[{id:"unbreaking",lvl:10}]}

# Mob Spawning
/summon minecraft:zombie ~ ~ ~ {IsBaby:1b}      # Spawn baby zombie
/summon minecraft:horse ~ ~ ~ {Tame:1b}         # Spawn tamed horse
/summon minecraft:villager ~ ~ ~ {Profession:librarian}  # Spawn librarian

# World Generation
/locate structure minecraft:stronghold          # Find nearest stronghold
/locate biome minecraft:mushroom_fields         # Find mushroom island
/forceload add ~ ~                              # Keep chunk loaded
```

## Block Functions & Hidden Mechanics

### Fishing Mechanics

#### How to Fish Effectively

```txt
Requirements:
- Fishing rod
- Water source (1x1 minimum, 2 blocks deep optimal)
- Patience and timing

Technique:
1. Cast line into water (right-click)
2. Watch for bobber to go underwater
3. Listen for splash sound
4. Right-click immediately when bobber dips
5. Items will fly toward you
```

#### Fishing Loot Tables

- **Fish**: 85% chance (cod, salmon, tropical fish, pufferfish)
- **Treasure**: 5% chance (enchanted books, name tags, saddles, nautilus shells)
- **Junk**: 10% chance (leather boots, bowls, sticks, string)

#### Fishing Enchantments

- **Luck of the Sea**: Increases treasure chance
- **Lure**: Decreases time between catches
- **Unbreaking**: Increases rod durability

### Portal Creation

#### Nether Portal

```txt
Materials: 14 obsidian blocks (minimum 10)
Size: 4x5 frame (can be larger up to 23x23)
Activation: Flint and steel or fire charge

Construction:
1. Build rectangular frame of obsidian
2. Light the inside with flint and steel
3. Purple particles = active portal
```

#### End Portal

```txt
Materials: 12 Eyes of Ender
Location: Must find stronghold first
Process:
1. Find stronghold using Eyes of Ender
2. Locate portal room
3. Fill empty frame slots with Eyes of Ender
4. Portal activates automatically when complete
```

#### Portal between two coordinates

Give yourself a command block

```txt
/give @p command_block
```

Place the command block (behind or under your portal frame).

Enter this command

```txt
execute as @p[x=PORTALX,y=PORTALY,z=PORTALZ,distance=..2] run tp @s DESTX DESTY DESTZ
```

Adjust coordinates:

- PORTALX/Y/Z = coordinates of the portal
- DESTX/Y/Z = coordinates where you want to teleport

Set the command block

- Block Type: Repeat
- Condition: Always Active

Build a second portal the same way to teleport back

### Advanced Block Mechanics

#### Redstone Components

**Comparator Functions:**

- **Compare Mode**: Outputs signal strength comparison
- **Subtract Mode**: Subtracts side input from main input
- **Container Reading**: Outputs signal based on fullness

**Observer Block:**

- Detects block updates in front of it
- Outputs 1-tick pulse
- Can detect block state changes, not just placement

#### Water Mechanics

**Water Logging:**

- Stairs, slabs, fences can hold water
- Allows complex water features
- Prevents water flow while maintaining water block

**Bubble Columns:**

- **Soul Sand**: Creates upward bubble column (lifts entities)
- **Magma Block**: Creates downward bubble column (pulls entities down)
- Must have water source block above

#### Honey Block Properties

- **Sticky Movement**: Moves adjacent blocks when pushed
- **Slide Prevention**: Prevents fall damage and slows movement
- **Redstone Power**: Doesn't conduct redstone signals
- **Jump Reduction**: Reduces jump height by half

#### Scaffolding Mechanics

- **Dynamic Support**: Breaks if no horizontal support within 6 blocks
- **Climbing**: Can climb by looking up while moving
- **Bottom-up Breaking**: Breaks from bottom automatically
- **Side Placement**: Can be placed on sides of other scaffolding

### Hidden Block Interactions

#### Cauldron Uses

```txt
- Store water, lava, or powder snow
- Clean leather armor (removes dye)
- Fill bottles and buckets
- Extinguish fire on entities
- Clean banners (removes patterns)
- Clean shulker boxes (removes dye)
```

#### Composter Mechanics

```txt
Compostable Items (by percentage):
- 30%: Seeds, saplings, leaves
- 50%: Flowers, crops, cactus
- 65%: Baked potato, bread, cookies
- 85%: Hay bales, nether wart blocks
- 100%: Pumpkin pie, cake
```

#### Bell Functions

- **Raid Detection**: Highlights nearby raiders when rung
- **Villager Gathering**: Calls villagers to nearby area
- **Schedule**: Villagers gather at bells during certain times
- **Redstone**: Can be activated with redstone signal

#### Lectern Features

- **Book Storage**: Holds written books and book & quill
- **Page Reading**: Right-click to read, use scroll wheel for pages
- **Redstone Output**: Emits signal based on current page
- **Comparator Compatible**: Signal strength = page number

### Creative Building Tricks

#### Invisible Item Frames

```bash
/give @p minecraft:item_frame{EntityTag:{Invisible:1b}}
```

#### Custom Player Heads

```bash
/give @p minecraft:player_head{SkullOwner:"PlayerName"}
```

#### Barrier Blocks

```bash
/give @p minecraft:barrier    # Invisible, unbreakable blocks
```

#### Structure Blocks

```txt
Save Mode: Save structures to files
Load Mode: Load saved structures
Corner Mode: Mark structure boundaries
Data Mode: Function execution
```

### Mob Behavior Secrets

#### Villager Trading

- **Reputation System**: Affects prices (attack villagers = higher prices)
- **Gossip Mechanics**: Villagers share reputation information
- **Profession Blocks**: Remove to reset trades (if not traded with yet)
- **Time-of-Day**: Villagers restock twice per day

#### Wolf/Dog Mechanics

- **Healing**: Feed any meat to heal
- **Sitting**: Right-click to sit/stand
- **Teleporting**: Dogs teleport if >12 blocks away (except when sitting)
- **Pack Behavior**: Angry wolves call nearby wolves to help
