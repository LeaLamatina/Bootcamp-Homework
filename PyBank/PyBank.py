import os, csv

#creating direct path for the csv file with information
BudgetDataRaw = 'C:/Users/leala/Documents/Data Git Repo/python-challenge/Python_Challenge/Resources/budget_data.csv'

#open csv fill to read in, and name it Alex because he asked for it
with open(BudgetDataRaw, "r") as Alex:
    budData = csv.reader(Alex)
    next(budData)

#So many variables, there was probably a cleaner way to do this
    Months = 0
    PLTot = 0
    totalDiff = 0
    previousMonth = 0
    firstLoop = True
    currentDiff = 0
    maxDiff = 0
    maxDate = 0
    minDiff = 0
    minDate = 0

#for loop through to capture the totals of each
    for line in budData:
        Months = Months + 1
        PLTot = PLTot + int(line[1])
        if firstLoop == False:
            currentDiff = previousMonth - int(line[1])
            totalDiff = totalDiff + currentDiff
        previousMonth = int(line[1])
        if currentDiff > maxDiff:
            maxDiff = currentDiff
            maxDate = line[0]
        if currentDiff < minDiff:
            minDiff = currentDiff
            minDate = line[0]
        firstLoop = False

#total months - 1 because you need two months to average    
averageDiff = totalDiff / (Months - 1)

print("Budget Snapshot")
print("--------------------------")
print("Total Number of Months: ", Months)
print("Net Profit/Loss over", Months, "Months: ", PLTot)
print("--------------------------")
print("Average Change: ", averageDiff)
print("Greatest Increase: ", maxDate, " > ", maxDiff)
print("Greatest Decrease: ", minDate, " > ", minDiff)
print("--------------------------")