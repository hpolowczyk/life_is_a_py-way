# PyBank Assignment

#Modules
import os
import csv

# Set path for file
bdgt_path = os.path.join("..", "PyBank", "budget_data.csv")

months = []
p_l = []

# Open the CSV
with open(bdgt_path, newline="", encoding="utf8") as bdgt_file:
    csv_reader = csv.reader(bdgt_file, delimiter=",")
    csv_header=next(csv_reader)
    for row in csv_reader:
        months.append(row[0])
        p_l.append(int(row[1]))
        diff = [p_l[i]-p_l[i-1] for i in range(1,len(p_l))]

    total_p_l = sum(p_l)
    ave_change = round(sum(diff)/len(diff),2)
    max_change = max(diff)
    min_change = min(diff)
    max_month = months[diff.index(max_change) + 1]
    min_month = months[diff.index(min_change) + 1]

print(f"Financial Analysis")
print(f"-----------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${total_p_l}")
print(f"Average Change: ${ave_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

f = open("Pybank.txt","w")
print(f"Financial Analysis", file=f)
print(f"-----------------------------------", file=f)
print(f"Total Months: {len(months)}", file=f)
print(f"Total: ${total_p_l}", file=f)
print(f"Average Change: ${ave_change}", file=f)
print(f"Greatest Increase in Profits: {max_month} (${max_change})", file=f)
print(f"Greatest Decrease in Profits: {min_month} (${min_change})", file=f)



    


    


