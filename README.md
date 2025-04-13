# Alien Invasion Game

A Python game created by ELYES using Pygame where players control a ship to shoot down invading aliens.

## About
This game is a classic space shooter where you control a spaceship to defend against an alien invasion. The game features:
- Smooth ship movement
- Alien fleet formation
- Score tracking
- Level progression
- High score system

## Copyright Notice
© 2024 ELYES. All rights reserved.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Installation
1. Make sure you have Python installed
2. Install the required packages:
   ```
   pip install pygame
   ```
3. Run the game:
   ```
   python alien_invasion.py
   ```

## Controls
- Left/Right Arrow Keys: Move ship
- Spacebar: Shoot
- Q: Quit game

## Credits
Created and developed by ELYES

![alt text](screenshots/alien_invasion.jpg "Alien Invasion")

## Add Pygame package when using PyCharm

The Alien Invasion game requires the Pygame package to be installed.
If it is missing, PyCharm will show the following error:

![alt text](screenshots/missing_pygame_package.jpg "Missing Pygame package")

To add the package for the Alien Invasion game, move the cursor to *import pygame* and press *Alt-enter*. The following popup menu should be shown:

![alt text](screenshots/install_pygame_package.jpg "Install Pygame package")

To install the Pygame package, select *Install package pygame*. This only works when using a correctly configured virtual environment.

## Installing Pygame

To install Pygame for the current user, enter the following command at a terminal prompt:

```
$ python -m pip install --user pygame
```

To install Pygame globally on Debian based systems, do:

```
# apt-get install python3-pygame
```

# Quitting the game

The alien invasion game will start in fullscreen mode. To exit the game, type 'q'
