#! /usr/bin/env python3


import os

import requests

# Define the target directory
BASEPATH = "/data/feedback/"

# External IP 
URL = "http://35.184.254.21/feedback/"

# List all .txt files under /data/feedback directory
folder = os.listdir(BASEPATH)
feedback_list = []

# Traverse over each file in the list 
for file in folder:
    # Safe check to only process text files and avoid hidden system files
    if file.endswith(".txt"):
        # Open the file in read mode to read the contents of the file
        with open(BASEPATH + file, "r") as f:
            # Create a dictionary by keeping title, name, date and feedback as keys for the content value
            # rstrip to remove any newlines trailing
            feedback_list.append({
                "title": f.readline().rstrip("\n"),
                "name": f.readline().rstrip("\n"),
                "date": f.readline().rstrip("\n"),
                "feedback": f.read().rstrip("\n"),
            })


# Use the python request module to post dictionary to the company's website
for item in feedback_list:
    resp = requests.post(URL, data=item)
    # Print the status code and text of the response object to check ehat's going on to make sure an error message isn't returned
    if resp.status_code != 201:
        raise Exception("POST error status={}".format(resp.status_code))
    print("Created feedback ID:{}".format(resp.json()["id"])) 
