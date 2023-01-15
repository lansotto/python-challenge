# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#create lists
ballots = []
candidates = []

#print the required lines
print("Election Results")
print("-------------------------")

#open csvfile and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
# for rows after header do the following
    for row in csvreader:
        ballots.append(row[0])
        candidates.append(row[2])

#Total number of votes cast
    print(f"Total Votes: " ,len(ballots))
    print("-------------------------")
    set_res = set(candidates)
    list_res = (list(set_res))
    for item in list_res:
        print(item + ": ")
    
    print("-------------------------")
    