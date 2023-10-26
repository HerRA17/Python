class Recipe():

    all_ingredients = []
    # initialized method 
    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = ""
    # getter method name
    def get_name(self):
        return self.name
    # setter method name
    def set_name(self, name):
        self.name = name
    # getter method for cooking_time
    def get_cooking_time(self):
        return self.cooking_time
    # setter method cooking time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
    # a method called add_ingredients that takes in variable number of arguments and adds them to the recipe's ingredients
    def add_ingredients(self, *args):
        self.ingredients = args
        self.update_all_ingredients()
    # getter method ingredients
    def get_ingredients(self):
        print("\nIngredients: ")
        print("------------------")
        for ingredient in self.ingredients:
            print("-" + str(ingredient))
    # a getter method for difficulty
    def get_difficulty(self):
        difficulty = self.calculate_difficulty(self.cooking_time, self.ingredients)
        output = "Difficulty: " + str(self.cooking_time)
        self.difficulty = difficulty
        return output
    # a method for calculating the difficulty of a recipe
    def calculate_difficulty(self, cooking_time, ingredients):
            if cooking_time < 10 and len(ingredients) < 4:
                difficulty_level = "easy"
            elif cooking_time < 10 and len(ingredients) >= 4:
                difficulty_level = "medium"
            elif cooking_time >= 10 and len(ingredients) < 4:
                difficulty_level = "intermediate"
            elif cooking_time >= 10 and len(ingredients) >= 4:
                difficulty_level = "hard"
            else:
                print("Something wrong happened, please try again")

            return difficulty_level
    # method to search for an ingredient in the recipe
    def search_ingredient(self, ingredient, ingredients):
        if ingredient in self.ingredients:
            return True
        else: 
            return False
    # a method to updates the all_ingredients list
    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if ingredient not in self.all_ingredients:
                self.all_ingredients.append(ingredient)
    # string representation that prints the Recipe
    def __str__(self):
        output = "Name: " + self.name + \
        "\nIngredients:" + str(self.ingredients) + \
        "\nCooking Time: " + str(self.cooking_time) + " minutes" + \
         "\nDifficulty: " + self.difficulty + \
         "\n --------------"
        for ingredient in self.ingredients:
            output += "- " + ingredient + "\n"
        return output 
    # method to search a recipe that contains a specific ingredient
    def recipe_search(self, recipes_list, ingredient):
        data = recipes_list 
        search_term = ingredient
        for recipe in data:
            if self.search_ingredient(search_term, recipe.ingredients):
                print(recipe)

recipes_list = []

tea = Recipe("Tea")
tea.add_ingredients("Tea Leaves, Sugar, Water")
tea.set_cooking_time(5)
tea.get_difficulty()
print(tea)
recipes_list.append(tea)

coffee = Recipe("Coffee")
tea.add_ingredients("Coffee Powder, Sugar, Water")
tea.set_cooking_time(5)
tea.get_difficulty()
print(coffee)
recipes_list.append(coffee)

cake = Recipe("Cake")
tea.add_ingredients("Butter, Baking Powder Eggs, Vanilla Essence, Flour, Milk, Sugar")
tea.set_cooking_time(50)
tea.get_difficulty()
print(cake)
recipes_list.append(cake)

bananaSmothie = Recipe("Banana Smothie")
tea.add_ingredients("Banana, Milk, Peanut Butter, Sugar, Ice Cubes")
tea.set_cooking_time(5)
tea.get_difficulty()
print(bananaSmothie)
recipes_list.append(bananaSmothie)

print("--------------------------")
print("Recipes List")
print("--------------------------")
for recipe in recipes_list:
    print(recipe)

print("--------------------------")
print("Results for recipe_search with Water: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Water")

print("--------------------------")
print("Results for recipe_search with Sugar: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Sugar")

print("--------------------------")
print("Results for recipe_search with Bananas: ")
print("--------------------------")
tea.recipe_search(recipes_list, "Bananas")