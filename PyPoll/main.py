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
    
    candidate_list = set(candidates)
    candidate_list = (list(set_res))
    for unique_list_of_candidates in list_res:
        print(unique_list_of_candidates)
    
    #print(candidate_list)