import os
import csv

#create starting variables
months = 0
profloss = 0
maxprofitdate = ""
maxlossdate = ""
maxprofit = 0
maxloss = 999999999
net = 0
difference = 0
previous = 0
change = 0
diflist = []

#create path for csv
csvpath = os.path.join("Resources", "budget_data.csv")
#open csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #read/skip header row
    firstrow = next(csvreader)

    #loop starts in second row
    for row in csvreader: 

        #track months 
        months = months + 1
        
        #track net profit / loss
        net = net + int(row[1])

        #track change in difference
        difference = int(row[1]) - previous
        diflist.append(difference)

        #grab/replace max profit & date
        if maxprofit < int(row[1]) and months != 0:
            maxprofit = difference
            maxprofitdate = str(row[0])

        #grab/replace max loss & date
        if maxloss > int(row[1]) and months != 0:
            maxloss = difference
            maxlossdate = str(row[0])

        #previous tracker
        previous = int(row[1])

#create ending variables

#average change mean
meandif = (difference / months)
#account for skipped month
months = months + 1

#print analysis 
print("Financial Analysis")
print("------------------------------")
print("total months: " + str(months))
print("total: " + str(net))
print("average: " + str(meandif))
print("greatest increase in profits: " + str(maxprofitdate) + "(" + str(maxprofit) + ")")
print("greatest decrease in profits: " + str(maxlossdate) + "(" + str(maxloss) + ")")

#EXPORT CODE DOES NOT WORK  

#export text file
#utput = os.path.join("Analysis", "results.txt")

#f = open(output, 'w')
    
#txtfile.write("Financial Analysis"
#txtfile.write("--------------------")
#txtfile.write("total months:  + str(months)")
#txtfile.write("total:  + str(net)")
#txtfile.write("average: " + str(meandif)")
##txtfile.write("greatest decrease in profits: " + str(maxlossdate) + "(" + str(maxloss) + ")")

