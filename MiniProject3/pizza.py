#!/usr/bin/python3
"""TLG SDE Cohort | Robert Martinez
   A simple Flask server. Responds to HTTP [GET, POST, PUT, DELETE] requests
   """

# An object of Flask class is our WSGI application
# redirect lets you redirect the user to a different URL
from flask import Flask, redirect, url_for, render_template, request
import sqlite3
import json

texasLocations = ["San Antonio", "Dallas", "Houston", "El Paso", "Austin"]
floridaLocations = ["Miami", "Tampa", "Orlando", "Jacksonville", "Tallahassee"]
californiaLocations = ["Los Angeles", "San Diego", "San Francisco", "Sacramento", "San Jose"]
newYorkLocations = ["New York City", "Buffalo", "Rochester", "Syracuse", "Albany"]
connecticutLocations = ["Hartford", "Bridgeport", "New Haven", "Stamford", "Norwalk"]
virginiaLocations = ["Richmond", "Norfolk", "Virginia Beach", "Chesapeake", "Arlington"]
massachusettsLocations = ["Boston", "Worcester", "Springfield", "Lowell", "Cambridge"]

orderNumber = 45856

# Flask constructor takes the name of current
# module (__name__) as argument
app = Flask(__name__)

# main page
@app.route("/")
def gamePage():
   return render_template("index.html")

# order page redirect
@app.route("/order")
def orderPage():
   return render_template("order.html")

@app.route("/confirmation")
def confirmationPage():
   return render_template("confirmation.html")

# api call to place the order
@app.route("/placeorder", methods=['POST'])
def placeOrder():
    global orderNumber
    try:
       data = request.get_json()
       pizzaSize = data.get("size")
       pizzaCrust = data.get("crust")
       pizzaSauce = data.get("sauce")
       pizzaToppings = json.dumps(data.get("toppings"))
       recordId = orderNumber

       conn = sqlite3.connect('Pizza.db')
       cursor = conn.cursor()

       query = "INSERT INTO ORDERS (ID, SIZE, CRUST, SAUCE, TOPPINGS) VALUES (?,?,?,?,?)"

       cursor.execute(query, (recordId, pizzaSize, pizzaCrust, pizzaSauce, pizzaToppings))

       conn.commit()
       conn.close()

       print("successfully placed order")
       msg = {"msg": "Successfully placed the order", 'status': 200}
       orderNumber += 8
    except Exception as e:
       print(e)
       print("failed to place order")
       msg = {'msg': "Failed to place the order. Please try again", 'status': 500}
    return msg

# database setup
@app.route("/database/setup/pizza")
def dbSetupPizza():
   try:
      conn = sqlite3.connect('Pizza.db')
      conn.execute("DROP TABLE IF EXISTS LOCATIONS")
      conn.execute('''CREATE TABLE IF NOT EXISTS LOCATIONS 
      (ID INT PRIMARY KEY     NOT NULL,
      STATE           TEXT    NOT NULL,
      CITY          TEXT    NOT NULL);''')

      createLocation(1, 'Texas', json.dumps(texasLocations))
      createLocation(2, 'Florida', json.dumps(floridaLocations))
      createLocation(3, 'California', json.dumps(californiaLocations))
      createLocation(4, 'New York', json.dumps(newYorkLocations))
      createLocation(5, 'Connecticut', json.dumps(connecticutLocations))
      createLocation(6, 'Virginia', json.dumps(virginiaLocations))
      createLocation(7, 'Massachusetts', json.dumps(massachusettsLocations))
      conn.commit()
      conn.close()
      return "Successfully created the pizza table"
   except Exception as e:
      print(e)
      return "Failed to create the pizza table. Please try again"

# database setup
@app.route("/database/setup/orders")
def dbSetupOrder():
   try:
      conn = sqlite3.connect('Pizza.db')
      conn.execute("DROP TABLE IF EXISTS ORDERS")
      conn.execute('''CREATE TABLE IF NOT EXISTS ORDERS 
      (ID INT PRIMARY KEY     NOT NULL,
      SIZE           TEXT    NOT NULL,
      CRUST           TEXT    NOT NULL,
      SAUCE           TEXT    NOT NULL,
      TOPPINGS          TEXT    NOT NULL);''')
      conn.commit()
      conn.close()
      return "Successfully created the orders table"
   except Exception as e:
      print(e)
      return "Failed to create the orders table. Please try again"

# helper function to create a new location
def createLocation(id, state, city):
   try:
      conn = sqlite3.connect('Pizza.db')
      insert_query = 'INSERT INTO LOCATIONS (ID, STATE, CITY) VALUES (?, ?, ?)'
      conn.execute(insert_query, (id, state, city))
      conn.commit()
      conn.close()
      return "Successfully uploaded a new map"
   except Exception as e:
      print(e)
      return "Upload failed. No modifications were made"

# api call to get all locations
@app.route("/database/getAllLocations")
def getAllLocations():
   try:
      conn = sqlite3.connect('Pizza.db')
      query = "SELECT * FROM LOCATIONS"
      cursor = conn.execute(query)
      locations = cursor.fetchall()
      response = {
         "body":locations,
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

# api call to get all locations
@app.route("/database/getAllOrders")
def getAllOrders():
   try:
      conn = sqlite3.connect('Pizza.db')
      query = "SELECT * FROM ORDERS"
      cursor = conn.execute(query)
      orders = cursor.fetchall()
      response = {
         "body":orders,
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

@app.route("/database/getorder/<orderID>")
def getOrder(orderID):

   global orderNumber

   try:
      conn = sqlite3.connect('Pizza.db')
      conn.row_factory = sqlite3.Row
      cursor1 = conn.execute(f"SELECT * from ORDERS WHERE ID = {orderID}")
      data = cursor1.fetchone()
      body = {
         'ID': data['ID'],
         'SIZE': data['SIZE'],
         'CRUST': data['CRUST'],
         'SAUCE': data['SAUCE'],
         'TOPPINGS': data['TOPPINGS']
      }
      newOrder = body
      print("Operation done successfully")
      try:
         
         cursor = conn.cursor()
         recordId = orderNumber
         print("successfully inserted")
         query = "INSERT INTO ORDERS (ID, SIZE, CRUST, SAUCE, TOPPINGS) VALUES (?,?,?,?,?)"

         cursor.execute(query, (orderNumber, body['SIZE'], body['CRUST'], body['SAUCE'], body['TOPPINGS']))

         conn.commit()
         conn.close()
         orderNumber += 8

         response = {
            'body': newOrder,
            'status': 200
         }
      except Exception as e:
         print(e)
         response = {
            'body': e,
            'status': 500
         }
      conn.close()
   except Exception as e:
      print(e)
      response = {
         'type': type(e).__name__,
         'args': e.args,
         'message': str(e)
    }
   return response
            
if __name__ == "__main__":
   # app.run(host="0.0.0.0", port=2224) # runs the application
   app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
