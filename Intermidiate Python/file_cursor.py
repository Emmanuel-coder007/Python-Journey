with open('example.txt', 'r') as file:
  file.seek(10)  # Move the cursor to the 10th byte
  content = file.read()  # Read from the current cursor position
  print(content)




  # Truncating a file
with open('example.txt', 'a') as file:
  file.truncate(20)  # Limit the file size to 20 bytes
