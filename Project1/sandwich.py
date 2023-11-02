#! /usr/bin/env python3

class SandwichRecipes:

    def __init__(self):
        self.sandwich_recipes = {
    "classic blt": {
        "ingredients": ["Bacon strips", "Lettuce leaves", "Sliced tomatoes", "Mayonnaise", "Slices of bread"]
    },
    "turkey and swiss": {
        "ingredients": ["Sliced turkey", "Swiss cheese slices", "Lettuce leaves", "Mustard", "Mayonnaise", "Slices of bread"]
    },
    "club": {
        "ingredients": ["Turkey or chicken slices", "Bacon strips", "Lettuce leaves", "Sliced tomatoes", "Mayonnaise", "Slices of bread"]
    },
    "grilled cheese": {
        "ingredients": ["Slices of bread", "Butter", "Sliced cheddar cheese"]
    },
    "egg salad": {
        "ingredients": ["Hard-boiled eggs", "Mayonnaise", "Dijon mustard", "Chopped celery", "Slices of bread"]
    },
    "caprese": {
        "ingredients": ["Fresh mozzarella slices", "Tomato slices", "Fresh basil leaves", "Balsamic glaze", "Slices of bread"]
    },
    "tuna salad": {
        "ingredients": ["Canned tuna", "Mayonnaise", "Chopped celery", "Diced pickles", "Lettuce leaves", "Slices of bread"]
    },
    "roast beef and cheddar": {
        "ingredients": ["Roast beef slices", "Cheddar cheese slices", "Horseradish sauce", "Lettuce leaves", "Slices of bread"]
    },
    "veggie wrap": {
        "ingredients": ["Hummus", "Sliced cucumber", "Sliced bell peppers", "Sliced carrots", "Sliced avocado", "Lettuce leaves", "Whole-grain wrap"]
    },
    "peanut butter and jelly": {
        "ingredients": ["Peanut butter", "Jelly or jam", "Slices of bread"]
    }
    }

    def getSandwichNames(self):
        return list(self.sandwich_recipes.keys())

    # returns the ingredients for a specific smoothie
    def getSandwichIngredients(self, sandwichName):
        return self.sandwich_recipes[sandwichName]["ingredients"]

    # adds a recipe to the dictionary
    def addRecipe(self, sandwichName, ingredients):
        try:
            self.sandwich_recipes[sandwichName] = {"ingredients": ingredients}
            return f"A recipe with the name {sandwichName} has been created successfully"
        except:
            return f"An error occurred when trying to created the recipe. Please try again."
