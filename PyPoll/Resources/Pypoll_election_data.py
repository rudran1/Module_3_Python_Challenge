import os, csv
from pathlib import Path 

filepath = os.path.join('.', 'Resources', 'election_data.csv')

total_votes = 0 
Charles_Casper_Stockham_votes = 0
Diana_DeGette_votes = 0
Raymon_Anthony_Doane_votes = 0

with open(filepath, newline='') as elections:

    csvreader = csv.reader(elections,delimiter=",") 

    header = next(csvreader)     

    for row in csvreader: 

        total_votes +=1

        if row[2] == "Charles Casper Stockham": 
            Charles_Casper_Stockham_votes +=1
        elif row[2] == "Diana DeGette":
            Diana_DeGette_votes +=1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane_votes +=1

candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes = [Charles_Casper_Stockham_votes, Diana_DeGette_votes,Raymon_Anthony_Doane_votes]


dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

Charles_Casper_Stockham_percent = (Charles_Casper_Stockham_votes/total_votes) *100
Diana_DeGette_percent = (Diana_DeGette_votes/total_votes) * 100
Raymon_Anthony_Doane_percent = (Raymon_Anthony_Doane_votes/total_votes)* 100


print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Charles_Casper_Stockham: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
print(f"Diana_DeGette: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
print(f"Diana_DeGette: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")


output_file = os.path.join('.', 'Resources',"Election_Results_Summary.txt")

with open(output_file,"w") as file:

    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {Charles_Casper_Stockham_percent:.3f}% ({Charles_Casper_Stockham_votes})")
    file.write("\n")
    file.write(f"Correy: {Diana_DeGette_percent:.3f}% ({Diana_DeGette_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {Raymon_Anthony_Doane_percent:.3f}% ({Raymon_Anthony_Doane_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")