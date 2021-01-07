# Import the  nodule  to allow for Python to be able to use across machine operating systems
import os

# Import the Module to read csv files in the program
import csv

# Initialize the lists to be used to hold values during the program
months = []

# pnl stands for profit_n_loss
pnl = []

# Set up the path to find the .csv file to be used with the program.
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

with open(csvpath, 'r') as csvfile:
    #   CSV  reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first to identify the layout of the file.
    csv_header = next(csvreader)

    #  Read each row of data after the header
#  initialize variables to hold calculations and output totals.
    
    total_months = int(0)
    total = 0
    
    net_total = float(0)
    total_net_pnl = float(0)
    total = float(0)
    average_change = float(0)
    greatest_increase = int(0)
    greatest_decrease = int(0)

    # Read the input file 'budget_data.csv' and process.
    for row in csvreader:
        total = round(total +  int(row[1]))

        # Accumulate the dates in an array called 'months'
        months.append(row[0])

        # Accumulate the profit/loss values, for the total in a list called 'pnl'.
        pnl.append(row[1])

        pnl.append(row[1])

        # Accumulate the number of months in the dataset.
        total_months += 1

        # Accumulate the net total amount of "Profit/Loss" over the entire period.
        #  net_total = net_total + row[1]


# Print out the totals
print(f'Financial Analysis')
print(f'-----------------------------total_months-----------------')
print(f'Total Months: {total_months}')
print(f'Total: {total}')
print(f'Average Change: ')
print(f'Greatest Increase in Profits: ')

print(f'Greatest Decrease in profits')
