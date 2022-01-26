# The data we need to retrieve
# 1.Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Total number of votes each candidate received
# 4. Percentage of votes each candidate won
# 5. The winner of the election based on popular vote

# Assign a variable for the file to load and the path.
import csv


file_to_load = 'Resources/election_results.csv'

candidates = {}
winnercount = 0
winnername = ""
# Open the election resu1lts and read the file.
with open(file_to_load, 'r') as csvfile:
    print(csvfile)
    election = csv.reader(csvfile, delimiter=",")
    print(election)
    header = next(election)
    print(header)
    for row in election:
        if row[2] not in candidates:
            candidates[row[2]] = 0
        candidates[row[2]] +=1
        if candidates[row[2]]>winnercount:
            winnercount = candidates[row[2]]
            winnername = row[2]

print(f"The winner is : {winnername} votes {winnercount}")
print(candidates)

