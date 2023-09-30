import requests
import os
import json

URL = ""

data = {
    'name': 'Ghazanfar',
    'roll_no': 104,
    'city': 'Abbottabad' 
}

json_data = json.dumps(data)
r = requests.post(url=URL,data=json_data)
data = r.json()
print(data) 