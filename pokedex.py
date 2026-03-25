# Write code below 💖
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f"{self.name}\n{self.name}")
  
  def display_details(self):
    print(f"""Entry Number: {self.entry}
Name: {self.name} 
Type: {self.types}
Description: {self.description}""")


Pikachu = Pokemon(1, 'Pikachuu', 'Lightening', 'Small but mighty animal for war', True)

Pikachu.speak()
Pikachu.display_details()