import os, csv

#creating direct path for the csv file with information
BudgetDataRaw = 'C:/Users/leala/Documents/Data Git Repo/python-challenge/Python_Challenge/Resources/budget_data.csv'

#open csv fill to read in, and name it Alex because he asked for it
with open(BudgetDataRaw, "r") as Alex:
    budData = csv.reader(Alex)
    next(budData)

#Variables for total Months and Profit/Loss
    Months = 0
    PLTot = 0

#for loop through to capture the totals of each
    for line in budData:
        Months = Months + 1
        PLTot = PLTot + int(line[1])

with open(BudgetDataRaw, "r") as Alex:
    budData = csv.reader(Alex)
    next(budData)

#create variables to store all the necessary information
    totalDiff = 0
    previousMonth = 0
    firstLoop = True
    currentDiff = 0
    maxDiff = 0
    minDiff = 0    
    
    for line in budData:
        if firstLoop == False:
            currentDiff = previousMonth - int(line[1])
            totalDiff = totalDiff + currentDiff
        previousMonth = int(line[1])
        if  - int(line[1]) > :
            maxDiff = [line[1], " - ", previousMonth - int(line[1])]
        if previousMonth - int(line[1]) < 0:
            minDiff = line[1], " - ", previousMonth - int(line[1])
        firstLoop = False
    
    #total months - 1 because you need two months to average    
    averageDiff = totalDiff / (Months - 1)
    print(totalDiff)
    print(averageDiff)
    print(maxDiff)
    print(minDiff)

print("Budget Snapshot")
print("--------------------------")
print("Total Number of Months: ", Months)
print("Net Profit/Loss over", Months, "Months: ", PLTot)
print("--------------------------")
print("Average Change: ", averageDiff)
print("Greatest Increase: ")
print("Greatest Decrease: ")
print("--------------------------")