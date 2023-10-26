# Creates an engine object called engine that connects to your desired database.
from sqlalchemy import create_engine

engine = create_engine("mysql://cf-python:Hermannr17@localhost/my_database")

from sqlalchemy.orm import declarative_base, sessionmaker
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy.types import Integer, String

#  Declares Recipe Class that inherits from Base
class Recipe(Base):
    __tablename__= "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(250))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        return "<Recipe ID: " + str(self.id) + "-" + self.name + ">"
    
    def __str__(self):
        output = ("\nRecipe Name: " + str(self.name) +  
          "\nRecipe Ingredients: " + str(self.ingredients) + 
          "\nRecipe Cooking time (min): " + str(self.cooking_time) + 
          "\nRecipe Difficulty: " + str(self.difficulty))
        return output

# create tables of all models defined
Base.metadata.create_all(engine)
# Creates a session object that will be used to make changes to the database
Session = sessionmaker(bind=engine)
session = Session()

# calculate_difficulty() calculates the difficulty of the recipe by taking in cooking_time and ingredients as arguments, and assign the difficulty level as a strings: Easy, Medium, Intermediate, or Hard to the difficulty variable
def calc_difficulty(cooking_time, recipe_ingredients):
      print("Run the calc_difficulty with: ", cooking_time, recipe_ingredients)

      if (cooking_time < 10) and (len(recipe_ingredients) < 4):
        difficulty = "Easy"
      elif (cooking_time < 10) and (len(recipe_ingredients) >= 4):
        difficulty = "Medium"
      elif (cooking_time >= 10) and (len(recipe_ingredients) < 4):
        difficulty = "Intermediate"
      elif (cooking_time >= 10) and (len(recipe_ingredients) >= 4):
        difficulty = "Hard"
      else:
        print("Something bad happened, please try again")
    
      print("Difficulty level: ", difficulty)
      return difficulty
# return_ingredients_as_list() function retrieves the ingredients string inside Recipe object as a list
def return_ingredients_as_list():
# assign all recipes to recepis_list
        recipes_list = session.query(Recipe).all()
        for recipe in recipes_list:
          print("Recipe :", recipe)
          print("Recipe Ingredients: ", recipe.ingredients)
# split the strings and create a list and 
          recipe_ingredients_list = recipe.ingredients.split(", ")
          print(recipe_ingredients_list)
    

# create recipe function
# Function below allows the user to input a new recipe data (name, cooking time, ingredients) and also automatically determines a difficulty level based on cooking time and number of ingredients
def create_recipe():
    recipe_ingredients = []
# Keep prompting the user until they enter a name < 50 with only alphabetical characters and numeric cooking time
    correct_input_name = False
    while correct_input_name == False:
# Asks the user to input recipe name
      name = input("\nEnter the name of the recipe: ")
      if len(name) < 50:
         correct_input_name = True

         correct_input_cooking_time = False
         while correct_input_cooking_time == False:
# Asks the user to input cooking time
          cooking_time = input("\nEnter the cooking time of the recipe (min): ")
          if cooking_time.isnumeric() == True:
             correct_input_cooking_time = True

          else:
            print("Please enter a number.")

      else:
         print("Please enter a name that contains less than 50 characters.")       
  # Asks the user to enter the number of ingredients he wants to add
  # Then, asks the user to input ingredients
      correct_input_number = False 
      while correct_input_number == False:
         ing_number = input("How many ingredients do you want to enter? ")
         if ing_number.isnumeric()  == True:
            correct_input_number = True

            for _ in range(int(ing_number)):
               ingredient = input("Enter an ingredient: ")
               recipe_ingredients.append(ingredient)
         else:
          correct_input_number = False
          print("Please enter a pasitive number.")

# Converts recipe_ingredients into comma-separated strings as MySQL doesn't fully support arrays
      recipe_ingredients_str = ",".join(recipe_ingredients)
      print(recipe_ingredients_str)

# Call calculate_difficulty() that calculates the difficulty of the recipe by taking in cooking_time and ingredients as arguments, and returning one of the following strings: Easy, Medium, Intermediate, or Hard
      difficulty = calc_difficulty(int(cooking_time), recipe_ingredients)
# Create a new Object from Recipe model called recipe_entry
      recipe_entry = Recipe(
         name = name,
         cooking_time = int(cooking_time),
         ingredients = recipe_ingredients_str,
         difficulty = difficulty 
         )
      print(recipe_entry)

#  Add the recipe to the final_recipes table and comit the changes
      session.add(recipe_entry)
      session.commit()

      print("Recipe saved into the database.")


# view all recipes
def view_all_recipes():
    all_recipes = []
    all_recipes = session.query(Recipe).all()

# If there aren’t any entries, inform the user that there aren’t any entries in your database
    if len(all_recipes) == 0:
        print("There is no Recipe in the database")
        return None

# Else, print all the recipes entered in the database
    else:
       print("\nAll recipes can be found below: ")
       print("-"*10)
       for recipe in all_recipes:
         print(recipe)

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


