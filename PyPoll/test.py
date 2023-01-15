# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#create lists
ballots = []
candidates = []
candidates_dictionary = {}
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
    print(number_of_votes)
    print(unique_list_of_candidates)
    print(percent)
    print("-------------------------")

    for candidate in candidates_dictionary:
      number_votes = 


    new_dict = {i:[j, k] for i, j, k in zip(unique_list_of_candidates, percent, number_of_votes)}
    print(new_dict)
    voter_output = f"{i}: {j:.3f}% ({k})\n"
    print("-------------------------")


if candidate_name not in candidate_options:

            # Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

        candidate_name = row[2]
