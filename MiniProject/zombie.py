#! /usr/bin/env python3 
import random
from colorist import Color
import time
from gameOver import gameOver

def deployInitialZombies(location):
    """
    Description:
        -   deploys 3 random zombies across the map
    Parameters:
        -   location: the building instance for the game map
    Return:
        -   None
    """
    for i in range (3):
        randomKey = random.choice(list(location.rooms.keys()))
        randomLocation = location.rooms[randomKey]['occupants']
        randomLocation.append('Zombie')


def deployZombie(location):
    """
    Description:
        -   deploys a single zombie across the map
    Parameters:
        -   location: the building instance for the game map
    Return:
        -   None
    """
    randomKey = random.choice(list(location.rooms.keys()))
    randomLocation = location.rooms[randomKey]['occupants']
    randomLocation.append('Zombie')


def zombieAttack(player, location):
    """
    Description:
        -   performs a single attack on the player
    Parameters:
        -   location: the building instance for the game map
        -   player: the player instance for the game map
    Return:
        -   None
    """
    zombieCount = len(location.rooms[player.getLocation()]['occupants'])
    if zombieCount > 0:
        for i in range(zombieCount):
            player.setHealth(player.getHealth() - random.randint(15,30))
            # player.health -= random.randint(15,30)
        if player.health >= 60:
            print(f"{Color.RED}The near by ZoMbIe attacked you... keep an eye on your health{Color.OFF}")
        elif player.health >= 40:
            print(f"{Color.RED}The near by ZoMbIe attacked you... your health is reaching critical low{Color.OFF}")
        elif player.health >= 16:
            print(f"{Color.RED}The near by ZoMbIe attacked you... your health is at CRITICAL LOW!!!{Color.OFF}")
        elif player.health >= 15:
            print(f"{Color.RED}The near by ZoMbIe attacked you... one more attack and you will most likely die!!!!{Color.OFF}")
        time.sleep(5)