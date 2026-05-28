import csv

# Open the CSV file in 'read' mode with UTF-8 encoding
with open('output.csv', 'r', encoding='utf8') as file:
  #Sometimes opening CSV files without specifying an encoding can 
  # cause decoding errors (especially in IDEs)
  # Create a CSV reader object
  csv_reader = csv.reader(file)

  for row in csv_reader:
    print(row)