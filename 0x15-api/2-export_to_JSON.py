#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to JSON format."""
import requests
import sys
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(url + "users/{}".format(employee_id)).json()
    username = user['username']
    
    # Fetch todos for the user
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Prepare data in the required format
    tasks = []
    for task in todos:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        })

    # Write data to JSON file
    data = {employee_id: tasks}
    file_name = "{}.json".format(employee_id)
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)
