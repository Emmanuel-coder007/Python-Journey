
print("R for Read\n" 
    "W for Write\n" 
    "X for Execute\n" 
    "- for No Permission\n"
    "Kindly type your choice for User, Group, Others in order of 3 without spaces: ")

def string_checker(string):
    if len(string) != 9:
        return False
    for char in string:
        if char not in ['r', 'w', 'x', '-']:
            return False
    return True

while True:
    answer = input("Enter your choice: ").lower()
    if not string_checker(answer):
        print("Invalid input. Please try again.")
    else:
        print("Valid input.")
        break

user_permission = ""

if answer[0:3] == 'rwx':
    user_permission = "7"
elif answer[0:3] == 'rw-':
    user_permission = "6"   
elif answer[0:3] == 'r-x':
    user_permission = "5"
elif answer[0:3] == 'r--':
    user_permission = "4"
elif answer[0:3] == '-wx':
    user_permission = "3"   
elif answer[0:3] == '-w-':
    user_permission = "2"
elif answer[0:3] == '--x':
    user_permission = "1"
else:
    user_permission = "0"

if answer[3:6] == 'rwx':
    user_permission = user_permission + "7"
elif answer[3:6] == 'rw-':
    user_permission = user_permission + "6"
elif answer[3:6] == 'r-x':
    user_permission = user_permission + "5"
elif answer[3:6] == 'r--':
    user_permission = user_permission + "4"
elif answer[3:6] == '-wx':
    user_permission = user_permission + "3"
elif answer[3:6] == '-w-':
    user_permission = user_permission + "2"
elif answer[3:6] == '--x':
    user_permission = user_permission + "1"
else:
    user_permission = user_permission + "0"

if answer[6:9] == 'rwx':
    user_permission = user_permission + "7"
elif answer[6:9] == 'rw-':
    user_permission = user_permission + "6"
elif answer[6:9] == 'r-x':
    user_permission = user_permission + "5"
elif answer[6:9] == 'r--':
    user_permission = user_permission + "4"
elif answer[6:9] == '-wx':
    user_permission = user_permission + "3"
elif answer[6:9] == '-w-':
    user_permission = user_permission + "2"
elif answer[6:9] == '--x':
    user_permission = user_permission + "1"
else:
    user_permission = user_permission + "0"

print("The permission in octal format is: " + user_permission)