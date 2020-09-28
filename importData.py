# Importing needed libraries
import pandas as pd 

# Function to import data in a CSV file as a Pandas DataFrame
def importCSV(csvFile):
    # Importing the data into a Pandas DataFrame
    data = pd.read_csv(csvFile)
    print("Data Imported Successfully")

    # Sorting the data by date and time
    data.sort_values(["DateTime"])
    print("Data Sorted Chronologially")

    # Seperating date and time into separate columns and deleting datetime
    data["Date"] = pd.to_datetime(data["DateTime"]).dt.date
    data["Time"] = pd.to_datetime(data["DateTime"]).dt.time
    print("Date and Time Columns Separated")

    # Deleting the old datetime column
    del data["DateTime"]
    print("Datetime Column Deleted")

    # Adding a datetime64 column
    data["datetime64"] = pd.to_datetime(data["Date"])
    print("Datetime64 Column Created")

    # Returning the dataframe
    print("Import and Processing Complete")
    return data