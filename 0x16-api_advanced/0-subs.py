#!/usr/bin/python3
"""
this doc for module
"""
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    except (KeyError, requests.RequestException):
        return 0

# Example usage:
subreddit = 'learnpython'
print(f"Number of subscribers in r/{subreddit}: {number_of_subscribers(subreddit)}")








