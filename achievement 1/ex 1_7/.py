# search recipe(s) by ingredients
def search_by_ingredients():
# Check if your table has any entries. If there aren’t any entries, notify the user, and exit the function.
  if session.query(Recipe).count() == 0:
   print("There is no recipe in the database")
   return None
  else: 
# Retrieve only the values from the ingredients column of the table, and store them into a variable called results.
    results = session.query(Recipe.ingredients).all()
    print("Results: ", results)
# Initialize an empty list called all_ingredients
    all_ingredients = []
# Iterates through the results list and for each recipe ingredients tuple
    for recipe_ingredients_list in results:
       # Iterate through recipe ingredients tuple
       for recipe_ingredients in recipe_ingredients_list:
          # split each recipe ingredients tuple
          recipe_ingredient_split = recipe_ingredients.split(", ")
          all_ingredients.extend(recipe_ingredient_split)
    print("All ingredients after the loop: ", all_ingredients)
# Remove all duplicates from the list
    all_ingredients = list(dict.fromkeys(all_ingredients))
# Shows the user all the available ingredients contained in all_ingredients
    all_ingredients_list = list(enumerate(all_ingredients))

    print("\nAll ingredients list:")
    print("-"*10)

    for index, tup in enumerate(all_ingredients_list):
       print(str(tup[0]+1) + ". " + tup[1])

    try:
 # User to pick a number from the all_ingredients_list. This number is used as the index to retrieve the corresponding ingredient, which is then stored into a variable called ingredient_searched
      ingredient_searched_number = input("\nEnter the number corresponding to the ingredient you want to select from the above list. You can enter several numbers. In this case, numbers shall be separated by a space: ")
# create a list to identify the different ingredients user wants to search
      ingredients_number_list_searched = ingredient_searched_number.split(" ")
# iterate through the list of ingredients nber searched and associate a ingredient name
      ingredient_searched_list = []
      for ingredient_searched_number in ingredients_number_list_searched:
         ingredient_searched_index = int(ingredient_searched_number) - 1
         ingredient_searched = all_ingredients_list[ingredient_searched_index][1]

         ingredient_searched_list.append(ingredient_searched)
         print("\nYou selected the ingredients(s): ", ingredient_searched_list)
# Initialize an empty list called conditions. This list will contain like() conditions for every ingredient to be searched for
      conditions = []

# Run a loop that runs through ingredient_searched_list
      for ingredient in ingredient_searched_list:
         like_term = "%"+ingredient+"%"
         # Append the search condition containing like_term to the conditions list
         condition = Recipe.ingredients.like(like_term)
         conditions.append(condition)
      print("Conditions: ", conditions)
# Retrieve all recipes from the database using the filter() query, containing the list conditions
      searched_recipes = session.query(Recipe).filter(*conditions).all()
      print(searched_recipes)

    except:
       print("An unexpected error occurred. Make sure to select a number from the list.")
    else:
       print("Searched Recipes: ")
       for recipe in searched_recipes:
          print(recipe)