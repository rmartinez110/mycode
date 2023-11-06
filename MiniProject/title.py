#! /usr/bin/env python3
import os
import time
from colorist import Color

def title():
    """
    Description:
      - Title workflow that prints each part of the workflow
    Parameters:
      - None
    Returns:
      - None
    """
    os.system('clear')
    
    print(f'''{Color.RED}

          ▒███████▒    ▒█████      ███▄ ▄███▓    ▄▄▄▄       ██▓   ▓█████          ▓█████      ██████     ▄████▄      ▄▄▄          ██▓███     ▓█████ 
          ▒ ▒ ▒ ▄▀░   ▒██▒  ██▒   ▓██▒▀█▀ ██▒   ▓█████▄    ▓██▒   ▓█   ▀          ▓█   ▀    ▒██    ▒    ▒██▀ ▀█     ▒████▄       ▓██░  ██▒   ▓█   ▀ 
          ░ ▒ ▄▀▒░    ▒██░  ██▒   ▓██    ▓██░   ▒██▒ ▄██   ▒██▒   ▒███            ▒███      ░ ▓██▄      ▒▓█    ▄    ▒██  ▀█▄     ▓██░ ██▓▒   ▒███   
            ▄▀▒   ░   ▒██   ██░   ▒██    ▒██    ▒██░█▀     ░██░   ▒▓█  ▄          ▒▓█  ▄      ▒   ██▒   ▒▓▓▄ ▄██▒   ░██▄▄▄▄██    ▒██▄█▓▒ ▒   ▒▓█  ▄ 
          ▒███████▒   ░ ████▓▒░   ▒██▒   ░██▒   ░▓█  ▀█▓   ░██░   ░▒████▒         ░▒████▒   ▒██████▒▒   ▒ ▓███▀ ░    ▓█   ▓██▒   ▒██▒ ░  ░   ░▒████▒
          ░▒▒ ▓░▒░▒   ░ ▒░▒░▒░    ░ ▒░   ░  ░   ░▒▓███▀▒   ░▓     ░░ ▒░ ░         ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░    ▒▒   ▓▒█░   ▒▓▒░ ░  ░   ░░ ▒░ ░
          ░░▒ ▒ ░ ▒     ░ ▒ ▒░    ░  ░      ░   ▒░▒   ░     ▒ ░    ░ ░  ░          ░ ░  ░   ░ ░▒  ░ ░     ░  ▒        ▒   ▒▒ ░   ░▒ ░         ░ ░  ░
          ░ ░ ░ ░ ░   ░ ░ ░ ▒     ░      ░       ░    ░     ▒ ░      ░               ░      ░  ░  ░     ░             ░   ▒      ░░             ░   
            ░ ░           ░ ░            ░       ░          ░        ░  ░            ░  ░         ░     ░ ░               ░  ░                  ░  ░
          ░                                           ░                                                 ░                                           

{Color.OFF}''')
    
    time.sleep(4)

    os.system('clear')

    print(f'''\n\n
{Color.RED}A Zombie Sandwich Production \n\n
          {Color.OFF}''')
    
    time.sleep(2)

    os.system('clear')

    print(f'''\n\n
{Color.BLUE}GAME RULES{Color.OFF}\n
The goal of the game is to kill zombies and try to find an escape route.
While doing this keep the below in mind:\n\n
1.) You can only move to rooms that are connected to the room you are in. 
    You can get a list for each room by looking at the Game Stats table 
    located at the top of the game screen when playing.\n
2.) You can only carry two weapons at a time. If you find yourself needing 
    to pick up another weapon and already have two weapons in your inventory
    you will need to drop one before picking another up.\n
3.) You can only exit the building once you have the required key. Keep an eye 
    out for the key in the game stats table under the location inventory. You 
    will also get a hint once the key is deployed right below the map in yellow.\n
4.) Once you have the key make your way to the first level hallway which will give 
    you the option to exit if you have the key and have killed the minimum amount of 
    zombies. If all the conditions are meet you will have the exit option available 
    in the hallway action menu.\n
5.) Weapons all have a durability value meaning that each weapon can kill a set 
    amount of zombies. For example, a knife might be good for only one zombie, however, 
    a sword might be good for two zombies. Once the durability is diminished the weapon 
    will be destroyed.\n
6.) You can see the game stats table at the top of the game screen when playing. The 
    table contains information such as player information, location information to 
    include inventory for each, the number of kills, traversable rooms and so on.\n
7.) The action menu is located at the bottom of the game screen when playing with the 
    following options.
        - <move>: To move all you need to do is type the name of the location you want 
          to move to (not case sensitive or space sensitive). For example, > office
        - pickup: To pick up items you need to type pickup then click enter. Once you do that
          you will be prompted to pick up which item. For example, > pickup ... then ... combat knife
        - drop: To drop items you need to type drop then click enter. Once you do that you will
          be prompted to drop which item. For example, > drop ... then ... combat knife
        - attack: To attack zombies you need to type attack then click enter. Once you do that you will
          be prompted asking which weapon you want to use (keeping in mind some have higher durability).
          For example, > attack ... then ... torch
        - exit: To exit the building you need to type exit then click enter. Keep in mind this will 
          only be available if you have meet all the requirements so keep playing till you get there.
    ''')

    
    input(f'{Color.GREEN}Press enter to continue{Color.OFF}')

    os.system('clear')