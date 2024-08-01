#!/usr/bin/python3
"""
Module that fetches an employee's TODO list progress and exports it to JSON.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Get user ID from the command line argument
    user_id = sys.argv[1]

    # Base URL for the API
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user information
    user = requests.get(f"{url}users/{user_id}").json()

    # Fetch the TODO list for the user
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    # Prepare the data in the required format
    user_tasks = {
        str(user_id): [  # USER_ID as string key
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            for todo in todos
        ]
    }

    # Write the data to a JSON file named USER_ID.json
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(user_tasks, json_file)
