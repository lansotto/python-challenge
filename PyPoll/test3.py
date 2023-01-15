# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#create lists
ballots = []
dictionary = {"Name":[],"Percent":[],"VoteCount":[]}
unique_list_of_candidates = []
percent = []
vote_count_for_candidate = 0
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
        if row[2] not in unique_list_of_candidates:
          unique_list_of_candidates.append(row[2])
          vote_count_for_candidate[unique_list_of_candidates]=0
        vote_count_for_candidate[unique_list_of_candidates] = vote_count_for_candidate[unique_list_of_candidates]+ 1

          
    
        #Total number of votes cast
    print(f"Total Votes: " ,len(ballots))
    print("-------------------------")
    print