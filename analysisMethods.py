# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import os

# Function to analyse messages per day over time
def messagesPerDay(data, directory):
    # Finding number of messages sent by day (incudling days of no contact)
    data["Date"] = pd.to_datetime(data["DateTime"]).dt.date
    data["datetime64"] = pd.to_datetime(data["Date"])
    countedData = data.groupby(data["datetime64"]).size().reset_index(name="Count")
    countedData.set_index(["datetime64"], inplace=True)
    dates = pd.date_range(start=min(data["Date"]), end=max(data["Date"]))
    fullCountedData = countedData.reindex(dates, fill_value=0)

    # Creating a rolling average to plot alongwith the raw data
    rollingAverage = fullCountedData.rolling(14, min_periods=1).mean()

    # Plotting the result
    plt.bar(fullCountedData.index.values,fullCountedData["Count"].to_numpy(), color="black")
    #plt.plot(rollingAverage, "r")
    #plt.ylabel("Number of Daily Messages")
    #plt.xlabel("Date")
    plt.ylim((0,10000))
    plt.axis("off")
    plt.axis()

    plt.savefig(os.path.join(directory, "messagesPerDay.png"), format="png", dpi=3000)

def statsAnalysis(data):
    # Counting the total number of messages sent/recieved:
    totalMessages = len(data["DateTime"])
    print("Total Messsages Exchanged: %s" % totalMessages)

    # Average message length
    data["MessageLength"] = data["Content"].str.len()
    averageMessageLength = np.mean(data["MessageLength"].to_numpy())
    print("Average Message Length: %s characters" % averageMessageLength)

