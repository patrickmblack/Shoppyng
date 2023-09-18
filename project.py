import json
import inflect
from fpdf import FPDF
import sys

order = [
    "bathroom",
    "medication",
    "cleaning",
    "dairy",
    "eggs",
    "cheese",
    "toiletries",
    "soda",
    "snacks",
    "breakfast",
    "baking",
    "rice",
    "pasta",
    "condiments",
    "frozen",
    "meat",
    "produce"
    ]

grocery_list = dict()  
ingredient_cats = dict()


def main():
  pdf = FPDF(orientation = "P", format = "letter")
  pdf.add_page()
  pdf.set_font("helvetica", "B", 12)
  p = inflect.engine()

  while True:
    try:
        #This is setup for later to add functions to the program
        choice = input("What would you like to do? [List] [Load]\n").lower()

        if choice not in ["list", "load", "ls", "ld"]:
           print("Please choose an option")
           continue
        elif choice == "list" or choice == "ls":
          cat_dict, ing_dict = load_recipes()
          sorted_dict = sort_ingredients(cat_dict)
          for i in sorted_dict.keys():
            qty_to_buy = ing_dict[i]
            item_to_buy = i
            pdf.cell(0, 10, f"[   ] {qty_to_buy} {p.plural(item_to_buy, qty_to_buy)}", new_x = "LMARGIN", new_y = "NEXT")
            print("[ ]", qty_to_buy, "", p.plural(item_to_buy, qty_to_buy))

            

          pdf.output("Grocery List.pdf")
          sys.exit()
        
        elif choice == "load" or choice == "ld":
           filename = input("Filename.csv: ")
           if load_from_csv(filename):
            continue
           else:
              continue

    except KeyboardInterrupt:
       sys.exit()
    break
  sys.exit()

def load_recipes():
  with open("recipes.json") as json_recipes:
      all_recipes = json.load(json_recipes)

  while True:
    try:

      time_options = list()
      meal_options = list()

      for times in all_recipes:
        time_options.append(times)

      print(time_options)

      chosen_time = input("[CTRL+Z to quit]\nCategory choice: ").lower()
      for recipe_names in all_recipes[chosen_time]:
        meal_options.append(recipe_names['recipe_name'])
      
      print(meal_options)

      chosen_meal = input("Option choice: ").lower()
      meal_index = meal_options.index(chosen_meal)

      for recipe_choice in all_recipes[chosen_time][meal_index]['ingredients']:
        ingredient_current = recipe_choice['ing_name']
        ingredient_qty = recipe_choice['quantity']
        ingredient_cat = recipe_choice['category']


        add_to_category(ingredient_cat, ingredient_current)
        add_to_list(ingredient_current, ingredient_qty)
      
      continue

    except EOFError:
        return ingredient_cats, grocery_list
        break
    except:
       continue

def add_to_category(item, cat):
    if item not in ingredient_cats:
       ingredient_cats[cat] = item
    
    #return ingredient_cats

def add_to_list(item, qty):
    if item in grocery_list:
       grocery_list[item] += qty
    else:
       grocery_list[item] = qty

    #return grocery_list


def sort_ingredients(dict_with_categories):
    #print(dict_with_categories)

    custom_key = lambda x: order.index(x[1])

    new_sorted_dict = dict(sorted(dict_with_categories.items(), key = custom_key))
    #print(new_sorted_dict)
    return new_sorted_dict

def load_from_csv(filename):
   try:
    with open(filename) as csv_list:
        for line in csv_list:
          if "#" not in line:
              category, itm = line.rstrip().split(',')
              add_to_category(itm, category)
              add_to_list(category, 1)
    print("Items added")
    return True
   except FileNotFoundError:
      print("File not found")
      return False
            

if __name__ == "__main__":
    main()