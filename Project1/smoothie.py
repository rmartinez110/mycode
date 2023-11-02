#! /usr/bin/env python3

class SmoothieRecipes:

    def __init__(self):
        self.smoothie_recipes = {
    "berry blast": {
        "ingredients": ["1 cup mixed berries (strawberries, blueberries, raspberries)", "1/2 banana", "1 cup yogurt", "1/2 cup orange juice", "1 tablespoon honey (optional)"]
    },
    "tropical paradise": {
        "ingredients": ["1 cup pineapple chunks", "1/2 cup mango chunks", "1/2 banana", "1/2 cup coconut milk", "1/2 cup orange juice", "Ice cubes (optional)"]
    },
    "green power": {
        "ingredients": ["1 cup spinach leaves", "1/2 cucumber", "1/2 avocado", "1/2 cup green apple slices", "1 cup coconut water", "1 tablespoon honey (optional)"]
    },
    "mango madness": {
        "ingredients": ["1 cup ripe mango chunks", "1/2 banana", "1 cup Greek yogurt", "1/2 cup almond milk", "1 tablespoon honey (optional)"]
    },
    "peanut butter banana ": {
        "ingredients": ["2 ripe bananas", "2 tablespoons peanut butter", "1 cup milk", "1/2 cup Greek yogurt", "1 tablespoon honey (optional)", "Ice cubes (optional)"]
    },
    "chocolate banana": {
        "ingredients": ["2 ripe bananas", "2 tablespoons cocoa powder", "1 cup milk", "1/2 cup Greek yogurt", "1 tablespoon honey (optional)", "Ice cubes (optional)"]
    },
    "strawberry banana oat": {
        "ingredients": ["1 cup strawberries", "1 ripe banana", "1/2 cup rolled oats", "1 cup milk", "1/2 cup Greek yogurt", "1 tablespoon honey (optional)"]
    },
    "blueberry spinach": {
        "ingredients": ["1 cup blueberries", "1 cup spinach leaves", "1/2 banana", "1 cup almond milk", "1 tablespoon honey (optional)"]
    },
    "pineapple coconut": {
        "ingredients": ["1 cup pineapple chunks", "1/2 cup shredded coconut", "1/2 banana", "1 cup coconut milk", "1 tablespoon honey (optional)"]
    },
    "mint chocolate chip": {
        "ingredients": ["1 cup fresh mint leaves", "2 tablespoons cocoa powder", "1 cup milk", "1/2 cup Greek yogurt", "1 tablespoon honey (optional)", "Ice cubes (optional)"]
    }
    }

    # returns all the smoothie names in the dictionary
    def getSmoothieNames(self):
        return list(self.smoothie_recipes.keys())

    # returns the ingredients for a specific smoothie
    def getSmoothieIngredients(self, smoothieName):
        return self.smoothie_recipes[smoothieName]["ingredients"]

    # adds a recipe to the dictionary
    def addRecipe(self, smoothieName, ingredients):
        try:
            self. smoothie_recipes[smoothieName] = {"ingredients": ingredients}
            return f"A recipe with the name {smoothieName} has been created successfully"
        except:
            return f"An error occurred when trying to created the recipe. Please try again."
