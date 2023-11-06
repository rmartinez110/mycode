#! /usr/bin/env python3 
import random
from weapon import getRandomWeapon

class Building:
    """
    Author:
        -   Robert Martinez
        
    Description:
        -   The building class creates a collection of rooms that are used to create the game map

    Parameters:
        -   rooms
        -   key
        
    Returns:
        -   Constructor returns a building instance of an object

    Version:
        -   1.0
        
    Date:
        -   20231103
        
    Change Log:
        -   Initial Creation: Robert Martinez/20231103
    """

    def __init__(self):
        """
        Description:
            -   Constructor that creates an instance of the building object
        
        Parameters:
            -   rooms: a dictionary with all the rooms in the building
            -   key: boolean to determine if the key has been deployed to the game map
            
        Returns:
            -   Constructor returns a building instance of an object
        """
        self.rooms = {
            "livingroom": {"name": "Livingroom", "inventory": {}, "occupants": [], "exit": "back door", "traversable": ["hall", "kitchen"]},
            "kitchen": {"name": "Kitchen", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["livingroom", "hall"]},
            "hall": {"name": "Hall", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["kitchen", "livingroom", "restroom1", "office", "garage", "stairs"]},
            "office": {"name": "Office", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["hall"]},
            "restroom1" : {"name": "Restroom 1", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["hall"]},
            "garage": {"name": "Garage", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["hall"]},
            "gameroom": {"name": "Gameroom", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["bedroom1", "bedroom2", "masterbedroom", "restroom2", "stairs"]},
            "bedroom1": {"name": "Bedroom 1", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["gameroom"]},
            "bedroom2": {"name": "Bedroom 2", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["gameroom"]},
            "masterbedroom": {"name": "Master Bedroom", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["gameroom"]},
            "restroom2": {"name": "Restroom 2", "inventory": {}, "occupants": [], "exit": "none", "traversable": ["gameroom"]}}
        self.key = False

    # add inventory to the desired location
    def addInventory(self, item):
        """
        Description:
            -   Adds an item to the inventory of the desired location
        
        Parameters:
            -   item: the item to be added to the inventory
            
        Returns:
            -   Returns the inventory of the desired location after adding the item to it
        """
        self.inventory.append(item)
        return self.inventory
    
    # get the inventory of the desired location
    def getInventory(self):
        """
        Description:
            -   Returns the inventory of the desired location
        
        Parameters:
            -   None
            
        Returns:
            -   Returns the inventory of the desired location
        """
        return self.inventory
    
    # get occupants of the desired location
    def getOccupants(self):
        """
        Description:
            -   Returns the occupants of the desired location
        
        Parameters:
            -   None
            
        Returns:
            -   Returns the occupants of the desired location
        """
        return self.occupants
    
    def removeInventory(self, item, location):
        """
        Description:
            -   Removes an item from the inventory of the desired location
        
        Parameters:
            -   item: the item to be removed from the inventory
            -   location: the location of the item to be removed from the inventory
            
        Returns:
            -   Returns the inventory of the desired location after removing the item from it
        """
        self.rooms[location]['inventory'].remove(item)
        return self.inventory
    
    # get key status
    def getKey(self):
        """
        Description:
            -   Returns the key status
        
        Parameters:
            -   None
            
        Returns:
            -   Returns the key status
        """
        return self.key
    
    # set key status
    def setKey(self, key):
        """
        Description:
            -   Sets the key status
        
        Parameters:
            -   key: the key status to be set
            
        Returns:
            -   Returns the key status
        """
        self.key = key
        return self.key
    
    def initialLoadOut(self):
        """
        Description:
            -   Adds initial load out to the rooms
        
        Parameters:
            -   None
            
        Returns:
            -   Returns the initial loadout to the rooms
        
        """
        for i in range(8):
            randomKey = random.choice(list(self.rooms.keys()))
            randomRoom = self.rooms[randomKey]

            newRandomWeapon = getRandomWeapon()

            randomRoom['inventory'][newRandomWeapon[0]] = {
                "damage": newRandomWeapon[1], "durability": newRandomWeapon[2] }