# Write code below 💖

class restaurants:
  name = ''
  category = ''
  rating = 0.0
  delivery = bool

  #objects are an instance of a class
  #a class is a blueprint for creating objects

  #to create an object, we call the class as if it were a function
shop1 = restaurants() #this is an object of the restaurant class
shop1.name = 'Pizza Hut'
shop1.category = 'Fast Food'  
shop1.rating = 4.5
shop1.delivery = True

print(vars(shop1)) #vars() is a built-in function that returns the __dict__ 
#attribute of an object, which is a dictionary containing all the attributes 
# #of the object and their values
# Output: {'name': 'Pizza Hut', 'category': 'Fast Food', 'rating': 4.5, 'delivery': True}

#------------------------------------------------------------------------------------------
#exerecise example
  # Write code below 💖

class restaurant:
  name = ''
  category = ''
  rating = 0
  delivery = bool

bobs_burgers = restaurant()
bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

kfc = restaurant()
kfc.name = 'KFC'
kfc.category = 'Fast food'
kfc.rating = 5.0
kfc.delivery = True

king_burgers = restaurant()
king_burgers.name = 'King\'s Burger'
king_burgers.category = 'Fast Food'
king_burgers.rating = 5.0
king_burgers.delivery = True

print(vars(bobs_burgers))
print(vars(kfc))
print(vars(king_burgers))
