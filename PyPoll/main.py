import csv
from collections import Counter

# Read data from file
with open('C:/Users/Nathan/Desktop/GitHub Repos/python-challenge/PyPoll/Resources/election_data.csv', 'r') as file:
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

# Export results to text file
with open('C:/Users/Nathan/Desktop/GitHub Repos/python-challenge/PyPoll/Analysis/election_analysis.txt', 'w') as file:
    file.write(f'Election Results\n')
    file.write(f'-------------------------\n')
    file.write(f'Total Votes: {total_votes}\n')
    file.write(f'-------------------------\n')
    for candidate, count in vote_counts.items():
        file.write(f'{candidate}: {vote_percentages[candidate]:.3f}% ({count})\n')
    file.write(f'-------------------------\n')
    file.write(f'Winner: {winner}\n')
    file.write(f'-------------------------\n')