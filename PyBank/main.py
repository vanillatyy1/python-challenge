#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period        
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period


#import and read csv script adapted from Python 3rd clss - 01-Evr_CerealCleaner
import os
import csv

# Path to the CSV file
pybank_csv = os.path.join('Resources', 'budget_data.csv')

# Open and read csv
with open(pybank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

# Read and print CSV header #print just to make sure the reading csv part is working
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

# Initialize variables for analysis
    total_month = 0
    total_amount = 0
    max = 0
    min = 0
    previous = 0
    total_change = 0

    for x in csv_reader: # Iterate over the rows in the CSV file (skipping the header)
         total_month += 1 #Add the total number of months by 1
        # Convert the second column to an integer and add it to the total. It can also be written like this #total_amount =int(x[1])+total_amount
         total_amount += int(x[1])

        # Calculate the change in profit/loss from the previous month
         if previous == 0:
             previous = int(x[1])
         change = int(x[1])-previous
         total_change = total_change+change
         previous = int(x[1])

        # Determine the greatest increase in profits
         if change > max:
            max = change
            max_date = x[0]

         # Determine the greatest decrease in profits
         if change < min:
            min = change
            min_date = x[0]

# Calculate the average change in profit/loss           
average = round(float(total_change/(total_month-1)),2)

# Print the financial analysis on the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_amount}")
print(f"Averge Change: ${average}")
print(f"Greatest Increase in Profits: {max_date} (${max})")
print(f"Greatest Decrease in Profits: {min_date} (${min})")

# Specify the file to write to
output_path = os.path.join('Analysis', 'pybank_result_1.txt')

# Open the file using "write" mode, and write the information to the file
with open(output_path, 'w') as text:
        text.write("Financial Analysis\n")
        text.write("----------------------------\n")
        text.write(f"Total Months: {total_month}\n")
        text.write(f"Total: ${total_amount}\n")
        text.write(f"Average Change: ${average}\n")
        text.write(f"Greatest Increase in Profits: {max_date} (${max})\n")
        text.write(f"Greatest Decrease in Profits: {min_date} (${min})\n")

#referenced https://www.pythontutorial.net/python-basics/python-write-text-file/ for text.write
