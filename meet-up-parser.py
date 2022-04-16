# Author:   Kerim Kilic
# date:     04/2022
from re import L
import pandas as pd
import numpy as np
import json

from pprint import pprint


f = open("meetup_data.json")
data = json.load(f)


for i in data:
    a = i["input"]
f.close()

data = pd.DataFrame(a)
total_data = len(data)

#######################

city_1 = []
state_1 = []
country_1 = []
city_2 = []
state_2 = []
country_2 = []
j = 0
while(j < total_data):
    if(np.size(data["location"].values[j]) == 1):
        # Do something else
        tmp = data["location"].values[j]
        tmp = tmp[0]
        if 'city' in tmp:
            city_1.append(tmp['city'])
            city_2.append("")
        else:
            city_1.append("")
            city_2.append("")
        if 'state' in tmp:
            state_1.append(tmp['state'])
            state_2.append("")
        else:
            state_1.append("")
            state_2.append("")
        if 'country' in tmp:
            country_1.append(tmp['country'])
            country_2.append("")
        else:
            country_1.append("")
            country_2.append("")
    else:
        # Do something else
        tmp = data["location"].values[j]
        tmp2 = tmp[0]
        tmp3 = tmp[1]
        if 'city' in tmp2:
            city_1.append(tmp2['city'])
        else:
            city_1.append("")
        if 'state' in tmp2:
            state_1.append(tmp2['state'])
        else:
            state_1.append("")   
        if 'country' in tmp2:
            country_1.append(tmp2['country'])
        else:
            country_1.append("") 
        
        if 'city' in tmp3:
            city_2.append(tmp3['city'])
        else:
            city_2.append("")
        if 'state' in tmp3:
            state_2.append(tmp3['state'])
        else:
            state_2.append("")   
        if 'country' in tmp3:
            country_2.append(tmp3['country'])
        else:
            country_2.append("") 

    j = j + 1

###

data['edition'] = data['edition'].astype("string")
data['name'] = data['name'].astype("string")
data['startDate'] = data['startDate'].astype("string")
data['endDate'] = data['endDate'].astype("string")
data['city_1'] = city_1
data['city_1'] = data['city_1'].astype("string")
data['state_1'] = state_1
data['state_1'] = data['state_1'].astype("string")
data['country_1'] = country_1
data['country_1'] = data['country_1'].astype("string")
data['city_2'] = city_2
data['city_2'] = data['city_2'].astype("string")
data['state_2'] = state_2
data['state_2'] = data['state_2'].astype("string")
data['country_2'] = country_2
data['country_2'] = data['country_2'].astype("string")
del(data['location'])

data = data.replace(np.nan, '', regex = True)

print(data)

i = 0
new_data = []
while(i < total_data):
    # Check if edition is present
    if(data.values[i,0] != ""):
        new_data.append(data.values[i,0] + " " + data.values[i,1] + " · " + data.values[i,2])
    else:
        new_data.append(data.values[i,1] + " · " + data.values[i,2])
    # Check if endDate is present
    if(data.values[i,3] == ""):
        new_data[i] = new_data[i] + " " + data.values[i,3] + " · "
    else:
        new_data[i] = new_data[i] + " / " + data.values[i,3] + " · "
    
    # Check if city_1 and state_1 are present and if a second location is present
    if(data.values[i,9] != "" and (data.values[i,9] == data.values[i,6])):
        if(data.values[i,4] == ""):
            if(data.values[i,5] != ""):
                new_data[i] = new_data[i] + data.values[i,5]
        else:
            if(data.values[i,5] != ""):
                new_data[i] = new_data[i] + data.values[i,4] + ", " + data.values[i,5]
            else:
                new_data[i] = new_data[i] + data.values[i,4]
    else:
        if(data.values[i,4] == ""):
            if(data.values[i,5] != ""):
                new_data[i] = new_data[i] + data.values[i,5] + ", " + data.values[i,6]
        else:
            if(data.values[i,5] != ""):
                new_data[i] = new_data[i] + data.values[i,4] + ", " + data.values[i,5] + ". " + data.values[i,6]
            else:
                new_data[i] = new_data[i] + data.values[i,4] + ", " + data.values[i,6]
    
    # Check if city_2 and state_2 are present
    if(data.values[i,9] != ""):
        if(data.values[i,7] != ""):
            if(data.values[i,8] == ""):
                new_data[i] = new_data[i] + " | " + data.values[i,7] + ", " + data.values[i,9]
            else:
                new_data[i] = new_data[i] + " | " + data.values[i,7] + ", " + data.values[i,8] + ". " + data.values[i,9]
        else:
            new_data[i] = new_data[i] + " | " + data.values[i,8] + ", " + data.values[i,9]

    i = i + 1
            
print(new_data[0])
print(new_data[1])
print(new_data[2])
print(new_data[3])
print(new_data[4])
print(new_data[5])