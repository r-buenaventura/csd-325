# Roxanne Buenaventura
# CSD 325
# Assignment 9_2
# 19 July 2026

import requests
response = requests.get("http://swapi.dev/api/planets/1/")
print(response.status_code)

import json

# create a fomratted string on the Python JSON object
def jprint(obj):
    test = json.dumps(obj, sort_keys=True, indent=4)
    print(test)

jprint(response.json())