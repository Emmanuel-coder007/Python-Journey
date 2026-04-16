#You can also use a with block to open a file, handle it, and close it automatically:
with open('filename', 'r') as f:
  # handle file here
    f.write('This is a line.\n')
    f.write('This is the next line.\n')

#No .close() method necessary!