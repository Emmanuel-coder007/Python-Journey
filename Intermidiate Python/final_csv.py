import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open('Packing_list.csv', 'r', newline="") as file:
        csv_reasder = csv.reader(file)
        for row in csv_reasder:
            print(row)
except FileNotFoundError:
    print("Packaging list not found. Creating a new one.")
    with open('Packing_list.csv', 'w', newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
