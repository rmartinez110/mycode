#! /usr/bin/env python3
import random
import time

def deployKey(location):
    """
    Description:
        -   deploys the key to a random location in the map
    
    Parameters:
        -   location: The location of the room to deploy the key to
        
    Returns:
        -   None
    """
    randomKey = random.choice(list(location.rooms.keys()))
    randomRoom = location.rooms[randomKey]
    randomRoom['inventory']['key'] = {"frontdoor": "exit", "backdoor": "exit"}