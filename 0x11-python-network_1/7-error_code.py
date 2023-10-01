#!/usr/bin/python3
"""_7-error_code_
 takes in a URL,
 sends a request to the URL
 and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response)
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
