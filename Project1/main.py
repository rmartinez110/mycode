#!/usr/bin/env python3

from colorist import Color
import os
from smoothie import SmoothieRecipes
from omelet import OmeletRecipes
from sandwich import SandwichRecipes

# create an instance of smoothie, omelet, and sandwich
smoothies = SmoothieRecipes()
omelets = OmeletRecipes()
sandwiches = SandwichRecipes()


# Main menu
def mainMenu():
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
def subMenu(category):
    menuSelections = []
    if category  == "smoothie":
        menuSelections = smoothies.getSmoothieNames()
    elif category == "omelet":
        menuSelections = omelets.getOmeletNames()
    elif category == "sandwich":
        menuSelections = sandwiches.getSandwichNames()
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
def outputIngredients(ingredients, itemName):
    print(f"\n{Color.YELLOW}####################################################################\n  {itemName.title()} Ingredients   \n####################################################################")
    for ingredient in ingredients:
        print(ingredient)
    print(f"####################################################################{Color.OFF}")
# Main
def main():
    exitStatus = False
    os.system('clear')

    # Main menu
    while not exitStatus:
        # display the main menu and return the user selection and assign to userSelection
        userSelection = mainMenu()

        # check if the user selection is exit if not exit then call subMenu and assign to subMenuSelection
        if (userSelection == "exit"):
            exitStatus = True

        # check if the user selection is invalid then display error message and loop the back to the main menu
        elif(userSelection != "Invalid"):
            subMenuExit = False
            while not subMenuExit:
                subMenuSelection = subMenu(userSelection)
                os.system('clear')
                # check if the user selection is exit if not exit then call subMenu and assign to subMenuSelection
                if (subMenuSelection != "exit"):

                    # try to get the ingredients for the selected item
                    try:
                        if(userSelection == "smoothie"):
                            listIngredients = smoothies.getSmoothieIngredients(subMenuSelection)
                            outputIngredients(listIngredients, subMenuSelection)
                        elif (userSelection == "omelet"):
                            listIngredients = omelets.getOmeletIngredients(subMenuSelection)
                            outputIngredients(listIngredients, subMenuSelection)
                        elif (userSelection == "sandwich"):
                            listIngredients = sandwiches.getSandwichIngredients(subMenuSelection)
                            outputIngredients(listIngredients, subMenuSelection)
                    except:
                        print(f"{Color.RED} !!!!! Invalid selection !!!!! {Color.OFF}")
                else:
                    subMenuExit = True
     
# Run main
if __name__ == "__main__":
    main()
