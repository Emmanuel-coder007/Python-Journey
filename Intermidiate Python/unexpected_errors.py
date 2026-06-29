import unittest
import math
# Passing a non-string will raise a TypeError
#with self.assertRaises(TypeError):
#  self.assertIn('World', 123)

#The .assertRaises() method works as a code block started by the with keyword. 
# Inside the block, we can write tests that might raise an error, such as a TypeError. 
# In this example, the code trying to check if the string 'World' is inside 123. 
# Since 123 is a number, not a string, Python will raise a TypeError.



def get_sqrt(n):
  return math.sqrt(n)

def divide(a, b):
  return a / b

class TestMathFunctions(unittest.TestCase):
    def test_get_sqrt(self):
        self.assertEqual(get_sqrt(144), 12)
        
        with self.assertRaises(ValueError):
            self.assertEqual(get_sqrt(-144))

    def test_divide(self):
        self.assertEqual(divide(144, 12), 12)

        with self.assertRaises(ZeroDivisionError):
            self.assertEqual(divide(144, 0))