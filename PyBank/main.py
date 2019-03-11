import os
import csv

Revenue = 0
NextRevenue = 1

csvpath = os.path.join("budget_data.csv")

Dates = []
ProfitLoss = [0]
RevenueChange = []


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        Dates.append(row[0])
        ProfitLoss.append(int(row[1]))
        RevenueChange.append((ProfitLoss[NextRevenue])-ProfitLoss[Revenue])
        Revenue = Revenue + 1
        NextRevenue = NextRevenue +1

AvgRevChange = (sum(RevenueChange)-RevenueChange[0])/(len(Dates)-1)
AvgChange = round(AvgRevChange, 2)

MaxIndex = RevenueChange.index((max(RevenueChange)))
MaxMonth = Dates[MaxIndex]
MinIndex = RevenueChange.index((min(RevenueChange)))
MinMonth = Dates[MinIndex]


print(' ')
print(' ')
print('Financial Analysis')
print('-----------------------------------------------')
print("Total Months:  " + str(len(Dates)))
print("Total Revenue: $" + str(sum(ProfitLoss)))
print("Average Change: $" + str(AvgChange))
print("Greatest Increase in Profits: " + str(MaxMonth) + " ($" + str(max(RevenueChange)) + ")")
print("Greatest Decrease in Profits: " + str(MinMonth) + " ($" + str(min(RevenueChange)) + ")")

text_file = open("PybankAnalysis.txt", "w")
text_file.write("Financial Analysis\n")
text_file.write("----------------------------\n")
text_file.write("Total Months:  " + str(len(Dates)) +"\n")
text_file.write("Total Revenue: $" + str(sum(ProfitLoss)) + "\n")
text_file.write("Average Change: $" + str(AvgChange) + "\n")
text_file.write("Greatest Increase in Profits: " + str(MaxMonth) + " ($" + str(max(RevenueChange)) + ")\n")
text_file.write("Greatest Decrease in Profits: " + str(MinMonth) + " ($" + str(min(RevenueChange)) + ")\n")
text_file.close()