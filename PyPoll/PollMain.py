import os
import csv

#path for csv
election_csv = os.path.join("Resources", "election_data.csv")

#open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    


#NEVER GOT TO THIS