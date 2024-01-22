import os
import csv

# Path to the CSV file
pypoll_csv = os.path.join('Resources', 'election_data.csv')

# Open and read csv
with open(pypoll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Print CSV reader object
    print(csv_reader)

# Read and print CSV header
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")