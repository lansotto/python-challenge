# Modules
import os
import csv
# Set path for file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

print("Financial Analysis")
print()
print("----------------------------")
print()
#create lists
months_included = []
list_of_profits = []
change_in_profit_loss = []

#open csvfile and read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    # for rows after header do the following
    for row in csvreader:
        months_included.append(row[0])
        list_of_profits.append(row[1])
        new_list = list_of_profits[1:len(list_of_profits)]
        difference = [float(new_list[i])-float(list_of_profits[i]) for i in range(min(len(list_of_profits), len(new_list)))]
        
    #The total number of months included in the dataset
    length_of_list = len(months_included)
    print("Total Months: ", length_of_list)
    print()
    
    #The net total amount of "Profit/Losses" over the entire period
    total = 0
    for number in list_of_profits:
        total += float(number)
    total 
    print("Total: ","${:.0f}".format(total))
    print()
    

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
    print("Average Change: ","${:+.2f}".format(sum(difference) / len(difference)))
    print()
#The greatest increase in profits (date and amount) over the entire period
    month_of_greatest_increase = months_included[difference.index(max(difference))+1]
    print("Greatest Increase in Profits: ", month_of_greatest_increase, "({})".format("${:-.0f}".format(max(difference))))
    print()
# The greatest decrease in profits (date and amount) over the entire period
    month_of_greatest_decrease = months_included[difference.index(min(difference))+1]
    print("Greatest Decrease in Profits: ", month_of_greatest_decrease, "({})".format("${:-.0f}".format(min(difference))))
    print()
#Export results as text file
    line3 = "Total Months: " + str(length_of_list)
    line4 = "Total: " + str("${:.0f}".format(total))
    line5 = "Average Change: " + str("${:+.2f}".format(sum(difference) / len(difference)))
    line6 = "Greatest Increase in Profits: " + str(month_of_greatest_increase) + " " + str("({})".format("${:-.0f}".format(max(difference))))
    line7 = "Greatest Decrease in Profits: " + str(month_of_greatest_decrease) + " " + str("({})".format("${:-.0f}".format(min(difference))))

    output_path = os.path.join("..", "PyBank", "analysis", "results.txt")
    with open(output_path, 'w') as textfile:
        textfile.write("Financial Analysis\n")
        textfile.write("\n")
        textfile.write("----------------------------\n")
        textfile.write("\n")
        textfile.write(line3+"\n")
        textfile.write("\n")
        textfile.write(line4+"\n")
        textfile.write("\n")
        textfile.write(line5+"\n")
        textfile.write("\n")
        textfile.write(line6+"\n")
        textfile.write("\n")
        textfile.write(line7+"\n")