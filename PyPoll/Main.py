import csv
from pathlib import Path

input_data = Path("resources/election_data.csv")
output_data = Path("analysis/PyPolData.txt")

# Set up variables to store data
voter_totals = 0
listofallcandidates = []
candidate_individual_votes = {}

# Read in CSV file and iterate through rows
with open(input_data) as csvfile:
    PollData = csv.reader(csvfile)
    header = next(PollData)
    for row in PollData:
        # Increment vote count
        voter_totals += 1
        
        # Add candidate to list of listofallcandidates if not already there
        candidate_name = row[2]
        if candidate_name not in listofallcandidates:
            listofallcandidates.append(candidate_name)
            candidate_individual_votes[candidate_name] = 0
        
        # Increment vote count for candidate
        candidate_individual_votes[candidate_name] += 1

# Print results to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {voter_totals}")
print("-------------------------")
for candidate in listofallcandidates:
    vote_count = candidate_individual_votes[candidate]
    vote_percent = round((vote_count / voter_totals) * 100, 3)
    print(f"{candidate}: {vote_percent}% ({vote_count})")
print("-------------------------")
winner = max(candidate_individual_votes, key=candidate_individual_votes.get)
print(f"Winner: {winner}")
print("-------------------------")

# Export results to text file
with open(output_data, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {voter_totals}\n")
    txtfile.write("-------------------------\n")
    for candidate in listofallcandidates:
        vote_count = candidate_individual_votes[candidate]
        vote_percent = round((vote_count / voter_totals) * 100, 3)
        txtfile.write(f"{candidate}: {vote_percent}% ({vote_count})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")