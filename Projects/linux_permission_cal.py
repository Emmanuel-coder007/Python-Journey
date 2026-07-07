
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

un_codes = {"rwx": "7", "rw-": "6", "r-x": "5", "r--": "4", "-wx": "3", "-w-": "2", "--x": "1", "---": "0"}
user_permission = ""

for i in range(len(answer)):
    for key, value in un_codes.items():
        if answer[i:i+3] == key:
            user_permission += value
            i += 2
            break

print(answer)
print("The permission in octal format is: " + user_permission)