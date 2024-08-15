#!/usr/bin/python3
"""
Program to return the number of subscribers on a subreddit
by querying the Reddit API.
If not found, return 0.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function to make the query to get the
    number of subscribers for a subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        'User-Agent': 'i
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
