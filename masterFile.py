# Importing public libraries
import pathlib
import os

# Importing functions
from readJSONs import readJSONs
from importCSV import importCSVdata
from analysisMethods import *

# Getting the directory
directory = pathlib.Path(__file__).parent.absolute()

# Checking if the JSON files need importing
jsonCheck = input("Do CSV files need creation? [y/n]: ")
if jsonCheck == "y":
    readJSONs(directory)
else: 
    pass

# Opening the csv file directory and finding out how many files are in there
allCSVS = os.listdir(os.path.join(directory, "CSV Files"))

# Allowing the user to choose which to analyse
print("\nCSV Files Available for Analysis: ")
for i in range(len(allCSVS)):
    print("[%s]: %s" % (i+1, allCSVS[i][:-4]))

csvChoice = input("Type ID of File: ")

# Setting the csv file according to the choice
chosenCSV = os.path.join(directory, "CSV Files", allCSVS[int(csvChoice)-1])

# Running the data analysis script
csvDataFrame = importCSVdata(chosenCSV)
while True:
    # Asking what type of analysis to carry ot
    print("\nChoose what analyses to perform:")
    print("[1]: Messages per day over time")
    print("[2]: General statistics")
    analysisChoice = input("Analysis: ")

    # Running the desired analysis
    if analysisChoice == "1":
        messagesPerDay(csvDataFrame, directory)
    elif analysisChoice == "2":
        statsAnalysis(csvDataFrame)
    else:
        pass

    