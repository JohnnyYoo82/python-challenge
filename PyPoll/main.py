import os
import csv

csvpath = os.path.join("election_data.csv")

TotalVotes = 0
CandidateVotes = {}
PercentageVotes = {}
WinnerVotes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        TotalVotes = TotalVotes + 1
        Candidate = row[2]

        if Candidate in CandidateVotes:
            CandidateVotes[Candidate] = CandidateVotes[Candidate] + 1
        else:
            CandidateVotes[Candidate] = 1

    for VotedCandidate, NumVotes in CandidateVotes.items():
        PercentageVotes[VotedCandidate] = CandidateVotes[VotedCandidate] / TotalVotes * 100
        
        if NumVotes > WinnerVotes:
            WinnerVotes = NumVotes
            WinningCandidate = VotedCandidate


        
print(' ')
print(' ')
print('Election Results')
print('-----------------------------------------------')
print("Total Votes:  " + str(TotalVotes))
print('-----------------------------------------------')

for VotedCandidate, NumVotes in CandidateVotes.items():
    print(str(VotedCandidate) + ":     " + str(round(PercentageVotes[VotedCandidate])) + "%     (" + str(NumVotes) + ")")

print('-----------------------------------------------')
print("Winner: " + str(WinningCandidate))
print('-----------------------------------------------')


text_file = open("PyPollResults.txt", "w")
text_file.write('Election Results\n')
text_file.write('-----------------------------------------------\n')
text_file.write("Total Votes:  " + str(TotalVotes) + "\n")
text_file.write('-----------------------------------------------\n')

for VotedCandidate, NumVotes in CandidateVotes.items():
    text_file.write(str(VotedCandidate) + ":     " + str(round(PercentageVotes[VotedCandidate])) + "%     (" + str(NumVotes) + ")" + "\n")

text_file.write('-----------------------------------------------\n')
text_file.write("Winner: " + str(WinningCandidate) + "\n")
text_file.write('-----------------------------------------------\n')
text_file.close()




