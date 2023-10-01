#!/usr/bin/python3
"""10-my_github:
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    personal_access_token = sys.argv[2]

    url = f'https://api.github.com/user'

    auth = HTTPBasicAuth(username, personal_access_token)

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        data = response.json()
        github_id = data.get('id')
        print(github_id)
    else:
        print(None)
