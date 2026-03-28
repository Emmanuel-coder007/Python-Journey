# Write code below 💖
import random
fruits = ['🍒', '🍇', '🍉', '7️⃣']
results = []
status = True
def play():
  global results
  results = random.choices(fruits, k=3)
  print(results[0] + ' | ' + results[1] + ' | ' + results[2])

while status == True:
  play()
  if results == ['7️⃣', '7️⃣', '7️⃣']:
      print("Jackpot!  💰")
      status = False
  else:
    print("Thank you for playing")
    ans = input("Do you wish to continue?\nY or N\n")
    if ans == 'N':
      status = False
    
 