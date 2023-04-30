import csv
from pathlib import Path

input_file = Path("election_data.csv")
output_file = Path("PyPolData.txt")

# Set up variables to store data
total_votes = 0
candidates = []
votes_per_candidate = {}

# Read in CSV file and iterate through rows
with open("election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        # Increment vote count
        total_votes += 1
        
        # Add candidate to list of candidates if not already there
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            votes_per_candidate[candidate_name] = 0
        
        # Increment vote count for candidate
        votes_per_candidate[candidate_name] += 1

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    vote_count = votes_per_candidate[candidate]
    vote_percent = round((vote_count / total_votes) * 100, 3)
    print(f"{candidate}: {vote_percent}% ({vote_count})")
print("-------------------------")
winner = max(votes_per_candidate, key=votes_per_candidate.get)
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
with open("election_results.txt", "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate in candidates:
        vote_count = votes_per_candidate[candidate]
        vote_percent = round((vote_count / total_votes) * 100, 3)
        txtfile.write(f"{candidate}: {vote_percent}% ({vote_count})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")