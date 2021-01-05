# Import the  nodule  to allow for Python to be able to use across machine operating systems
import os

# Import the Module to read csv files in the program
import csv

# Set up the path to find the .csv file to be used with the programcd ..
csvpath = os.path.join("Resources", "budget_data.csv")
print(csvpath)

with open(csvpath, 'r') as csvfile:
    #   CSV  reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first to identify the layout of the file.
    csv_header = next(csvreader)

#  Read each row of data after the header and print out to verify that you are getting the data.
#  for row in csvreader:
    month_counter = 0
    for row in csvreader:
        month_counter += 1
    print(month_counter)

#
