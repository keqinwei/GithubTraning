# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:37:00 2019

@author: smendonc
"""
import pandas as pd
b =["Taco Bell", "Shake Schack", "Chipotle"]
print(type(b))




import json
b_f =json.dumps(b)
print(type(b_f))
print(b_f)

print(type(json.loads(b_f)))


import requests
# Make the same request we did earlier, but with the coordinates of San Francisco instead.
parameters = {"lat": 37.78, "lon": -122.41}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
print(response.url)
print(response)
# Get the response data as a python object.  Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

print(response.headers)

from pandas.io.json import json_normalize
df = pd.DataFrame.from_dict(json_normalize(data), orient='columns')

m =data["response"]
m1=pd.DataFrame.from_dict(m, orient="columns")



el= requests.get("https://api.census.gov/data/2017/acs/acs1?get=NAME,group(B01001)&for=us:1")
print(type(el))
el_data=el.json()
el_df2 = pd.DataFrame(el_data[1:],columns=el_data[0])
#from pandas.io.json import json_normalize
#df = pd.DataFrame.from_dict(json_normalize(el_data), orient='columns')


#type 2:


el_full= requests.get("https://api.census.gov/data/2017/acs/acs1")
print(type(el_full))
print(el_full)
el_data=el.json()
n=el_data["dataset"]
n1=n[0]
df_el_full = pd.DataFrame.from_dict(json_normalize(n), orient='columns')

el_df2 = pd.DataFrame(el_data[1:],columns=el_data[0])



a="%8790"
print(type(a))
b=a.str.slice(0,1)
print(type(b))