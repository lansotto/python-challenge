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
    from collections import Counter
    summary = Counter(candidates)
    number_of_votes = list(summary.values())
    percent = []
    for item in number_of_votes:
      percent.append(item/len(ballots))

    
    unique_list_of_candidates = list(summary.keys())
    #print(number_of_votes)
    #print(unique_list_of_candidates)
    #print(percent)
    #print("-------------------------")
    new_dict = {i:[j, k] for i, j, k in zip(unique_list_of_candidates, percent, number_of_votes)}
    print(new_dict)

    print("-------------------------")
    max_value = max(number_of_votes)
    index = number_of_votes.index(max_value)
    print(index)
    
