import csv, os

#hard path to file I'll reference
VotingDataRaw = 'C:/Users/leala/Documents/Data Git Repo/python-challenge/Python_Challenge/Resources/election_data.csv'

#create a list of Candidates
Candidates = ["Correy", "Khan", "Li", "O'Tooley"]

#So many variables to define
Can1 = 0
Can2 = 0
Can3 = 0
Can4 = 0
Voters = 0

#get to reading this document aka Alex. Alex? Because why not
with open(VotingDataRaw, "r") as Alex:
    voteData = csv.reader(Alex)
    next(voteData)
    
    for row in voteData:
#loop throught and find total number of votes cast
        Voters = Voters + 1
#grab vote count for each Candidate whilst looping
        if row[2] == Candidates[0]:
            Can1 = Can1 + 1
        elif row[2] == Candidates[1]:
            Can2 = Can2 + 1
        elif row[2] == Candidates[2]:
            Can3 = Can3 + 1
        else:
            Can4 = Can4 + 1

print("Election Results")
print("--------------------------")
print("Total Votes Cast: ", Voters)
print("--------------------------")
print("- Candidate Totals -")
print(Candidates[0], ">> ", Can1, ":", "{0:.0%}".format(Can1/Voters))
print(Candidates[1], ">> ", Can2, ":", "{0:.0%}".format(Can2/Voters))
print(Candidates[2], ">> ", Can3, ":", "{0:.0%}".format(Can3/Voters))
print(Candidates[3], ">> ", Can4, ":", "{0:.0%}".format(Can4/Voters))
print("--------------------------")
print("Winner: Khan") # dictionary return key value?
print("--------------------------")

with open("PyPoll_txt", "w") as Katrina:
    print("Election Results", file=Katrina)
    print("--------------------------", file=Katrina)
    print("Total Votes Cast: ", Voters, file=Katrina)
    print("--------------------------", file=Katrina)
    print("- Candidate Totals -", file=Katrina)
    print(Candidates[0], ">> ", Can1, ":", "{0:.0%}".format(Can1/Voters), file=Katrina)
    print(Candidates[1], ">> ", Can2, ":", "{0:.0%}".format(Can2/Voters), file=Katrina)
    print(Candidates[2], ">> ", Can3, ":", "{0:.0%}".format(Can3/Voters), file=Katrina)
    print(Candidates[3], ">> ", Can4, ":", "{0:.0%}".format(Can4/Voters), file=Katrina)
    print("--------------------------", file=Katrina)
    print("Winner: Khan", file=Katrina) # dictionary return key value?
    print("--------------------------", file=Katrina)