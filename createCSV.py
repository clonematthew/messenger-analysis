#Importing necessary libraries
import os
import json
import csv
import pathlib
from datetime import datetime

# Function to run through message folders and create needed CSV files
def createCSV():
    
    # Getting directory where script is being run
    directory = pathlib.Path(__file__).parent.absolute()

    # Getting list of all folders in the directory
    folders = os.listdir(directory)

    # Going through all the items in the directory to find the messages
    for folder in folders:
        
        # Checking if directory is actually a folder and not the python file or csv file
        if folder.endswith(".py") or folder.endswith(".csv") or folder == "__pycache__":
            pass 

        else:
            # Printing the folder currently being processed
            print("Current processing folder: %s" % folder)

            # Creating the string for the csv file's name
            csvName = str(folder + ".csv")

            # Generating a path for the file to save in 
            csvName = os.path.join(directory, csvName)

            # Opening a csv file and adding the column headings
            csv_file = open(csvName, "w", encoding="utf-8", newline="")
            writer = csv.writer(csv_file)
            writer.writerow(["DateTime", "Sender", "Content"])

            # Passing through each file in the folder
            for filename in os.listdir(os.path.join(directory, folder)):

                # Checking if the file is a messages json file
                if filename.startswith("message"):

                    # Loading the data in the file using the json library
                    data = json.load(open(os.path.join(directory, folder, filename), "r", encoding='utf-8'))
            
                    # Passing through each message in the data
                    for message in data["messages"]:

                        try:
                            # Extracting the desired data from the message 
                            date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
                            sender = message["sender_name"]
                            content = message["content"]

                            # Writing the message data to the csv file
                            writer = csv.writer(csv_file)
                            writer.writerow([date, sender, content])

                        except KeyError:
                            pass
                
            # Closing the csv file
            csv_file.close()

    # Letting user know function has finished
    print("CSV files created successfuly.")