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
    last_text = "Winner: " + str(unique_list_of_candidates[voteindex])
   
    ziplist = zip(unique_list_of_candidates, percent, number_of_votes)
    for unique_list_of_candidates in ziplist:
        output = (f'{unique_list_of_candidates[0]}: {unique_list_of_candidates[1]} ({unique_list_of_candidates[2]})')
        print(output)
        
        print()
    print("-------------------------")
    print()
    print(last_text)
    print()
    print("-------------------------")

#create txt file and write the same results to it
    output_path = os.path.join("..", "PyPoll", "analysis", "results.txt")
    with open(output_path, 'w') as textfile:
        textfile.write("Election Results\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        textfile.write(line1+"\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        for i in range(len(unique_list_of_candidates)):
            txt.write(f'{unique_list_of_candidates[i]}')
        textfile.write("\n")
        #textfile.write(line3+"\n")
        textfile.write("\n")
        #textfile.write(line4+"\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        textfile.write(last_text+"\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")