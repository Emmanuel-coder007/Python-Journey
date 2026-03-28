import random, maths #you can import multiple modules in one line by separating them with a comma

dice = [1, 2, 3, 4, 5, 6]

print(random.choices(dice))
#randomly selects an item from the list and returns it as a list

print(random.choices(dice, k=3))
#randomly selects 3 items from the list and returns them as a list


