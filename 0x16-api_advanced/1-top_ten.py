#!/usr/bin/python3
"""
1-top_ten
"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'my-reddit-app'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return
    
    data = response.json()
    posts = data.get('data', {}).get('children', [])
    
    for i in range(min(10, len(posts))):
        print(posts[i]['data']['title'])
