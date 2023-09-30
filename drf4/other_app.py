import requests
import os, json

URL = 'http://127.0.0.1:8000/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)

# get_data()

def post_data():
    data = {
        'name': 'Steve',
        'roll_no': 104,
        'city': 'San Francisco'
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    data = r.json()
    print(data)    

# post_data()

def put_data():
    data = {
        'id': 3,
        'name': 'Jules',
        'city': 'Miami',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    data = r.json()
    print(data)

# put_data()

def delete_data():
    data = {'id': 2}
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    json_data = r.json()
    print(json_data)
