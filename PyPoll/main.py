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

# Define names as string for comparison
khan = str("Khan")
correy = str("Correy")
li = str("Li")
otooley = str("O'Tooley")

# Variables to calculate totals
candidate_name = str (" ")
total_votes = int(0)
khan_total_votes = int(0)
correy_total_votes = int(0)
li_total_votes = int(0)
otooley_total_votes = int(0)

kahn_percent = float(0)
correy_percent = float(0)
li_percent = float(0)
otooley_percent = float(0)


# Set up the path to find the .csv file to be used with the program.
csvpath = os.path.join("Resources", "election_data.csv")

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
    # Read through the candidate list and calculate the votes per    
    for name in candidate:
        
        candidate_name = name    
        if name == khan :
            khan_total_votes += 1

        if candidate_name == correy :
            correy_total_votes += 1
        
        if candidate_name == li :
            li_total_votes += 1

        if candidate_name == otooley :
            otooley_total_votes += 1   

    #total number of votes
    total_votes = len(voter_id) - 1

    #  Each candidate's % of total votes
    khan_percent =  (khan_total_votes / total_votes) * 100
    khan_percent =  round(khan_percent,3)
    
    correy_percent =  (correy_total_votes / total_votes) * 100
    correy_percent =  round(correy_percent,3)
    
    li_percent =  (li_total_votes / total_votes) * 100
    li_percent =  round(li_percent,3)

    otooley_percent =  (otooley_total_votes / total_votes) * 100
    otooley_percent =  round(otooley_percent,3) 

# Print the results to the screen
print(f'Election Results')
print(f'--------------------------------')
print(f'Total Votes: {total_votes}')  
print(f'--------------------------------')
print(f'Khan: {khan_percent}%   ({khan_total_votes})')
print(f'Correy: {correy_percent}%   ({correy_total_votes})')
print(f'Li: {li_percent}%      ({li_total_votes})')
print(f"O'Tooley: {otooley_percent}%  ({otooley_total_votes})")
print(f'--------------------------------')
print(f'Winner: ')
print(f'--------------------------------')
    
# Print out to a text file    
# output_file = os.path.join("Analysis", "election_results_analysis.txt")
# with open(output_file, "w") as text_file: 
#         print("Election Results", file=open(output_file, "w"))
#         print("--------------------------------", file=open(output_file, "a"))
#         print("Total Votes", total_votes, file=open(output_file, "a"))
#         print("--------------------------------", file=open(output_file, "a")))
#         print("Khan: ", khan_percent, "%", "(", khan_total_votes,")", file=open(output_file, "a"))
#         print("Correy: ", correy_percent, "%", "(", correy_total_votes,")", file=open(output_file, "a"))
#         print("Li: ", li_percent, "%", "(", li_total_votes,")", file=open(output_file, "a"))
#         print("O'Tooley: ", otooley_percent, "%", "(", otooley_total_votes,")", file=open(output_file, "a"))
#         print("--------------------------------", file=open(output_file, "a"))
#         print("Winner: ", file=open(output_file, "w")) 
#         print("--------------------------------", file=open(output_file, "a"))