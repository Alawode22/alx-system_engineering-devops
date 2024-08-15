#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get

def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    
    - Checks if the subreddit is a valid string.
    - Uses a custom User-Agent to avoid being blocked by Reddit.
    - Fetches the top 10 hot posts for the specified subreddit.
    - Handles errors and prints "None" if any issue occurs.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print("None")
        return

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    try:
        response = get(url, headers=user_agent, params=params)
        if response.status_code != 200:
            print("None")
            return

        results = response.json()
        my_data = results.get('data', {}).get('children', [])
        if not my_data:
            print("None")
            return
        
        for i in my_data:
            print(i.get('data', {}).get('title', "None"))

    except Exception as e:
        print("None")
