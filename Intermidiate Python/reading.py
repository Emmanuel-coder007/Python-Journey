file = open('example.txt', 'r')

content = file.read()

print('Using read():')
print(content)

#this is how to read the contents of a file using the read() method. It reads the entire content of the file and stores 
# it in the variable content, which is then printed to the console.

line1 = file.readline()  # Read the first line
print(line1, end='')     # Printing the first line

lin2 = file.readline()  # Read the second line
print(lin2, end='.')     # Printing the second line

#To print each line on a single line without adding a '\n' newline character at the end, we use the end='' option in the print() function.


#The .readlines() method lets you read all lines in a list:
lines = file.readlines()

for line in lines:
  print(line, end='')