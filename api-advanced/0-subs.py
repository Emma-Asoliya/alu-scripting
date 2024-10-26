#!/usr/bin/python3
"""0-subs.py"""

import requests


def number_of_subscribers(subreddit):
    """Reddit subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    else:
        return response.json().get("data").get("subscribers")#!/usr/bin/python3
""" 0-subs module """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json" \
        .format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data') \
            .get('subscribers')
    return 0
