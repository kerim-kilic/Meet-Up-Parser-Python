# Author:   Kerim Kilic
# date:     04/2022

import string
import pandas as pd
import numpy as np
import json

##########################################
# Read in JSON file and create dataframe #
##########################################
with open('meetup_data.json') as f:
    a = json.load(f)

data = pd.DataFrame(a)
total_data = len(data)

tmp = data["input"].values[0]["location"]
tmp = tmp[0]
##############################################
# Create function to rearrange datastructure #
##############################################
def arrange_data(temp):
    tmp = temp
    if("edition" in tmp):   # Check if edition is present
        meetup_string = tmp["edition"] + " " + tmp["name"] + " · " + tmp["startDate"]
    else:
        meetup_string = tmp["name"] + " · " + tmp["startDate"]
    if("endDate" in tmp):   # Check if endDate is present
        meetup_string = meetup_string + " / " + tmp["endDate"] + " · "
    else:
        meetup_string = meetup_string + " · "
    ##
    i = 0
    location_string = ""
    while(i < np.size(tmp["location"])): # Loop twice if there are two locations
        # Check if city and state are present in location
        if("city" in tmp["location"][i] and "state" in tmp["location"][i]):
            location_string = location_string + tmp["location"][i]["city"] + ", " + tmp["location"][i]["state"] + ". " + tmp["location"][0]["country"]
        elif("city" in tmp["location"][i] and "state" not in tmp["location"][i]):
            location_string = location_string + tmp["location"][i]["city"] + ", " + tmp["location"][i]["country"]
        elif("city" not in tmp["location"][i] and "state" in tmp["location"][i]):
            location_string = location_string +  tmp["location"][i]["state"] + ", " + tmp["location"][i]["country"]
        # Check if two locations are in the same country
        if(i == 0 and np.size(tmp["location"]) > 1 and tmp["location"][i]["country"] != tmp["location"][i+1]["country"]):
            location_string = location_string + " | "
        elif((i == 0 and np.size(tmp["location"]) > 1 and tmp["location"][i]["country"] == tmp["location"][i+1]["country"])):
            location_string = location_string.replace(", " + tmp["location"][i]["country"], " | ")
        i = i + 1
    return(meetup_string + location_string)
####################################################################
# Loop through arrange_data() function to create new datastructure #
####################################################################
i = 0
new_data = []
while(i < total_data):
    tmp = data["input"].values[i]
    new_data.append(arrange_data(tmp))
    i = i + 1
###################################################################
# Save new datastructure in a dictionary and create new JSON file #
###################################################################
new_data = pd.DataFrame(new_data)
new_data.columns = ["meetUps"]
new_data['meetUps'] = new_data['meetUps'].astype("string")
dict_data = new_data.to_dict("dict")
list_data = list(dict_data["meetUps"].values())
new_dict = {"meetUps" : list_data}

with open('./json_data.json', 'w') as outfile:
    json.dump(new_dict, outfile, indent = 2,ensure_ascii = False)