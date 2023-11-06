#! /usr/bin/env python3
from colorist import Color
import time
import os
import threading
import title
from player import Player
from building import Building
from weapon import getRandomWeapon
from maps import maps
from gameTable import gameTable
from zombie import deployInitialZombies
from zombie import deployZombie
from weapon import deployWeapon
from exitKey import deployKey
from gameCredits import gameCredits
from gameOver import gameOver

# main class that creates the player and map
class Main:
    """
    Author:
        -   Robert Martinez
    
    Class Description: 
        -   This class is the main class the create the 'player', 'building layout', and controls the overall loop of the game till the 
            player either wins or loses and the game thread is killed.
    """

    # constructor
    def __init__(self, playerName):
        """
        The game constructor that uses composition
        The game HAS-A player object instance and HAS-A building object instance
        """
        self.player = Player(playerName)
        self.building  = Building()
        self.endGame = False

#########################################################################################
#########################################################################################
#########################################################################################

# display the title
# title.title()
playerName = input("What is your player's name? ")
game = Main(playerName)
creditsClock = 0
gameClock = 0

#########################################################################################
#########################################################################################
#########################################################################################

# start the game
def startGame():
    # start the game timer
    gameStatus = threading.Thread(target=gameTimer)
    gameStatus.start()
    # clear the screen of any commands/output
    os.system('clear')

    # deploy the initial zombies and weapon load outs
    game.building.initialLoadOut()
    deployInitialZombies(game.building)

    # game loop
    while gameStatus.is_alive():

        # display the cli UI
        cliUI()
        print(f"{Color.BLUE}Game Action Menu\n ######################################################################################################################################################################{Color.OFF}")
        # display the main menu
        print(f"{Color.GREEN}\nAction Menu{Color.OFF}")
        print(f"- <location>\n- Pickup\n- Drop\n- Attack\n- Perk")

        # if the player has killed more than 5 zombies and have the key they can exit
        if game.player.getKills() > 5 and game.player.getLocation() == "hall" and "key" in game.player.getInventory():
            print("- Exit\n")
        else:
            print("\n")

        if game.building.key == True:
            print(f"{Color.YELLOW}Try searching for the key some where in the house ...{Color.OFF}\n")
        
        # get user input for their next action
        userInput = input("What would you like to do? ").replace(" ", "").lower()

        # perform the action based on input
        if userInput in game.building.rooms:
            game.player.traversLocations(userInput, game.building)
        elif userInput == "stairs" and game.player.location == "hall":
            game.player.traversLocations(userInput, game.building)
        elif userInput == "stairs" and game.player.location == "gameroom":
            game.player.traversLocations(userInput, game.building)
        elif userInput == "pickup":
            if len(game.player.inventory.keys()) >= 2:
                print(f"{Color.RED}You have too many weapons equipped ... drop some to pick up others!{Color.OFF}")
                time.sleep(3)
            else: 
                itemName = input("what item would you like to pick up (weapon name)? ")
                game.player.pickupItem(itemName, game.building)
        elif userInput == "drop":
            itemName = input("What item would you like to drop (weapon name)? ")
            game.player.dropItem(itemName, game.building)
        elif userInput == "attack":
            weaponName = input("What weapon would you like to use? ")
            game.player.attack(game.building, weaponName)
        elif userInput == "perk":
            game.player.usePerk(userInput)
        elif userInput == "exit" and game.building.key == True and "key" in game.player.inventory and game.player.location == 'hall':
            gameCredits(game.player, creditsClock)
            game.endGame = True
            time.sleep(2)
            os.system('clear')
            exit()
        else:
            print(f"{Color.RED}Invalid input ... Pick from the options above {Color.OFF}")
            time.sleep(3)
        os.system('clear')

    game.endGame = True

#########################################################################################
#########################################################################################
#########################################################################################

# game timer
def gameTimer():
    global gameClock
    global creditsClock

    while game.endGame == False:
        print(game.endGame)
        gameClock+= 1
        creditsClock = gameClock

        # deploy a zombie and weapon every 30 seconds
        if gameClock % 30 == 0:
            deployZombie(game.building)
            deployWeapon(game.building)

        # deploy the key if the player has killed more than 5 zombies and 3 minutes has gone by
        if gameClock >= 180 and game.player.getKills() >= 5 and game.building.getKey() == False:
            deployKey(game.building)
            game.building.setKey(True)

        # checks the game clock to see if the game should end    
        if(gameClock >= 600 or game.player.getHealth() <= 0):
            game.endGame = True
            os.system('clear')
            # display the game over screen if the main game thread ends
            gameOver()
        # sleep for 1 second
        time.sleep(1)

#########################################################################################
#########################################################################################
#########################################################################################

# create cli UI
def cliUI():
    locationInfo = game.building.rooms[game.player.getLocation()]
    # print the table
    gameTable(game.player, locationInfo)
    # print the map
    maps(game.player.getLocation())

#########################################################################################
#########################################################################################
#########################################################################################

# run the game
if __name__ == "__main__":
    startGame()