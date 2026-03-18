# Snack Rider

Snack Rider is a small retro-style platform game made with **Python** and **Pygame**.  
The game uses a simple tile-based map, pixel-art sprites, traps, enemies, food pickups, and health items.

<img width="772" height="404" alt="obrazek" src="https://github.com/user-attachments/assets/646faa25-0e9a-4ff3-821d-fa8f41910f7b" />

## Features

- Retro pixel-art look
- Tile-based map system
- Animated enemies
- Food collection
- Health pickups
- Traps such as blades and water
- Simple room scrolling

## Controls

- **Left Arrow** – move left
- **Right Arrow** – move right
- **Up Arrow** or **Space** – jump
- **Escape** – exit the game

## Requirements

- Python 3
- Pygame

## Install Pygame with:

```bash
pip install pygame
```

## Run the Game

Start the game with:

``` bash
python main.py
```

## Make sure these files are in the project:

-   `main.py`
-   `pictures.py`
-   `map.py`

------------------------------------------------------------------------

## Project Structure

### `main.py`

Contains the main game loop, movement, collision detection, rendering,
enemy logic, HUD, and room scrolling.

### `pictures.py`

All pixel-art graphics are defined here.

You can edit:

-   hero sprites
-   monsters
-   food
-   traps
-   icons
-   health items
-   environment tiles

Example sprite definitions in `pictures.py`:

-   `new_monster1`
-   `new_monster2`
-   `new_hero_right`
-   `new_hero_left`
-   `new_food`
-   `new_heart_ico`

------------------------------------------------------------------------

### `map.py`

The game map is created here.

The map is stored as a list of strings, where each character represents
one tile or object in the level.

Example:

``` python
mapa = [
    "#############################################################################################",
    "#       #     P #               #            #             P              #                 #",
    "#       #                                    #       P  F      P          #                 #",
]
```

------------------------------------------------------------------------

## Map Symbols

Each character in `map.py` has a meaning:

-   `#` = wall / stone block
-   `F` = food pickup
-   `L` = health pickup
-   `H` = blade trap
-   `V` = water
-   `M` = monster type 1
-   `P` = monster type 2
-   `` = empty space

------------------------------------------------------------------------

## Editing Graphics

Sprites in `pictures.py` are built from text characters.\
Each line represents one row of pixels.

Example:

``` python
new_monster1 = [
    '  3 3  2',
    '  212  2',
    '11111112',
    '   1   2',
    ' 11111 2',
    ' 1   33 ',
    '33      '
]
```

------------------------------------------------------------------------

## Color Meaning

-   `1` = primary sprite color (`color_p`)
-   `2` = yellow
-   `3` = brown
-   `4` = red
-   `5` = orange
-   `6` = blue
-   `7` = white
-   `8` = green
-   anything else = black

------------------------------------------------------------------------

## Example Game Objects

### Monsters

-   `new_monster1`
-   `new_monster2`

Animation:

-   `new_monster1_mov`
-   `new_monster2_mov`

------------------------------------------------------------------------

### Hero

-   `new_hero_right`
-   `new_hero_left`
-   `new_hero_up`
-   `new_hero_down`
-   `new_hero_death`

------------------------------------------------------------------------

### Other Objects

-   `new_food`
-   `new_food_ico`
-   `new_health`
-   `new_blade`
-   `new_blade_mov`
-   `new_water`
-   `new_stone`
-   `new_heart_ico`

------------------------------------------------------------------------

## Notes

-   Graphics are made directly in Python using arrays of strings.
-   The map is also fully editable in Python.

Good for learning:

-   Pygame basics
-   2D collisions
-   tile maps
-   sprite animation
-   retro game design


This project is open-source.

