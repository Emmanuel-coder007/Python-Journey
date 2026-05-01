file_path = "diary.txt"

try:
    file = open(file_path, 'r')
finally:
    file.close() # Ensures file close even if an exception occurs

with open(file_path, 'r') as file:
    content = file.read()
    print(content)
    # Reading from a file using read() method