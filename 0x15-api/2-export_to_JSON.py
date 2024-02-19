#!/usr/bin/python3
""" Exports to-do list information for a given employee ID to JSON format """


from requests import get
from sys import argv
import json

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    data = response.json()

    row = []
    response2 = get('https://jsonplaceholder.typicode.com/users')
    data2 = response2.json()

    for j in data2:
        if j['id'] == int(argv[1]):
            u_name = j['username']
            id_no = j['id']

    row = []

    for j in data:

        new_dict = {}

        if j['userId'] == int(argv[1]):
            new_dict['username'] = u_name
            new_dict['task'] = j['title']
            new_dict['completed'] = j['completed']
            row.append(new_dict)

    final_dict = {}
    final_dict[id_no] = row
    json_obj = json.dumps(final_dict)

    with open(argv[1] + ".json", "w") as f:
        f.write(json_obj)
