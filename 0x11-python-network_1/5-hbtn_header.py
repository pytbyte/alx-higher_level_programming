#!/usr/bin/python3

"""_5-hbtn_header_
  takes in a URL,
  sends a request to the URL and
  displays the value of the variable X-Request-Id 
  in the response header
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./5-hbtn_header.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)

    except Exception as e:
        print("Error :", e)
