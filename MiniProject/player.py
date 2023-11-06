from colorist import Color
import time
from zombie import zombieAttack

class Player():
    """
    Author:
        -   Robert Martinez
        
    Description:
        -   This class creates an instance of the player object.

    Parameters:
        -   None
        
    Returns:
        -   Constructor returns a player instance of an object

    Version:
        -   1.0
        
    Date:
        -   20231103
        
    Change Log:
        -   Initial Creation: Robert Martinez/20231103
    """
    def __init__(self, name):
        """
        Description:
            -   Player constructor that creates an instance of the player object
        Parameters:
            -   name: name of the place
            -   health: health of the player
            -   stamina: stamina of the player
            -   inventory: inventory of the player
            -   location: location of the player
            -   kills: number of kills of the player
        Returns:
        """
        self.name = name
        self.health = 100
        self.stamina = 100
        self.inventory = {}
        self.location = "hall"
        self.kills = 0

    # travers locations around the map
    def traversLocations(self, newLocation, location):
        """
        Description:
            -   traversLocations traverses locations around the map
        Parameters:
            -   newLocation: new location of the player
            -   location: location of the player
        Returns:
            -   traversLocations returns the new location of the player
        """
        # send the play to the game room or the hall depending where they are when they enter the stairs
        if(newLocation == "stairs" and self.location == "gameroom" ):
            zombieAttack(self, location)
            self.location = "hall"
        elif(newLocation == "stairs" and self.location == "hall" ):
            zombieAttack(self, location)
            self.location = "gameroom"
        elif (newLocation in location.rooms[self.location]['traversable']):
            zombieAttack(self, location)
            self.location = newLocation
        else:
            print(f"{Color.RED}Location is not traversable ... check the list in the menu {Color.OFF}")
            time.sleep(3)

    # attack a zombie
    def attack(self, location, weaponName):
        """
        Description:
            -   attack attacks a zombie
        Parameters:
            -   location: location of the player
            -   weaponName: weapon name of the player
        Returns:
            -   attack returns the new location of the player
        """
        if location.rooms[self.location]['occupants'] == []:
            print(f"{Color.RED}There is no one to attack here...{Color.OFF}")
            time.sleep(3)
        else:
            if weaponName in self.inventory:
                print(f"{Color.BLUE}{self.name} is attacking a zombie in the {self.location} with a {weaponName}!!")
                time.sleep(2)
                if weaponName == "grenade":
                    self.kills += len(location.rooms[self.location]['occupants'])
                    location.rooms[self.location]['occupants'].clear()
                    print(f"{Color.RED}All Zombies in the room have been killed with the {weaponName}!{Color.OFF}")
                    self.inventory[weaponName]['durability'] -= 1
                    if self.inventory[weaponName]['durability'] == 0:
                        del self.inventory[weaponName]
                        print(f"{Color.RED}The {weaponName} has been destroyed!{Color.OFF}")
                    time.sleep(3)
                else:
                    location.rooms[self.location]['occupants'].pop()
                    print(f"The zombie has been killed!")
                    self.kills += 1
                    time.sleep(3)
                    self.inventory[weaponName]['durability'] -= 1
                    if self.inventory[weaponName]['durability'] == 0:
                        del self.inventory[weaponName]
                        print(f"{Color.RED}The {weaponName} has been destroyed!{Color.OFF}")
                        time.sleep(3)
                zombieAttack(self, location)
            else:
                print(f"{Color.RED}You don't have a {weaponName} to attack with...{Color.OFF}")
                time.sleep(3)

    # get the player's inventory
    def getInventory(self):
        """
        Description:
            -   getInventory gets the player's inventory
        Parameters:
            -   None
        Returns:
            -   getInventory returns the player's inventory
        """
        return self.inventory

    # get the player's location
    def getLocation(self):
        """
        Description:
            -   getLocation gets the player's location
        Parameters:
            -   None
        Returns:
            -   getLocation returns the player's location
        """
        return self.location
    
    # get player name
    def getName(self):
        """
        Description:
            -   getName gets the player's name
        Parameters:
            -   None
        Returns:
            -   getName returns the player's name
        """
        return self.name
    
    # get player kills
    def getKills(self):
        """
        Description:
            -   getKills gets the player's kills
        Parameters:
            -   None
        Returns:
            -   getKills returns the player's kills
        """
        return self.kills
    
    # get players health
    def getHealth(self):
        """
        Description:
            -   getHealth gets the player's health
        Parameters:
            -   None
        Returns:
            -   getHealth returns the player's health
        """
        return self.health
    
    # change players health
    def setHealth(self, health):
        """
        Description:
            -   changeHealth changes the player's health
        Parameters:
            -   health: health of the player
        Returns:
            -   changeHealth returns the player's health
        """
        self.health = health
        
    # pickup an item from a room
    def pickupItem(self, item, location):
        """
        Description:
            -   pickupItem picks up an item from a room
        Parameters:
            -   item: item to be picked up
            -   location: location of the player
        Returns:
            -   pickupItem returns the player's inventory and the room's inventory
        
        """
        try:
            self.inventory[item] = location.rooms[self.location]['inventory'][item]
            del location.rooms[self.location]['inventory'][item]
        except:
            print(f"{Color.RED}There is no {item} in this room...{Color.OFF}")
            time.sleep(3)

    # drop an item from the player's inventory
    def dropItem(self, item, location):
        """
        Description:
            -   dropItem drops an item from the player's inventory
        Parameters:
            -   item: item to be dropped
            -   location: location of the player
        Returns:
            -   dropItem returns the player's inventory and the room's inventory
        """
        try:
            print(f"{self.name} is dropping {item}")
            location.rooms[self.location]['inventory'][item] = self.inventory[item]
            del self.inventory[item]
        except:
            print(f"{Color.RED}You don't have {item} to drop...{Color.OFF}")
            time.sleep(3)
        zombieAttack(self, location)