#! /usr/bin/env python3
from colorist import Color
import time
import os

def gameCredits(player, gameClock):
      """
      Description:
            -     Escape successful message
      Parameters:
            -     player: Player object
            -     gameClock: GameClock object
      
      Return:
            -     None
      """
      os.system('clear')
      print(f'''{Color.GREEN}               
                            ▓█████      ██████     ▄████▄      ▄▄▄          ██▓███     ▓█████ 
                            ▓█   ▀    ▒██    ▒    ▒██▀ ▀█     ▒████▄       ▓██░  ██▒   ▓█   ▀ 
                            ▒███      ░ ▓██▄      ▒▓█    ▄    ▒██  ▀█▄     ▓██░ ██▓▒   ▒███   
                            ▒▓█  ▄      ▒   ██▒   ▒▓▓▄ ▄██▒   ░██▄▄▄▄██    ▒██▄█▓▒ ▒   ▒▓█  ▄ 
                            ░▒████▒   ▒██████▒▒   ▒ ▓███▀ ░    ▓█   ▓██▒   ▒██▒ ░  ░   ░▒████▒
                            ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░   ░ ░▒ ▒  ░    ▒▒   ▓▒█░   ▒▓▒░ ░  ░   ░░ ▒░ ░
                            ░ ░  ░   ░ ░▒  ░ ░     ░  ▒        ▒   ▒▒ ░   ░▒ ░         ░ ░  ░
                            ░      ░  ░  ░     ░             ░   ▒      ░░             ░   
                            ░  ░         ░     ░ ░               ░  ░                  ░  ░
                                                ░                                           
          ''')
    
      print(f'''


          ██████     █    ██     ▄████▄      ▄████▄     ▓█████      ██████      ██████      █████▒    █    ██     ██▓    
        ▒██    ▒     ██  ▓██▒   ▒██▀ ▀█     ▒██▀ ▀█     ▓█   ▀    ▒██    ▒    ▒██    ▒    ▓██   ▒     ██  ▓██▒   ▓██▒    
        ░ ▓██▄      ▓██  ▒██░   ▒▓█    ▄    ▒▓█    ▄    ▒███      ░ ▓██▄      ░ ▓██▄      ▒████ ░    ▓██  ▒██░   ▒██░    
          ▒   ██▒   ▓▓█  ░██░   ▒▓▓▄ ▄██▒   ▒▓▓▄ ▄██▒   ▒▓█  ▄      ▒   ██▒     ▒   ██▒   ░▓█▒  ░    ▓▓█  ░██░   ▒██░    
        ▒██████▒▒   ▒▒█████▓    ▒ ▓███▀ ░   ▒ ▓███▀ ░   ░▒████▒   ▒██████▒▒   ▒██████▒▒   ░▒█░       ▒▒█████▓    ░██████▒
        ▒ ▒▓▒ ▒ ░   ░▒▓▒ ▒ ▒    ░ ░▒ ▒  ░   ░ ░▒ ▒  ░   ░░ ▒░ ░   ▒ ▒▓▒ ▒ ░   ▒ ▒▓▒ ▒ ░    ▒ ░       ░▒▓▒ ▒ ▒    ░ ▒░▓  ░
        ░ ░▒  ░ ░   ░░▒░ ░ ░      ░  ▒        ░  ▒       ░ ░  ░   ░ ░▒  ░ ░   ░ ░▒  ░ ░    ░         ░░▒░ ░ ░    ░ ░ ▒  ░
        ░  ░  ░      ░░░ ░ ░    ░           ░              ░      ░  ░  ░     ░  ░  ░      ░ ░        ░░░ ░ ░      ░ ░   
              ░        ░        ░ ░         ░ ░            ░  ░         ░           ░                   ░            ░  ░
                        ░           ░                                                                            

          {Color.OFF}''')
    
      print(f"{Color.BLUE}######################################### {Color.OFF}")
      print(f"{Color.BLUE}Player Info: {player.name}{Color.OFF}")
      print(f"Name: ............. {player.name}")
      print(f"Kills:........... {player.kills}")
      print(f"Time: ............ {gameClock}")
      print(f"{Color.BLUE}######################################### {Color.OFF}")

      input("\n\nPress enter to continue ... ")