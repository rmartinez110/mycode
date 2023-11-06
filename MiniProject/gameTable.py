#! /usr/bin/env python3
from colorist import Color

def gameTable(playerInfo, locationInfo):
    """
    Description:
        -   Creates the game status table that provides information such as player info and map info
    Parameters:
        -   playerInfo: player information used to display the player info in the table
        -   locationInfo: location information used to display the map info in the table
    Return:
        -   None
    """
    # Game data
    playerData = [
        ["Player Info: ",                                                       f"{locationInfo['name']} Info:"],
        [f"Name:........... {playerInfo.getName()}",                                 f"Room Inventory: {', '.join(map(str, locationInfo['inventory']))}"],
        [f"Inventory:...... {', '.join(map(str, playerInfo.getInventory()))}",       f"Room Occupants: {', '.join(map(str, locationInfo['occupants']))}"],
        [f"Health:......... {playerInfo.getHealth()}",                               f"Traversable Rooms: {', '.join(map(str, locationInfo['traversable']))}"],
        [f"Location:....... {playerInfo.getLocation()}",                             "",],
        [f"Kills: ..........{playerInfo.getKills()}",                                    ""]

    ]

    # Calculate the maximum width of each column
    max_widths = [max(len(str(cell)) for cell in col) for col in zip(*playerData)]

    print(f"{Color.BLUE}Game Stats\n######################################################################################################################################################################{Color.OFF}")

    # Print the table header
    print(f"{Color.GREEN}{playerData[0][0]:<{max_widths[0]}} \t\t{playerData[0][1]:<{max_widths[1]}}{Color.OFF}")

    # Print the table rows
    for row in playerData[1:]:
        print(f"{row[0]:<{max_widths[0]}} \t\t{row[1]:<{max_widths[1]}}")

    print("\n")