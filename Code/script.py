from trie import Trie
from data import *
from welcome import *
from hashmap import HashMap
from linkedlist import LinkedList

#Printing the Welcome Message
print_welcome()

#Write code to insert food types into a data structure here. The data is in data.py
food_types = Trie()
food_types.make_trie(types)
#Write code to insert restaurant data into a data structure here. The data is in data.py
restaurants = HashMap(len(types))
for restaurant_datum in restaurant_data:
  key, value = restaurant_datum[0], restaurant_datum[1:]
  if not restaurants.has_key(key):
    restaurants.assign(key, LinkedList(value))
  else:
    restaurants.retrieve(key).insert_beginning(value)
#Write code for user interaction here
while True:
  #start the loop by clearing any suggested words
  food_types.reset_words()
  user_input = str(input("\nWhat type of food would you like to eat?\nType the beginning of that food type and press enter to see if it's here, or press 'Enter' with no input to see all options.\n")).lower()
  #Search for user_input in food types data structure here
  res = food_types.return_suggestions(user_input)
  if res == -1:
    print("No other strings found with this prefix\n")
  elif res == 0:
    print("No string found with this prefix\n")
  else:
    if len(food_types.words) > 1:
      print("With those beginning letters, your choices are:\n")
      for word in food_types.words:
        print("- {0}".format(word))
    else:
      food_type = food_types.words[0]
      print("\nThe only option with that beginning letter is {0}. Do you want to look at {0} restaurants?".format(food_type))
      yes_or_no = str(input("Enter 'y' for yes and 'n' for no: "))
  #After finding food type write code for retrieving restaurant data here
      if yes_or_no == 'n':
        continue
      elif yes_or_no == 'y':
        available_restaurants = restaurants.retrieve(food_type).get_head_node()
        print("The {0} restaurants in SoHo are...".format(food_type))
          
        while available_restaurants:
          info = available_restaurants.get_value()
          print("________________________________")
          print("Name: {0}".format(info[0]))
          print("Price: {0}/5".format(info[1]))
          print("Rating: {0}/5".format(info[2]))
          print("Address: {0}".format(info[3]))
          available_restaurants = available_restaurants.get_next_node()
        print("\nDo you want to find other restaurants?")
        yes_or_no = str(input("Enter 'y' for yes and 'n' for no: "))
        if yes_or_no == 'n':
          print("\nThank you for using the this program!")
          break
        elif yes_or_no == 'y':
          continue
