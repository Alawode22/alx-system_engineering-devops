#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import requests
import sys
import csv

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

    # File name format: USER_ID.csv
    file_name = "{}.csv".format(employee_id)

    # Write data to CSV
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, username, task['completed'], task['title']])
