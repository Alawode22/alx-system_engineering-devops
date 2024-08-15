#!/usr/bin/python3
"""
Program to return 'OK' if a subreddit exists or '0' if it doesn't.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to check if a subreddit exists.
    Returns 'OK' if the subreddit exists, otherwise returns '0'.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'MyRedditAPI/0.1 (by YourUsername)'
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return "OK"
    else:
        return "0"
