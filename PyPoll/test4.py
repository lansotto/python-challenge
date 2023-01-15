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
print()
print("-------------------------")
print()

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
    print()
    print("-------------------------")
    print()

    #get list of total votes per candidate
    from collections import Counter
    summary = Counter(candidates)
    number_of_votes = list(summary.values())

    percent = []
    for item in number_of_votes:
      percent_of_vote = round(item/len(ballots)*100,3)
      percent.append(f'{percent_of_vote}%')
 
    #calculate the winner by creating a list of unique candidates by removing duplicates
    unique_list_of_candidates = list(summary.keys())

    #find the largest value from the list of votes
    max_value = max(number_of_votes)
    voteindex = number_of_votes.index(max_value)
    last_text = ("Winner: " + unique_list_of_candidates[voteindex])
   


    ziplist = zip(unique_list_of_candidates, percent, number_of_votes)
    for unique_list_of_candidates in ziplist:
        print(unique_list_of_candidates)
    
    print()
    print("-------------------------")
    print()
    print(last_text)
    print()
    print("-------------------------")

    
    
