#!/usr/bin/python3
"""2-post_email:
- takes in a URL
  sends a POST request to the passed URL
  takes email as a parameter
  displays the body of the response
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email_ = sys.argv[2]

    data = urllib.parse.urlencode({'email': email_}).encode("ascii")
    req = urllib.request.Request(url, data=data, method='POST')

    try:
        with urllib.request.urlopen(req) as response:
            data = response.read().decode('utf-8')
            print(data)

    except Exception as e:
        print("ERROR", e)
