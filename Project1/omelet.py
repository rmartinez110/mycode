#! /usr/bin/env python3

class OmeletRecipes:

    def __init__(self):
        self.omelet_recipes = {
    "classic cheese": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup shredded cheddar cheese", "1 tablespoon butter"]
    },
    "vegetable": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup diced bell peppers", "1/4 cup diced onions", "1/4 cup diced tomatoes", "1/4 cup shredded cheddar cheese", "1 tablespoon butter"]
    },
    "mushroom and swiss": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup sliced mushrooms", "2 tablespoons grated Swiss cheese", "1 tablespoon butter"]
    },
    "ham and cheese": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup diced ham", "1/4 cup shredded cheddar cheese", "1 tablespoon butter"]
    },
    "spinach and feta": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup fresh spinach leaves", "2 tablespoons crumbled feta cheese", "1 tablespoon butter"]
    },
    "western": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup diced ham", "1/4 cup diced bell peppers", "1/4 cup diced onions", "1/4 cup shredded cheddar cheese", "1 tablespoon butter"]
    },
    "mediterranean": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "1/4 cup diced tomatoes", "2 tablespoons sliced black olives", "2 tablespoons crumbled feta cheese", "1 tablespoon chopped fresh basil", "1 tablespoon butter"]
    },
    "bacon and mushroom": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "2 strips cooked bacon, crumbled", "1/4 cup sliced mushrooms", "2 tablespoons shredded cheddar cheese", "1 tablespoon butter"]
    },
    "sausage and pepper": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "2 cooked sausages, sliced", "1/4 cup sliced bell peppers", "1/4 cup sliced onions", "2 tablespoons shredded mozzarella cheese", "1 tablespoon butter"]
    },
    "asparagus and goat cheese": {
        "ingredients": ["2 large eggs", "2 tablespoons milk", "Salt and pepper to taste", "4 asparagus spears, trimmed and blanched", "2 tablespoons crumbled goat cheese", "1 tablespoon chopped fresh chives", "1 tablespoon butter"]
    }
    }

    def getOmeletNames(self):
        return list(self.omelet_recipes.keys())

    # returns the ingredients for a specific smoothie
    def getOmeletIngredients(self, omeletName):
        return self.omelet_recipes[omeletName]["ingredients"]

    # adds a recipe to the dictionary
    def addRecipe(self, omeletName, ingredients):
        try:
            self.omelet_recipes[omeletName] = {"ingredients": ingredients}
            return f"A recipe with the name {omeletName} has been created successfully"
        except:
            return f"An error occurred when trying to created the recipe. Please try again."
