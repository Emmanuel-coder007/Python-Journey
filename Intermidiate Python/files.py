file = open('example.txt', 'w')

file.write('Hello, world!\n')


lines = ['This is a line.\n', 'This is the next line.\n']
file.writelines(lines)