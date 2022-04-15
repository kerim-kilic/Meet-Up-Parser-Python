# Author:   Kerim Kilic
# date:     04/2022
import pandas as pd
from numpy import NaN, size
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
    if(size(data["location"].values[j]) == 1):
        # Do something else
        tmp = data["location"].values[j]
        tmp = tmp[0]
        if 'city' in tmp:
            city_1.append(tmp['city'])
            city_2.append(NaN)
        else:
            city_1.append(NaN)
            city_2.append(NaN)
        if 'state' in tmp:
            state_1.append(tmp['state'])
            state_2.append(NaN)
        else:
            state_1.append(NaN)
            state_2.append(NaN)
        if 'country' in tmp:
            country_1.append(tmp['country'])
            country_2.append(NaN)
        else:
            country_1.append(NaN)
            country_2.append(NaN)
    else:
        # Do something else
        tmp = data["location"].values[j]
        tmp2 = tmp[0]
        tmp3 = tmp[1]
        if 'city' in tmp2:
            city_1.append(tmp2['city'])
        else:
            city_1.append(NaN)
        if 'state' in tmp2:
            state_1.append(tmp2['state'])
        else:
            state_1.append(NaN)   
        if 'country' in tmp2:
            country_1.append(tmp2['country'])
        else:
            country_1.append(NaN) 
        
        if 'city' in tmp3:
            city_2.append(tmp3['city'])
        else:
            city_2.append(NaN)
        if 'state' in tmp3:
            state_2.append(tmp3['state'])
        else:
            state_2.append(NaN)   
        if 'country' in tmp3:
            country_2.append(tmp3['country'])
        else:
            country_2.append(NaN) 

    j = j + 1

###

data['city_1'] = city_1
data['state_1'] = state_1
data['country_1'] = country_1
data['city_2'] = city_2
data['state_2'] = state_2
data['country_2'] = country_2
del(data['location'])

print(data.dtypes)
print(data)