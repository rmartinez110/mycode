#!/usr/bin/env python3

from colorist import Color
import os
from recipeBook import RecipeBook

# Main
def main():
    recipeBook = RecipeBook()
    exitStatus = False
    os.system('clear')

    # Main menu
    while not exitStatus:
        # display the main menu and return the user selection and assign to userSelection
        userSelection = recipeBook.mainMenu()

        # check if the user selection is exit if not exit then call subMenu and assign to subMenuSelection
        if (userSelection == "exit"):
            exitStatus = True

        # check if the user selection is invalid then display error message and loop the back to the main menu
        elif(userSelection != "Invalid"):
            subMenuExit = False
            while not subMenuExit:
                subMenuSelection = recipeBook.subMenu(userSelection)
                os.system('clear')
                # check if the user selection is exit if not exit then call subMenu and assign to subMenuSelection
                if (subMenuSelection != "exit"):
                    # try to get the ingredients for the selected item
                    try:
                        if(userSelection == "smoothie"):
                            listIngredients = recipeBook.smoothies.getSmoothieIngredients(subMenuSelection)
                            recipeBook.outputIngredients(listIngredients, subMenuSelection)
                        elif (userSelection == "omelet"):
                            listIngredients = recipeBook.omelets.getOmeletIngredients(subMenuSelection)
                            recipeBook.outputIngredients(listIngredients, subMenuSelection)
                        elif (userSelection == "sandwich"):
                            listIngredients = recipeBook.sandwiches.getSandwichIngredients(subMenuSelection)
                            recipeBook.outputIngredients(listIngredients, subMenuSelection)
                    except:
                        print(f"{Color.RED} !!!!! Invalid selection !!!!! {Color.OFF}")
                else:
                    subMenuExit = True
     
# Run main
if __name__ == "__main__":
    main()
