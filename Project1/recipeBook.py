#!/usr/bin/env python3

from colorist import Color
import os
from smoothie import SmoothieRecipes
from omelet import OmeletRecipes
from sandwich import SandwichRecipes

class RecipeBook:
    def __init__(self):
        self.smoothies = SmoothieRecipes()
        self.omelets = OmeletRecipes()
        self.sandwiches = SandwichRecipes()

    # Main menu
    def mainMenu(self):
        menuSelections = ["smoothie", "omelet", "sandwich", "exit"]
        print(f"\n{Color.BLUE}#################\n    Main Menu \n#################")
                # for loop to print menu selections
        for menuItem in menuSelections:
            print(menuItem.title())
        print(f"#################{Color.OFF}")
        userSelection = input("Enter your selection (exit to quit the program): ").lower()
        os.system('clear')


        if userSelection in menuSelections:
            return userSelection
        else:
            print(f"\n{Color.RED} !!!!! Invalid menu selection !!!!! {Color.OFF}\n")
            return "Invalid"

    # Sub menu
    def subMenu(self, category):
        menuSelections = []
        if category  == "smoothie":
            menuSelections = self.smoothies.getSmoothieNames()
        elif category == "omelet":
            menuSelections = self.omelets.getOmeletNames()
        elif category == "sandwich":
            menuSelections = self.sandwiches.getSandwichNames()
        else:
            menuSelections = ["Invalid"]
            print(f"{Color.RED} !!!!! Invalid selection !!!!! {Color.OFF}")
        if (menuSelections != "Invalid"):
            print(f"\n{Color.GREEN}##################################\n           Sub Menu \n##################################")
            # for loop to print menu selections
            for menuItem in menuSelections:
                print(menuItem.title())
            print(f"exit")
            print(f"##################################{Color.OFF}")
            userSelection = input("Enter your selection (exit to return to main menu): ").lower()
            return userSelection

    # Output Ingredients
    def outputIngredients(self, ingredients, itemName):
        print(f"\n{Color.YELLOW}####################################################################\n  {itemName.title()} Ingredients   \n####################################################################")
        for ingredient in ingredients:
            print(ingredient)
        print(f"####################################################################{Color.OFF}")
