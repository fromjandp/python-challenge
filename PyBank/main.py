# Import the module  to allow for Python to be able to use across machine operating systems
import os

# Import the module to read csv files in the program
import csv

# Initialize the lists to be used to hold values during the program
months = []

# pnl stands for profit_n_loss
pnl = []

# Set up the path to find the .csv file to be used with the program.
csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, 'r') as csvfile:
    #   CSV  reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first to identify the layout of the file.
    csv_header = next(csvreader)

    #  Read each row of data after the header
    #  initialize variables to hold calculations and output totals.
    
    total_months = int(0)
    total = 0
    # variables used for calculating the average change
    first_time_through = "false"
    value1 =  int(0)
    value2 =  int(0)
    value_difference = int(0)
    difference_totals = int(0)
    average_change = float(0)

    #variables used for the greatest increase and the greatest decrease
    greatest_increase = int(0)
    greatest_decrease = int(0)

    #variales used to hold the month during which the greatest increate and the greatest decrease occurred
    greatest_increase_month = ""
    greatest_decrease_month = ""

    # Read the input file 'budget_data.csv' and process.
    for row in csvreader:
    
        # Accumulate the dates in an array called 'months'
        months.append(row[0])

        # Accumulate the profit/loss values, for the total in a list called 'pnl'.
        pnl.append(row[0]) 
                
        # Accumulate the number of months in the dataset.
        total_months += 1
        total = total + int(row[1])
    
        if first_time_through == "false":
            # the profit/loss value is needed but there is nothing to compare it to until the next record is read in.
            value1 = int(row[1])
            first_time_through = "true"
        else:
            # old month profit/loss value
            value2 = value1
            #new month profit/loss value
            value1 = int(row[1])
            # subtract old from new to get the change between each month
            value_difference =  value1 -  value2
            # add to total of monthly differences
            difference_totals = difference_totals + value_difference

            # Determine the greatest increase
            if value_difference > greatest_increase:
                greatest_increase = value_difference
                greatest_increase_month = str(row[0])
                                    
            # Determine the greates decrease                        
            if value_difference < greatest_decrease:
                greatest_decrease = value_difference
                greatest_decrease_month = str(row[0])
        
#round to eliminate the decimal point     
total = round(total) 

# calculation for average change from month to month
average_change = difference_totals / (total_months - 1)

#round average_change to 2 decimal places
average_change = round(average_change,2)

# Print out the totals to the display screen
print(f'Financial Analysis') 
print(f'---------------------------')
print(f'Total Months: {total_months}')
print(f'Total: {total}')
print(f'Average Change: {average_change}')
print(f'Greatest Increase in Profits:  {greatest_increase_month} (${greatest_increase})')
print(f'Greatest Decrease in profits:  {greatest_decrease_month} (${greatest_decrease})')


# Print to a text file - Note:  researched on the web and found some in information, on stackoverflow, which makes sense to me.
# https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

output_file = os.path.join("Analysis","budget_data_analysis.txt")
with open("budget_data_analysis.txt", "w") as text_file:  
    print("Financial Analysis", file=open("budget_data_analysis.txt", "w"))
    print("-----------------------------",  file=open("budget_data_analysis.txt", "a"))
    print("Total Months:", total_months, file=open("budget_data_analysis.txt", "a"))
    print("Total:", total, file=open("budget_data_analysis.txt", "a"))
    print("Average Change:", average_change, file=open("budget_data_analysis.txt", "a"))
    print("Greatest Increase in Profits:", greatest_increase_month, "($",greatest_increase,")", file=open("budget_data_analysis.txt", "a"))
    print("Greatest Decrease in Profits:", greatest_decrease_month, "($",greatest_decrease,")", file=open("budget_data_analysis.txt", "a"))
   