# edit recipe
def edit_recipe():
    if session.query(Recipe).count() == 0:
       print("There is no recipe in the database")
       return None
    else:
# Retrieve only the values from the id and name columns of the table, and store them into a variable called results.
       results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
       print("Results: ", results)
       print("Lits of available recipes:")
       for recipe in results:
        print("\nId: ", recipe[0])
        print("Name: ", recipe[1])
       
# Asks the user to input the ID of the recipe he wants to edit
        recipe_id_for_edit = int((input("\nEnter the ID of the recipe you want to edit (or '0' to exit): ")))
        
        print(session.query(Recipe).with_entities(Recipe.id).all())

        recipe_id_tup_list = session.query(Recipe).with_entities(Recipe.id).all()
        recipes_id_list = []

        for recipe_tup in recipe_id_tup_list:
           print(recipe_tup[0])
           recipes_id_list.append(recipe_tup[0])

        print(recipes_id_list)
        
        if recipe_id_for_edit == 0:
           return # exit function
        elif recipe_id_for_edit not in recipes_id_list:
           print("Not in the ID list, please try again later.")
           return
        else:
           print("Ok you can continue")
# Look for the object associated with the ID and retrieve it
           recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).one()

           print("\nWARNING: You are about to edit the following recipe: ")
           print(recipe_to_edit)
# Asks the user to input which column he wants to update among name, cooking_time and ingredients
           column_for_update = int(input("\nEnter the data you want to update among 1. name, 2. cooking time and 3. ingredients: (select '1' or '2' or '3'): "))
#  Asks the user to input the new value
           updated_value = (input("\nEnter the new value for the recipe: "))
           print("Choice: ", updated_value)

           if column_for_update == 1:
              print("You want to update the name of the recipe")
              session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.name: updated_value})
              session.commit()
           elif column_for_update == 2:
              print("You want to update the cooking time of the recipe")
              session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.cooking_time: updated_value})
              session.commit()
           elif column_for_update == 3:
              print("You want to update the ingredients of the recipe")
              session.query(Recipe).filter(Recipe.id == recipe_id_for_edit).update({Recipe.ingredients: updated_value})
              session.commit()
           elif column_for_update == 0:
              print("Exiting the edit recipe function.")
              return
           else:
              print("Wrong input, please try again.")
# Recalculate the difficulty
           update_difficulty = calc_difficulty(recipe_to_edit.cooking_time, recipe_to_edit.ingredients)
           print("Updated difficulty: ", update_difficulty)
# Assign the updated difficulty to edited recipe
           recipe_to_edit.difficulty = update_difficulty
# Commit changes to the database
           session.commit()
           print("Modification done.")
# delete recipe
def delete_recipe():
# Check if your table has any entries. If there aren’t any entries, notify the user, and exit the function
    if session.query(Recipe).count() == 0:
       print("There is no recipe in the database")
       return None
    else:
# Retrieve only the values from the id and name columns of the table, and store them into a variable called results.
       results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()
       print("Results: ", results)
       print("List of recipes available: ")
       for recipe in results:
          print("\nId: ", recipe[0])
          print("Name: ", recipe[1])
# Asks the user to input the ID of the recipe he wants to delete
       recipe_id_for_deletion = (input("\nEnter the ID of the recipe you want to delete: "))
# Look for the object associated with the ID and retrieve it
       recipe_to_be_deleted = session.query(Recipe).filter(Recipe.id == recipe_id_for_deletion).one()
       
       print("\nWARNING: You are about to delete the following recipe: ")
       print(recipe_to_be_deleted)
# Confirm with the user he wants to delete this entry
       deletion_confirmed = input("Are you sure you want to delete this recipe? (y/n): ")

       if deletion_confirmed == "y":
# Delete the corresponding recipe into result 
          session.delete(recipe_to_be_deleted)
# Commits changes made to the final_recipes table
          session.commit()
          print("\nRecipe successfully deleted from the database.")
       else:
          return None

# main_menu() function

def main_menu():
  # Loops until the user decides to type "quit"
  choice = ""
  while(choice != "quit"):
    print("\n======================================================")
    print("\n Main Menu:")
    print("-------------")
    print("Pick a choice:")
    print("   1. Create a new recipe")
    print("   2. Search for a recipe by ingredient")
    print("   3. Update an existing recipe")
    print("   4. Delete a recipe")
    print("   5. View all recipes")
    print("\n   Type 'quit' to exit the program.")
    choice = input("\n Your choice: ")
    print("\n======================================================\n")

    if choice == "1":
      create_recipe()
    elif choice == "2":
      search_by_ingredients()
    elif choice == "3":
      edit_recipe()
    elif choice == "4":
      delete_recipe()
    elif choice == "5":
      view_all_recipes()
    else:
       if choice == "quit":
          print("Good bye\n")
       else:
          print("WARNING... Wrong entry, please try again.")

main_menu()

session.close()