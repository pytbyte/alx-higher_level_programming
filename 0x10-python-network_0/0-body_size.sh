#!/usr/bin/bash
#Reads input url from args and sends request to the same.

url="$1"
echo "Size of the response body: $(curl -s "$url" | wc -c) bytes"
