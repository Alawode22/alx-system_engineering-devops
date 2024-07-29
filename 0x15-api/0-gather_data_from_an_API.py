#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(url + "users/{}".format(employee_id)).json()
    
    # Fetch todos for the user
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    # Find completed tasks
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Print results in required format
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for title in completed:
        print("\t {}".format(title))
