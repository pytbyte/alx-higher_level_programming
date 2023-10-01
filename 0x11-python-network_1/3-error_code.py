#!/usr/bin/python3
"""_3-error_code_
 takes in a URL,
 sends a request to the URL
 and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(data)

    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
