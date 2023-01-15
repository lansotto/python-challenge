# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

#create lists
ballots = []
candidates = []

#print the required lines
print()
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
    line1 = "Total Votes: " + str(len(ballots))
    print(line1)
    print()
    print("-------------------------")
    print()

    #get list of total votes per candidate
    from collections import Counter
    summary = Counter(candidates)
    number_of_votes = list(summary.values())

    #create new list for percentage of popular vote per candidate
    percent = []
    for item in number_of_votes:
      percent_of_vote = round(item/len(ballots)*100,3)
      percent.append(f'{percent_of_vote}%')
 
    #calculate the winner by creating a list of unique candidates by removing duplicates
    unique_list_of_candidates = list(summary.keys())

    #find the largest value from the list of votes
    max_value = max(number_of_votes)
    voteindex = number_of_votes.index(max_value)
    
    #list the candidates, their vote percentage and number of votes
    for i in range(len(unique_list_of_candidates)):
        print(f'{unique_list_of_candidates[i]}: {percent[i]} ({number_of_votes[i]})')
        print()
    print()
    print("-------------------------")
    print()
    last_text = "Winner: " + str(unique_list_of_candidates[voteindex])
    print(last_text)
    print()
    print("-------------------------")


#create txt file and write the same results to it
    output_path = os.path.join("..", "PyPoll", "analysis", "results.txt")
    with open(output_path, 'w') as textfile:
        textfile.write("\n")
        textfile.write("Election Results\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        textfile.write(line1+"\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        for i in range(len(unique_list_of_candidates)):
            textfile.write(f'{unique_list_of_candidates[i]}: {percent[i]} ({number_of_votes[i]})')
            textfile.write("\n")
            textfile.write("\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        textfile.write(last_text+"\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")