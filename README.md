# Shoppyng

#### Video Demo: https://youtu.be/qCib3G8_r6Q

#### Description

Shoppyng is a grocery list generator. CSV files of items and their categories can be loaded, in addition to choosing premade meals. The program will output the organized list and generate a PDF to print. The organization can be modified by changing the "order" list at the top of the program

##### project.py
This python file is the main program that parses all the items and outputs the organized list. The user is prompted for their desired action; create a List, or Load a file.

##### Load
Prompts the user for a csv file to load. Ignoring commented lines, separates items into a dictionary containing the item itself as the key, and its category as it's value.

##### List
Creating a list from predetermined recipes in the JSON file. Reads through the collections and loads those as the category options; such as breakfast or dinner. Choosing a category then dives into specific collection and loads all the documents and their names. Choosing a specific document loads the collection of ingredients under the item and adds them to the correct dictionary.

##### Final output
Two dictionaries are created; One for items and their category, the other for items their quantity. The category dictionary is sent to a function to be rearranged based on the "order" list at the start. This sorted list is sent to the final output; one by one each item is pulled from the sorted category dictionary and used as the key to take out the quantity required. This is both printed to console, as well as added as a new line to a PDF. 

##### recipes.json

List of recipes that can be quickly loaded and their ingredients and quantity added to the final dictionaries. Collections are sorted by category, such as time of day for the meal. Within each collection are the recipes themselves. Within the recipe, is the list of ingredients, the quantity required, and the category that it is in to be sorted when generating the list. 

I found a github repo of recipes in JSON format that I used as inspiration for laying out my own recipes. https://github.com/kodecocodes/recipes/blob/master/Recipes.json

##### list.csv

A more simple way to add items to the generator. In any order items and their categories can be added, each on their own line. Comments are ignored. 


#### Decisions

JSON was chosen for the recipes, because it was the more straightforward way I could find to parse through groups of items and extract them as needed. 

CSV file was used for a straightforward list, more similar to a list I would create on paper or Google Keep. CSV is easier to parse quickly, as well as write down as a person. I could open a CSV on my phone and quickly write down an item I need with little formatting required.

FPDF Is used to generate the final PDF that can be easily printed or shared. This was used for CS50P Week 9 and was a nice addition so I can print the final list.

The reason I created this program is to assist the creation of my grocery list and organize it how I like to shop. I'm a very linear shopper, going in a route around the store to pick everything; I dislike when a list needs to be sorted through to find all the produce first, then all the meats, and oh yea you actually need more fruit, now onto canned goods...
