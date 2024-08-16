#!/usr/bin/python3
"""
Reddit API Recursive Word Count Module
Counts keyword occurrences in hot articles from a subreddit.
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=''):
    """
    Recursively counts keyword occurrences in
    titles of hot articles in a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'python:count_words:v1.0 (by /u/yourusername)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json().get('data', {})
            posts = data.get('children', [])
            after = data.get('after')

            for post in posts:
                title = post['data']['title'].lower()
                for word in word_list:
                    word = word.lower()
                    if word in title.split():
                        word_count[word] = {
                            word_count.get(word, 0) + title.split().count(word)
                        }

            if after:
                return count_words(subreddit, word_list, word_count, after)
            else:
                return word_count
        else:
            return {}
    except requests.exceptions.RequestException:
        return {}

    if not after:
        sorted_words = {
            sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
        }
        for word, count in sorted_words:
            if count > 0:
                print(f"{word}: {count}")
