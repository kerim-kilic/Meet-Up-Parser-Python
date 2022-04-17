# Author:   Kerim Kilic
# date:     04/2022

import pandas as pd
import numpy as np
import json

with open('meetup_data.json') as f:
    a = json.load(f)

data = pd.DataFrame(a)
total_data = len(data)

tmp = data["input"].values[0]["location"]
tmp = tmp[0]

#######################

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
    if(np.size(tmp["location"]) == 1):
        if("city" in tmp["location"][0] and "state" in tmp["location"][0]):
            location_string = tmp["location"][0]["city"] + ", " + tmp["location"][0]["state"] + ". " + tmp["location"][0]["country"]
        elif("city" in tmp["location"][0] and "state" not in tmp["location"][0]):
            location_string = tmp["location"][0]["city"] + ", " + tmp["location"][0]["country"]
        elif("city" not in tmp["location"][0] and "state" in tmp["location"][0]):
            location_string = tmp["location"][0]["state"] + ", " + tmp["location"][0]["country"]
    elif(np.size(tmp["location"]) == 2):
        if(tmp["location"][0]["country"] != tmp["location"][1]["country"]):
            if("city" in tmp["location"][0] and "state" in tmp["location"][0]):
                location_string1 = tmp["location"][0]["city"] + ", " + tmp["location"][0]["state"] + ". " + tmp["location"][0]["country"]
            elif("city" in tmp["location"][0] and "state" not in tmp["location"][0]):
                location_string1 = tmp["location"][0]["city"] + ", " + tmp["location"][0]["country"]
            elif("city" not in tmp["location"][0] and "state" in tmp["location"][0]):
                location_string1 = tmp["location"][0]["state"] + ", " + tmp["location"][0]["country"]
        else:
            if("city" in tmp["location"][0] and "state" in tmp["location"][0]):
                location_string1 = tmp["location"][0]["city"] + ", " + tmp["location"][0]["state"]
            elif("city" in tmp["location"][0] and "state" not in tmp["location"][0]):
                location_string1 = tmp["location"][0]["city"]
            elif("city" not in tmp["location"][0] and "state" in tmp["location"][0]):
                location_string1 = tmp["location"][0]["state"]

        if("city" in tmp["location"][1] and "state" in tmp["location"][1]):
            location_string2 = " | " + tmp["location"][1]["city"] + ", " + tmp["location"][1]["state"] + ". " + tmp["location"][1]["country"]
        elif("city" in tmp["location"][1] and "state" not in tmp["location"][1]):
            location_string2 = " | " +  tmp["location"][1]["city"] + ", " + tmp["location"][1]["country"]
        elif("city" not in tmp["location"][1] and "state" in tmp["location"][1]):
            location_string2 = " | " +  tmp["location"][1]["state"] + ", " + tmp["location"][1]["country"]
        location_string = location_string1 + location_string2
    
    return(meetup_string + location_string)

#######################

i = 0
new_data = []
while(i < total_data):
    tmp = data["input"].values[i]
    new_data.append(arrange_data(tmp))
    i = i + 1

new_data = pd.DataFrame(new_data)
new_data.columns = ["meetUps"]
new_data['meetUps'] = new_data['meetUps'].astype("string")
dict_data = new_data.to_dict("dict")
list_data = list(dict_data["meetUps"].values())
new_dict = {"meetUps" : list_data}

with open('./json_data.json', 'w') as outfile:
    json.dump(new_dict, outfile,indent = 2,ensure_ascii=False)
