#!/usr/bin/python3
"""TLG SDE Cohort | Robert Martinez
   A simple Flask server. Responds to HTTP [GET, POST, PUT, DELETE] requests
   """

# An object of Flask class is our WSGI application
# redirect lets you redirect the user to a different URL
from flask import Flask, redirect, url_for, render_template, request
import sqlite3
import json

building = {
    "1": {
        "livingroom": {
            "name": "Livingroom",
            "inventory": {},
            "occupants": [],
            "exit": "back door",
            "traversable": ["hall", "kitchen"],
        },
        "kitchen": {
            "name": "Kitchen",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["livingroom", "hall"],
        },
        "hall": {
            "name": "Hall",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": [
                "kitchen",
                "livingroom",
                "restroom1",
                "office",
                "garage",
                "stairs",
            ],
        },
        "office": {
            "name": "Office",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["hall"],
        },
        "restroom1": {
            "name": "Restroom 1",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["hall"],
        },
        "garage": {
            "name": "Garage",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["hall"],
        },
    },
    "2": {
        "gameroom": {
            "name": "Gameroom",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": [
                "bedroom1",
                "bedroom2",
                "masterbedroom",
                "restroom2",
                "stairs",
            ],
        },
        "bedroom1": {
            "name": "Bedroom 1",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["gameroom"],
        },
        "bedroom2": {
            "name": "Bedroom 2",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["gameroom"],
        },
        "masterbedroom": {
            "name": "Master Bedroom",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["gameroom"],
        },
        "restroom2": {
            "name": "Restroom 2",
            "inventory": {},
            "occupants": [],
            "exit": "none",
            "traversable": ["gameroom"],
        },
    },
}

roomCoordinates = {
    "1": {
        "office": { "x": { "min": 17, "max": 246 }, "y": { "min": 65, "max": 198 } },
        "stairs": { "x": { "min": 425, "max": 484 }, "y": { "min": 287, "max": 323 } },
        "garage": { "x": { "min": 345, "max": 602 }, "y": { "min": 65, "max": 278 } },
        "livingroom": { "x": { "min": 298, "max": 602 }, "y": { "min": 337, "max": 541 } },
        "kitchen": { "x": { "min": 17, "max": 299 }, "y": { "min": 331, "max": 541 } },
        "restroom1": { "x": { "min": 17, "max": 245 }, "y": { "min": 199, "max": 324 } },
        "hall": { "x": { "min": 252, "max": 337 }, "y": { "min": 66, "max": 336 } },
    },
    "2": {
        "stairs": { "x": { "min": 425, "max": 484 }, "y": { "min": 287, "max": 323 } },
        "gameroom": { "x": { "min": 251, "max": 599 }, "y": { "min": 60, "max": 335 } },
        "bedroom1": { "x": { "min": 19, "max": 250 }, "y": { "min": 60, "max": 195 } },
        "restroom2": { "x": { "min": 19, "max": 247 }, "y": { "min": 202, "max": 324 } },
        "bedroom2": { "x": { "min": 19, "max": 250 }, "y": { "min": 329, "max": 540 } },
        "masterbedroom": { "x": { "min": 251, "max": 601 }, "y": { "min": 330, "max": 540 } },
    },
};

weapons = {
   "axe": {"name": "axe", "damage": 30, "durability" : 2}, 
   "hammer": {"name": "hammer", "damage": 20, "durability" : 1}, 
   "chainsaw": {"name": "chainsaw", "damage": 60, "durability" : 3}, 
   "kitchen knife": {"name": "kitchen knife", "damage": 25, "durability" : 1}, 
   "combat knife": {"name": "combat knife", "damage": 35, "durability" : 2}, 
   "torch": {"name": "torch", "damage": 40, "durability" : 1}, 
   "grenade": {"name": "grenade", "damage": 35, "durability" : 1}, 
   "pistol": {"name": "pistol", "damage": 60, "durability" : 3}, 
   "pipe": {"name": "pipe", "damage": 15, "durability" : 2}, 
   "saw": {"name": "saw", "damage": 70, "durability" : 1}, 
   "sword": {"name": "sword", "damage": 50, "durability" : 2}
   }

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# main game page
@app.route("/")
@app.route("/game")
def gamePage():
   return render_template("gamePage/gamepage.html")

# api call to get the building details
@app.route("/game/building/<buildingNumber>")
def buildingDetails(buildingNumber):
   dbSetup()
   uploadBuilding(1, json.dumps(building), json.dumps(roomCoordinates), json.dumps(weapons), 1)
   downloadBuilding(1)
   return buildingNumber

# api call to get the game map that only accepts GET requests
@app.route("/game/map/<id>")
def downloadBuilding(id):
   try:
      conn = sqlite3.connect('ZombieEscape.db')
      cursor = conn.execute(f"SELECT FLOORPLAN, ROOMCOORDINATES, WEAPONS FROM BUILDINGS WHERE ID = {id}")
      gameMap = cursor.fetchone()
      response = {
         "body":gameMap,
         "status":200
      }
      conn.close()
   except Exception as e:
      print(e)
      response = {
         "body":e,
         "status":500
      }
   return response

# database setup
def dbSetup():
   try:
      conn = sqlite3.connect('ZombieEscape.db')
      conn.execute("DROP TABLE IF EXISTS BUILDINGS")
      conn.execute('''CREATE TABLE IF NOT EXISTS BUILDINGS 
      (ID INT PRIMARY KEY     NOT NULL,
      FLOORPLAN           TEXT    NOT NULL,
      ROOMCOORDINATES          TEXT    NOT NULL,
      WEAPONS              TEXT        NOT NULL,
      VERSION            INT     NOT NULL);''')
      conn.close()
      return "Successfully created the buildings table"
   except Exception as e:
      print(e)
      return "Failed to create the buildings table. Please try again"

# map upload
def uploadBuilding(id, floorplan, coordinates, weapons, version):
   try:
      conn = sqlite3.connect('ZombieEscape.db')
      insert_query = 'INSERT INTO BUILDINGS (ID, FLOORPLAN, ROOMCOORDINATES, WEAPONS, VERSION) VALUES (?, ?, ?, ?, ?)'
      conn.execute(insert_query, (id, floorplan, coordinates, weapons, version))
      conn.commit()
      conn.close()
      return "Successfully uploaded a new map"
   except Exception as e:
      print(e)
      return "Upload failed. No modifications were made"

if __name__ == "__main__":
   # app.run(host="0.0.0.0", port=2224) # runs the application
   app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
