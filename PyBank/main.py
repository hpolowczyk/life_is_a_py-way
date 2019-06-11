# PyBank Assignment

# Import modules
import os
import csv

# Set path for file
bdgt_path = os.path.join("..", "PyBank", "budget_data.csv")

# Set empty lists
months = []
p_l = []

# Open the CSV
with open(bdgt_path, newline="", encoding="utf8") as bdgt_file:
    csv_reader = csv.reader(bdgt_file, delimiter=",")
    csv_header=next(csv_reader)
    for row in csv_reader:
        # Put all months into a list
        months.append(row[0])
        # Put all profit/loss values into a list
        p_l.append(int(row[1]))
        # Create a list that determines the difference between two subsequent profit/loss values
        diff = [p_l[i]-p_l[i-1] for i in range(1,len(p_l))]

    # Sum all of the profit/loss values
    total_p_l = sum(p_l)
    # Determine the average of the differences between the profit/loss values
    ave_change = round(sum(diff)/len(diff),2)
    # Determine the largest difference between subsequent profit/loss values
    max_change = max(diff)
    # Determine the smallest difference between subsequent profit/loss values
    min_change = min(diff)
    # Determine the month where the largest difference occurs
    max_month = months[diff.index(max_change) + 1]
    # Determine the month where the smallest difference occurs
    min_month = months[diff.index(min_change) + 1]

# To print in Terminal
print(f"Financial Analysis")
print(f"-----------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total_p_l}")
print(f"Average Change: ${ave_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

# To print in seperate .txt file named PyBank
f = open("PyBank.txt","w")
print(f"Financial Analysis", file=f)
print(f"-----------------------------------", file=f)
print(f"Total Months: {len(months)}", file=f)
print(f"Total: ${total_p_l}", file=f)
print(f"Average Change: ${ave_change}", file=f)
print(f"Greatest Increase in Profits: {max_month} (${max_change})", file=f)
print(f"Greatest Decrease in Profits: {min_month} (${min_change})", file=f)