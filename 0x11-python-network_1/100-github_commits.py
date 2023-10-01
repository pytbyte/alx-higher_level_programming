#!/usr/bin/python3
"""lists the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]

    url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    response = requests.get(url)

    if response.status_code == 200:
        commits_data = response.json()

        for commit in commits_data[:10]:
            sha_ = commit['sha']
            author_ = commit['commit']['author']['name']
            print(f"{sha_}: {author_}")
    else:
        print(f"Error: Unable to fetch. Status code: {response.status_code}")
