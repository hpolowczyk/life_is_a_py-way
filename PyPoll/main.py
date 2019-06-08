# PyPoll Assignment 

#Modules
import os
import csv

# Set path for file
elec_path = os.path.join("..", "PyPoll", "election_data.csv")
# Set empty candidate list
candidate = []

# Open the CSV
with open(elec_path, newline="", encoding="utf8") as elec_file:
    csv_reader = csv.reader(elec_file, delimiter=",")
    csv_header=next(csv_reader)
    # Create list of 
    for row in csv_reader:
       candidate.append(row[2])
    
    # Determine unique canditates
    cand_list = [cand for cand in set(candidate)]
    # Determine the number of votes per candidate
    vote_total =[candidate.count(i) for i in cand_list]
    # Determine total number of votes
    total_votes = len(candidate)
    # Determine the percentage of votes per candidate
    vote_percent = [round(votes/total_votes,2) for votes in vote_total]
    # Combine number of votes and percentage of votes per candidate in seperate lists
    vote_list = list(zip(vote_total,vote_percent))
    # Create a dictionary with each candidate as a key, and vote_list as its respective values
    cand_dict = dict(zip(cand_list,vote_list))
    # Determine winner by using max
    winner = max(cand_dict,key=cand_dict.get)

print(f"Election Results")
print(f"-----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------------")
print(f"Khan: "+"{:.3%}".format(cand_dict['Khan'][1])+f" ({cand_dict['Khan'][0]})")
print(f"Correy: "+"{:.3%}".format(cand_dict['Correy'][1])+f" ({cand_dict['Correy'][0]})")
print(f"Li: "+"{:.3%}".format(cand_dict['Li'][1])+f" ({cand_dict['Li'][0]})")
print(f"O'Tooley: "+"{:.3%}".format(cand_dict["O'Tooley"][1]) + " ("+ str(cand_dict["O'Tooley"][0]) +")")
print(f"-----------------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------------")

f = open("PyPoll.txt","w")
print(f"Election Results", file=f)
print(f"-----------------------------------", file=f)
print(f"Total Votes: {total_votes}", file=f)
print(f"-----------------------------------", file=f)
print(f"Khan: "+"{:.3%}".format(cand_dict['Khan'][1])+f" ({cand_dict['Khan'][0]})", file=f)
print(f"Correy: "+"{:.3%}".format(cand_dict['Correy'][1])+f" ({cand_dict['Correy'][0]})", file=f)
print(f"Li: "+"{:.3%}".format(cand_dict['Li'][1])+f" ({cand_dict['Li'][0]})", file=f)
print(f"O'Tooley: "+"{:.3%}".format(cand_dict["O'Tooley"][1]) + " ("+ str(cand_dict["O'Tooley"][0]) +")", file=f)
print(f"-----------------------------------", file=f)
print(f"Winner: {winner}", file=f)
print(f"-----------------------------------", file=f)