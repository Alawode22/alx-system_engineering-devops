#!/usr/bin/python3
"""
Reddit API Recursive Query Module
Recursively retrieves titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and
    returns a list of titles of all hot articles
    for a given subreddit.
    """
    after = '' if len(hot_list) == 0 else hot_list[-1]
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'python:recurse:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data.get('after')
            if after:
                return recurse(subreddit, hot_list)
            else:
                return hot_list
        else:
            return None
    except requests.exceptions.RequestException:
        return None
