    # Import the module  to allow for Python to be able to use across machine operating systems
import os

# Import the module to read csv files in the program
import csv

#from csv import DictReader
# Initialize dictionary to lists to be used to hold values during the program
politician_info = {}

# Lists within the dictionary
voter_id = []
county = []
candidate = []

# Set up the path to find the .csv file to be used with the program.
csvpath = os.path.join("Resources", "election_data1.csv")

with open(csvpath, 'r') as csvfile:
    #  CSV  reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        csvreader = csv.DictReader(csvfile, delimiter=",")
    
        politician_info = {
            voter_id.append(row[0]),
            county.append(row[1]),
            candidate.append(row[2])
            }
    print(voter_id + county + candidate)


