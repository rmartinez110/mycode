#! /usr/bin/env python3 
import random
import time

# select a random weapon to generate
def getRandomWeapon():
        """
        Description:
                -       Randomly gets a weapon from the weapons dictionary   
        Parameters:
                -       None
        Return:
                -       None    
        """
        weapons = {"axe": {"name": "axe", "damage": 30, "durability" : 2}, 
                   "hammer": {"name": "hammer", "damage": 20, "durability" : 1}, 
                   "chainsaw": {"name": "chainsaw", "damage": 60, "durability" : 3}, 
                   "kitchen knife": {"name": "kitchen knife", "damage": 25, "durability" : 1}, 
                   "combat knife": {"name": "combat knife", "damage": 35, "durability" : 2}, 
                   "torch": {"name": "torch", "damage": 40, "durability" : 1}, 
                   "grenade": {"name": "grenade", "damage": 35, "durability" : 1}, 
                   "pistol": {"name": "pistol", "damage": 60, "durability" : 3}, 
                   "pipe": {"name": "pipe", "damage": 15, "durability" : 2}, 
                   "saw": {"name": "saw", "damage": 70, "durability" : 1}, 
                   "sword": {"name": "sword", "damage": 50, "durability" : 2}}

        randomKey = random.choice(list(weapons.keys()))
        randomWeapon = weapons[randomKey]

        newWeapon = [randomWeapon['name'], randomWeapon['damage'], randomWeapon['durability']]

        return newWeapon


def deployWeapon(location):
        """
        Description:
                -       deploys a random weapon to a random location   
        Parameters:
                -       location: the building instance for the game
        Return:
                -       None    
        """
        randomKey = random.choice(list(location.rooms.keys()))
        randomRoom = location.rooms[randomKey]

        newRandomWeapon = getRandomWeapon()
        randomRoom['inventory'][newRandomWeapon[0]] = {"damage": newRandomWeapon[1], "durability" : newRandomWeapon[2]}