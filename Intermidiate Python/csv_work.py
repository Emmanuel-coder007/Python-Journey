import csv
#this functions sucessfully
# converts a string to a float, and if it fails, 
# it returns 0.0 instead of throwing an error.
def convert_to_float(value): 
    try:
        return float(value)
    except ValueError:
        return 0.0

# or use csv_file.readline() to skip the first row 
sales = 0
# Open the CSV file in 'read' mode with UTF-8 encoding
with open('Bestseller.csv', 'r', encoding='utf8') as file:
    # Create a CSV reader object
#    file.readline() # to skip the header row
    csv_reader = csv.reader(file)
    # to also skip the header row
    #next(csv_reader)
    

    for row in csv_reader:
#        print(row)
        if convert_to_float(row[-2]) > sales:
            sales = convert_to_float(row[-2])
        else:
            continue
print(sales)






# Data to be written to the CSV file
data_to_write = [
  ['Name', 'Age', 'Grade'],
  ['Alice', 25, 'A'],
  ['Bob', 22, 'B'],
  ['Charlie', 28, 'A+']
]

with open('Bestseller_info.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data_to_write)