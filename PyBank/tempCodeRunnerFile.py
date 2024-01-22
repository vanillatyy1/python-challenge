import os
import csv

#"../Resources/budget_data.csv""..",
pybank_csv = os.path.join("Resources","budget_data.csv")

# Open and read csv
with open (pybank_csv) as csv_file:
    csv_reader = csv.reader (csv_file,delimiter=",")

print(csvreader)