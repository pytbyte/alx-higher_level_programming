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

import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    try:
        with urllib.request.urlopen(url) as response:
            body_response = response.read()
            print("Body response:")
            print("\t- type:", type(body_response))
            print("\t- content:", body_response)
            print("\t- utf8 content:", body_response.decode('utf-8'))
    except Exception as e:
        print("Error:", e)
