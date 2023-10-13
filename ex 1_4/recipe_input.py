import pickle

def take_recipe():
    name = input("Provide a Name for the recipe: ")
    cooking_Time = int(input("Provide the Cooking Time for the recipe: "))
    ingredients = list(input("Provide the Ingredients for the recipe: "))
    difficulty = calc_difficulty(cooking_Time, len(ingredients))
    ingredients = [i.title() for i in ingredients]

    recipe = {
       "name": name,
       "cooking time" : cooking_Time,
       "ingredients": ingredients,
       "difficulty": difficulty
    }
    return recipe
# function determing the difficulty of the recipe
def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and ingredients < 4:
     difficulty = "Easy"
    elif cooking_time < 10 and ingredients <= 4:
     difficulty = "Medium"
    elif cooking_time >= 10 and ingredients < 4:
     difficulty = "Intermediate"
    else:
     difficulty = "Hard"
# user provides filename
user_file = input("Enter a File name: ")
# open file and load with pickle
try:
    with open(user_file, "rb") as file:
        data = pickle.load(file)
        recipes_list = data["recipes_list"]
        all_ingredients = data["all_ingredients"]
        print("Data loaded successfully.")
# if file not found inform user, then create new dictionary
except FileNotFoundError:
   print("No files match the name - creating a new one")
   data = {
      "recipes_list" : [],
      "all_ingredients": [] 
   }
# if unexpected error inform user, then create new dictionary
except FileExistsError:
   print("The file already exist.")
except Exception as e:
   print("An error ocurred:", str(e))
else:
    user_file.close()
# extract values from dictionary into two seperate lists
finally:
   recipes_list = data["recipes_list"] 
   all_ingredients = data["all_ingredients"]
# user provides number of recipes
n = int(input("How many recipes would you like to enter? "))
    
for i in range(0, n):
    recipe = take_recipe()
# checks for ingredient in ingredient list, if not there then adds it
    for ele in recipe["ingredients"]:
        if ele not in all_ingredients:
            all_ingredients.append(ele)
    # adds recipe to recipe list
    recipes_list.append(recipe)
    print("Recipe added!")

  

# update data dictionary with newly added recipes/ingredients
data = {
   "recipes_list": recipes_list,
   "all_ingredients": all_ingredients   
}

with open(user_file, "wb") as file:
    pickle.dump(data, file)

print("Recipe file has been updated")