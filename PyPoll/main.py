import csv
import os
from collections import Counter

# Read data from file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

# Calculate the total number of votes cast
total_votes = len(data)

# Create a list of candidates who received votes
candidates = [row['Candidate'] for row in data]

# Count the votes for each candidate
vote_counts = Counter(candidates)

# Calculate the percentage of votes each candidate won
vote_percentages = {candidate: (count / total_votes) * 100 for candidate, count in vote_counts.items()}

# Find the winner of the election based on popular vote
winner = max(vote_counts, key=vote_counts.get)

# Print results to console
print(f'Election Results')
print(f'-------------------------')
print(f'Total Votes: {total_votes}')
print(f'-------------------------')
for candidate, count in vote_counts.items():
    print(f'{candidate}: {vote_percentages[candidate]:.3f}% ({count})')
print(f'-------------------------')
print(f'Winner: {winner}')
print(f'-------------------------')

# Export the output of the terminal to a txt file in the 'Analysis' folder.
# The \n dictates where a new line should begin in the output.
outpath = os.path.join("Analysis", "eleciton_analysis.txt")
with open(outpath, 'w') as file:
    file.write(f'Election Results\n')
    file.write(f'-------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write(f'-------------------------\n')
    for candidate, count in vote_counts.items():
        file.write(f'{candidate}: {vote_percentages[candidate]:.3f}% ({count})\n')
    file.write(f'-------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write(f'-------------------------\n')