class Student: 
  def __init__(self, name, year, gpa, enrolled):
    self.name = name
    self.year = year
    self.gpa = gpa
    self.enrolled = enrolled

daniel = Student('Daniel Li', 10, 4.0, True)
#this enables us to create an object of the Student class and initialize 
# its attributes in one line of code

ladybird = Student('Christine McPherson', 12, 4.0, True)
kyle = Student('Kyle Scheible', 12, 3.4, True)

print(vars(ladybird))
print(vars(kyle))

# Output: 
# {'name': 'Christine McPherson', 'year': 12, 'gpa': 4.0, 'enrolled': True}
# {'name': 'Kyle Scheible', 'year': 12, 'gpa': 3.4, 'enrolled': True}