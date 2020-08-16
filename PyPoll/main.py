import os
import csv
from collections import Counter

csv_path = os.path.join('Resources', 'election_data.csv')

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)

    total_votes = 0
    candidates = []
    votes = []
    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        votes.append(row[2])

    candidates_votes = Counter(votes)

print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_votes}')
print('-------------------------')
for key in candidates_votes:
    print(f'{key}: {round(candidates_votes[key] / total_votes * 100, 3)}% ({candidates_votes[key]})')
print('-------------------------')
print(f'Winner: {max(candidates_votes, key = candidates_votes.get)}')
print('-------------------------')

file = open('Analysis/Election_Results.txt', 'w')
file.write('Election Results\n')
file.write('-------------------------\n')
file.write('Total Votes: ' + str(total_votes) + '\n')
file.write('-------------------------\n')
for key in candidates_votes:
    file.write(key + ': ' + str(round(candidates_votes[key] / total_votes * 100, 3)) + '% (' + str(candidates_votes[key]) + ')\n')
file.write('-------------------------\n')
file.write('Winner: ' + str(max(candidates_votes, key = candidates_votes.get) + ')\n'))
file.write('-------------------------\n')
file.close()