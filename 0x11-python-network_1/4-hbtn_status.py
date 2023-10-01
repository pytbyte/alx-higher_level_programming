#!/usr/bin/python3

"""_0-hbtn_status _
   A script to fetch https://alx-intranet.hbtn.io/status
   uses urllib package
   displays eg :
       Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with requests.get(url) as response:
            print("Body response:")
            print("\t- type:", type(response.text))
            print("\t- content:", response.text)

    except Exception as e:
        print("Error:", e)
