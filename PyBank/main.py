# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

print("Financial Analysis")
print("----------------------------")


months_included = []
list_of_profits = []
change_in_profit_loss = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    for row in csvreader:
        months_included.append(row[0])
        list_of_profits.append(row[1])
        change_in_profit_loss = [list_of_profits[i:i+2] for i in range(0, len(list_of_profits),2)]
    #The total number of months included in the dataset
    length_of_list = len(months_included)
    print("Total Months: ",length_of_list)
    

    #The net total amount of "Profit/Losses" over the entire period

    total = 0
    for number in list_of_profits:
        total += float(number)
    total 
    
    print("Total: ","${:.0f}".format(total))

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print(change_in_profit_loss)
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period