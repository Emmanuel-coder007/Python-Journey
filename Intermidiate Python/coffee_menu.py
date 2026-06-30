
class CoffeeMenu:
  def __init__(self):
    self.menu = {
      'espresso': 2.50,
      'latte': 2.75,
      'cappuccino': 3.20,
      'americano': 2.70
    }
    
  def get_price(self, drink):
    return self.menu.get(drink.lower())

  def add_item(self, drink, price):
    #if drink.lower() in self.menu:
    #raise ValueError(f"{drink} already exists in the menu.")
    self.menu[drink.lower()] = price





   