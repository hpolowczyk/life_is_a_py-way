# PyPoll Assignment 

# Import modules
import os
import csv

# Set path for file
elec_path = os.path.join("..", "PyPoll", "election_data.csv")

# Set empty candidate votes list
candidate_votes = []

# Open the CSV
with open(elec_path, newline="", encoding="utf8") as elec_file:
    csv_reader = csv.reader(elec_file, delimiter=",")
    csv_header=next(csv_reader)
    for row in csv_reader:
       # Put all candidate votes into a list
       candidate_votes.append(row[2])
    
    # Determine unique canditates
    candidate_list = [candidate for candidate in set(candidate_votes)]
    # Determine the number of votes per candidate
    votes_per_cand =[candidate_votes.count(vote) for vote in candidate_list]
    # Determine total number of votes
    total_votes = len(candidate_votes)
    # Determine the percentage of votes per candidate
    vote_percent = [round(votes/total_votes,2) for votes in votes_per_cand]
    # Combine number of votes and percentage of votes per candidate in seperate lists
    vote_list = list(zip(votes_per_cand,vote_percent))
    # Create a dictionary with each candidate as a key, and vote_list as its respective values
    candidate_dict = dict(zip(candidate_list,vote_list))
    # Determine winner by using max
    winner = max(candidate_dict, key=candidate_dict.get)

# To print in Terminal
print(f"Election Results")
print(f"-----------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------------")
print(f"Khan: "+"{:.3%}".format(candidate_dict['Khan'][1])+f" ({candidate_dict['Khan'][0]})")
print(f"Correy: "+"{:.3%}".format(candidate_dict['Correy'][1])+f" ({candidate_dict['Correy'][0]})")
print(f"Li: "+"{:.3%}".format(candidate_dict['Li'][1])+f" ({candidate_dict['Li'][0]})")
print(f"O'Tooley: "+"{:.3%}".format(candidate_dict["O'Tooley"][1]) + " ("+ str(candidate_dict["O'Tooley"][0]) +")")
print(f"-----------------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------------")

# To print in seperate .txt file named PyPoll
f = open("PyPoll.txt","w")
print(f"Election Results", file=f)
print(f"-----------------------------------", file=f)
print(f"Total Votes: {total_votes}", file=f)
print(f"-----------------------------------", file=f)
print(f"Khan: "+"{:.3%}".format(candidate_dict['Khan'][1])+f" ({candidate_dict['Khan'][0]})", file=f)
print(f"Correy: "+"{:.3%}".format(candidate_dict['Correy'][1])+f" ({candidate_dict['Correy'][0]})", file=f)
print(f"Li: "+"{:.3%}".format(candidate_dict['Li'][1])+f" ({candidate_dict['Li'][0]})", file=f)
print(f"O'Tooley: "+"{:.3%}".format(candidate_dict["O'Tooley"][1]) + " ("+ str(candidate_dict["O'Tooley"][0]) +")", file=f)
print(f"-----------------------------------", file=f)
print(f"Winner: {winner}", file=f)
print(f"-----------------------------------", file=f)