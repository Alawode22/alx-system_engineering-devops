#!/usr/bin/python3
"""
Module that fetches an employee's TODO list progress and exports it to JSON.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url}users/{user_id}").json()
    todos = requests.get(f"{url}todos", params={"userId": user_id}).json()

    user_tasks = {
        user_id: [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            }
            for todo in todos
        ]
    }

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(user_tasks, json_file)
