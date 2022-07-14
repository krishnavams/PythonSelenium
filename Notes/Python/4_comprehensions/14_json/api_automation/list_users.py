from requests import request
from json import loads
import csv

url = "https://reqres.in/api/users?page=2"
response = request("GET", url)

# validate status code
assert response.status_code == 200

json_string = response.text

# de-serialize
python_object = loads(json_string)

users = python_object['data']

with open("./_users.csv", "w") as f:
    writer = csv.DictWriter(f, ["id", "email", "first_name", "last_name", "avatar"])
    writer.writeheader()
    for user in users:
        writer.writerow(user)