#!/usr/bin/python3

"""_1-hbtn_header_
 takes in a URL
 sends a request to the URL and
 displays the value of the X-Request-Id variable
 found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./1-hbtn_header.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            x_request_id = res.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)

    except Exception as e:
        print("Error :", e)
