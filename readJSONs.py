''' JSON File Merging Script '''

# Importing required public libraries 
import json
import os
import csv
from datetime import datetime
from alive_progress import alive_bar

def readJSONs(directory):
    # Getting the directory where the important folders are
    JSONdirectory = os.path.join(directory, "Message Folders")
    CSVdirectory = os.path.join(directory, "CSV Files")

    # Looping through all the folders in the directory
    allFolders = os.listdir(JSONdirectory)

    for folder in allFolders:
        # Notifying the user of the currently processed folder
        print("Currently Merging Folder: %s" % folder)

        # Generating a csv for the currently processed folder
        csvLoc = os.path.join(CSVdirectory, str(folder + ".csv"))

        # Opening the csv file
        csvFile = open(csvLoc, "w", encoding="utf-8", newline="")
        writer = csv.writer(csvFile)
        writer.writerow(["DateTime", "Sender", "Content"])

        # Looping through each file in the folder to merge them
        with alive_bar(len(os.listdir(os.path.join(JSONdirectory, folder)))) as bar:
            for filename in os.listdir(os.path.join(JSONdirectory, folder)):
                if filename.startswith("message_"):
                    # Getting the data from the json file
                    data = json.load(open(os.path.join(JSONdirectory, folder, filename), "r", encoding="utf-8"))

                    # Passing through each message in the data
                    for message in data["messages"]:
                        # Attempting to extract the data and write the data to the csv file
                        try:
                            date = datetime.fromtimestamp(message["timestamp_ms"] / 1000).strftime("%Y-%m-%d %H:%M:%S")
                            sender = message["sender_name"]
                            content = message["content"]
                            writer.writerow([date, sender, content])
                        
                        # Passing in the case of an error
                        except KeyError:
                            pass
                
                bar()
            
            # Closing the csv file and notifying user of completion
            csvFile.close()
            print("Folder Completed: %s" % folder)

    print("CSV Files Created Successfully")