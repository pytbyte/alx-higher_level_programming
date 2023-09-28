#!/usr/bin/bash
#Reads input url from args and sends request to the same.
#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
url="$1"
echo "Size of the response body: $(curl -s "$url" | wc -c) bytes"
