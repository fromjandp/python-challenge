    # Import the module  to allow for Python to be able to use across machine operating systems
import os

# Import the module to read csv files in the program
import csv

# Initialize dictionary to lists to be used to hold values during the program
politician_info = {}

# Lists within the dictionary
voter_id = []
county = []
candidate = []
k = str("Khan")



# Variables to calculate totals
candidate_name = str (" ")
total_votes = int(0)
khan_total_votes = int(0)
correy_total_votes = int(0)
li_total_votes = int(0)
otooley_total_votes = int(0)


# Set up the path to find the .csv file to be used with the program.
csvpath = os.path.join("Resources", "election_data1.csv")

with open(csvpath, 'r') as csvfile:
    #  CSV  reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        csvreader = csv.DictReader(csvfile, delimiter=",")
        # load up the dictionary of lists    
        politician_info = {
            voter_id.append(row[0]),
            county.append(row[1]),
            candidate.append(row[2])
        }
        # total number of votes
        total_votes = len(voter_id) - 1
        for name in candidate:
            candidate_name = name    
            if candidate_name =="Khan" :
                khan_total_votes =+ 1
                print("K= " + str(khan_total_votes))
            elif candidate_name == "Correy" :
                    correy_total_votes =+ 1
                    print("C = " + str(correy_total_votes))
            elif candidate_name == "Li" :dir
                    li_total_votes =+ 1
                    print("L = " + str(li_total_votes))
            else:
                if candidate_name == "O'Tooley" :
                    otooley_total_votes =+ 1   
                    print("O = " + str(otooley_total_votes))     

      
        

# Print the results to the screen
print(f'Election Results')
print(f'--------------------------------')
print(f'Total Votes: {total_votes}')  
print(f'--------------------------------')
print(f'--------------------------------')
print(f'--------------------------------')
    
