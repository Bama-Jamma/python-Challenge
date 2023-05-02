import csv
from pathlib import Path

input_data = Path("resources/election_data.csv")
output_data = Path("analysis/PyPolData.txt")

# Set up variables to store data
voter_totals = 0
candidateslist = []
votes_per_candidate_totals = {}

# Read in CSV file and iterate through rows
with open(input_data) as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        # Increment vote count
        voter_totals += 1
        
        # Add candidate to list of candidateslist if not already there
        candidate_name = row[2]
        if candidate_name not in candidateslist:
            candidateslist.append(candidate_name)
            votes_per_candidate_totals[candidate_name] = 0
        
        # Increment vote count for candidate
        votes_per_candidate_totals[candidate_name] += 1

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voter_totals}")
print("-------------------------")
for candidate in candidateslist:
    vote_count = votes_per_candidate_totals[candidate]
    vote_percent = round((vote_count / voter_totals) * 100, 3)
    print(f"{candidate}: {vote_percent}% ({vote_count})")
print("-------------------------")
winner = max(votes_per_candidate_totals, key=votes_per_candidate_totals.get)
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
with open(output_data, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {voter_totals}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidateslist:
        vote_count = votes_per_candidate_totals[candidate]
        vote_percent = round((vote_count / voter_totals) * 100, 3)
        txtfile.write(f"{candidate}: {vote_percent}% ({vote_count})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")