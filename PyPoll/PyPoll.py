import csv, os

#hard path to file I'll reference
VotingDataRaw = 'C:/Users/leala/Documents/Data Git Repo/python-challenge/Python_Challenge/Resources/election_data.csv'

#create a list of Candidates
Candidates = ["Correy", "Khan", "Li", "O'Tooley"]

#and then variables to store the vote count for each Candidate
Can1 = 0
Can2 = 0
Can3 = 0
Can4 = 0

#get to reading this document aka Alex. Alex? Because why not
with open(VotingDataRaw, "r") as Alex:
    voteData = csv.reader(Alex)
    next(voteData)
    
#loop throught and find total number of votes cast
    Voters = 0
    for row in voteData:
        Voters = Voters + 1

#Loop through and grab vote count for each Candidate
    for lines in voteData:
        if line[3] == Candidates[0]:
            Can1 = Can1 + 1
        elif line[3] == Candidates[1]:
            Can2 = Can2 + 1
        elif line[3] == Candidates[2]:
            Can3 = Can3 +1
        else:
            Can4 = Can4 +1
    
    print(Can1)
    print(Can2)
    print(Can3)
    print(Can4)

print("Election Results")
print("--------------------------")
print("Total Votes Cast: ", Voters)
print("--------------------------")
print("Candidate Totals:")
print(Candidates[0], ": ")
print(Candidates[1], ": ")
print(Candidates[2], ": ")
print(Candidates[3], ": ")
print("--------------------------")
print("Winner with ", " of the vote, ")
print("--------------------------")