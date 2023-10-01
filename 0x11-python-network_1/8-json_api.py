#!/usr/bin/python3
"""A script that
- takes in a letter
- sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    params = {'q': letter}

    response = requests.post(url, data=params)

    try:
        data = response.json()

        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
