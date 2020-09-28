''' Python Script to Import and Analyse Facebook Messenger Data '''

# Importing necessary libraries
from createCSV import createCSV
from importData import importCSV
from dataAnalysisMethods import *

''' Part 1: Joining the multiple json files 
            together and building them into 
            one csv file '''

# Imported function to generate CSV files
createCSV()

''' Part 2: Functions to import the data
            from the CSV files and then
            perform analysis on them '''

csvFile = r'C:\Users\Matth\Desktop\messagesProject\Tom.csv'

# Imported function to import CSV file and create a DataFrame
dataFrame = importCSV(csvFile)

dailyData = countDailyMessages(dataFrame)
averagedData = dailyMessagesRollingAverage(28, dailyData)

import matplotlib.pyplot as plt

plt.bar(dailyData.index.values, dailyData["Count"], color="grey", label="Raw Data")
plt.plot(dailyData.index.values, averagedData["Count"], "r-", label="Rolling Average")
plt.xlabel("Date")
plt.ylabel("Number of Messages")
plt.title("Number of Messages exchanged per Day")
plt.xticks(rotation=75)
plt.legend()
plt.show()
