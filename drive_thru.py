# Write code below 💖
def main():
  welcome()
  value = int(input('What do you want to order: '))

  get_item(value)

def welcome():
  print('''Here is your menu:\n
    1. 🍔 Cheeseburger
    2. 🍟 Fries 
    3. 🥤 Soda 
    4  🍦 Ice Cream 
    5. 🍪 Cookie''')

def get_item(value):
  if value == 1:
      print('🍔 Cheeseburger')
  elif value == 2:
    print('🍟 Fries')
  elif value == 3:
    print('🥤 Soda')
  elif value == 4:
    print('🍦 Ice Cream')
  else:
    print('🍪 Cookie')
  
main()
