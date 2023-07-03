import os
import csv
from collections import Counter
#Path to collect data from Resources folder.  Name new variable for code
electiondata_csv = os.path.join("Resources/election_data.csv")

#open file
with open(electiondata_csv, encoding="utf") as electiondata:
    #csv reader to specify delimiter and variables
    electiondatar = csv.reader (electiondata, delimiter=",")
    #account for the header row
    header = next(electiondatar, None)

    #set the variables
    votescount = 0
    candidatescount = 0
    candidatesvotes = []
    # set value for a set of data to acumulate the unique values
    candidates = set()  #information from documentation https://www.geeksforgeeks.org/python-set-method/
    
    for row in electiondatar:
        # count the number of votes
        votescount +=1
        
        # complete list of candidates who receive a vote
        #define candidate row and variable candidate
        candidate = row[2]
        #add names to the set
        candidates.add(candidate)
        #append candidates to count votes
        candidatesvotes.append(candidate)

    #count the number of candidates
    numberofcandidates = len(candidates) 

#count the number of votes per candidate using counter 
#information from documentation  https://www.digitalocean.com/community/tutorials/python-counter-python-collections-counter     
candidatesvotescount = Counter(candidatesvotes)       

#print results
single_string = f"""
Election results

----------------------------

Total votes: {str(votescount)}

----------------------------

"""

#calculate the percentage of votes per candidate
for candidate, count in candidatesvotescount.items():
    percentage = (count/votescount)*100
    candidateinformation = f"{candidate}: {percentage:.3f}% ({count})\n\n"
    single_string += candidateinformation

#add the winner of the elections
winnercandidate = candidatesvotescount.most_common(1)[0][0]
winnercandidateresult = f"----------------------------\nWinner: {winnercandidate}\n----------------------------\n"
#add the winner results to the single string
single_string += winnercandidateresult

print (single_string)

electionstxt_path = "analysis/electionsresults.txt"
with open(electionstxt_path,"w") as file:
    file.write(single_string)
