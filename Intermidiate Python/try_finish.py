try:
    file = open("diary.txt", 'r')
    # Perform operations on the file
finally:
    file.close() # Ensures file close even if an exception occurs
    