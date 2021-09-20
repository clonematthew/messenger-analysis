# Importing libraies
import pandas as pd

# Function to import the data from the csv into a pandas library
def importCSVdata(chosenCSV):
    # Reading csv into pandas
    dataFrame = pd.read_csv(chosenCSV)

    return dataFrame
