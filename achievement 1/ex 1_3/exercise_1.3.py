recipes_list = []
ingredients_list = []

def take_recipe():
   name = str(input("Add the name of the recipe: "))
   cooking_time = int(input("Add the cooking time for the recipe: "))
   ingredients = list(input("Add the ingredients for the Recipe: ").split(","))
   recipe = { "Name": name, "Cooking Time": cooking_time, "Ingredients": ingredients}
   return recipe

n = int(input("How many recipes would you like to enter? "))
    
for i in range(n):
   recipe = take_recipe()
   for ingredient in recipe["Ingredients"]:
      if ingredient not in ingredients_list:
         ingredients_list.append(ingredient)

recipes_list.append(recipe)

for recipe in recipes_list:
    cooking_time = recipe["Cooking Time"]
    ingredients = len(recipe["Ingredients"])

if cooking_time < 10 and ingredients < 4:
   difficulty = "Easy"
elif cooking_time < 10 and ingredients <= 4:
   difficulty = "Medium"
elif cooking_time >= 10 and ingredients < 4:
     difficulty = "Intermediate"
else:
      difficulty = "Hard"

recipe["Difficulty"] = difficulty

print('========================')
print("Recipe: ", recipe["Name"])
print("Cooking Time: ", recipe["Cooking Time"])
print("Ingredients: ", recipe["Ingredients"])
print("Difficulty: ", recipe["Difficulty"])

def print_ingredients():
    ingredients_list.sort()
    print('========================')
    print('ingredients avaliable for all recipes')
    print('-----------------------')
    for ingredient in ingredients_list:
        print(ingredient)
        
print_ingredients()