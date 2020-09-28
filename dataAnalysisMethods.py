# Importing necessary libraries
import pandas as pd 

# Function to count the number of messages sent per day 
def countDailyMessages(dataFrame):

    # Getting the number of messages recorded for each individual day
    countedData = dataFrame.groupby(dataFrame["datetime64"]).size().reset_index(name="Count")

    # Setting the index of the counted data to the dates
    countedData.set_index(["datetime64"], inplace=True)

    # Creating an array of dates between the min and max dates of countedData
    dates = pd.date_range(start=min(dataFrame["Date"]), end=max(dataFrame["Date"]))

    # Filling in the dates missed in countedData
    fullCountedData = countedData.reindex(dates, fill_value=0)

    # Returning the filled dataframe
    return fullCountedData

# Function to calculate a rolling average for messages sent per day
def dailyMessagesRollingAverage(window, dataFrame):

    # Getting a rolling average for the counts per day
    rollingAverage = dataFrame.rolling(window, min_periods=1).mean()

    # Returning the averaged dataframe
    return rollingAverage

# Function to split the dataFrame between the two senders
def splitSenders(dataFrame):

    # Getting the names of each sender
    names = dataFrame(["Sender"]).unique()

    # Splitting dataFrame based on sender
    participantOne = dataFrame[dataFrame["Sender"] == names[0]]
    participantTwo = dataFrame[dataFrame["Sender"] == names[1]]

    # Returning the split dataFrames
    return participantOne, participantTwo

# Function to analyse the ratio of messages sent per person
def senderAnalysis(participantOne, participantTwo):

    # Finding the % of messages sent by participantOne
    percentage = (len(participantOne) / (len(participantOne) + len(participantTwo))) * 100

    # Counting the number of messages sent by each person per day
    participantOneCount = countDailyMessages(participantOne)
    participantTwoCount = countDailyMessages(participantTwo)

    # Creating a new array with the ratio between senders per day
    participantOneCount["Ratio"] = participantOneCount["Count"] / (participantOneCount["Count"] + participantTwoCount["Count"])

    # Creating a new array with dates and ratio
    senderRatioByDay = participantOneCount
    del senderRatioByDay["Count"]
    senderRatioByDay["Ratio"] = senderRatioByDay["Ratio"] * 100

    # Filling all NaN values with 0
    senderRatioByDay = senderRatioByDay.where(pd.notnull(senderRatioByDay), 0)
  
    # Returning the percentage, ratio dataFrame, and name of person who the dataFrame give the ratio for 
    return percentage, senderRatioByDay, names[0]
