#!/usr/bin/env python
import urllib2
import json
url = "https://notoriousbiginteger.pythonanywhere.com/cuisines/json"
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)
"""
for i in range(5):
    if(data['Cuisines'][i]['name'] ):
        print(data['Cuisines'][i]['name'])
#print(data['Cuisines'][0]['name'])
"""
for item in data['Cuisines']:
    print(item['name'])