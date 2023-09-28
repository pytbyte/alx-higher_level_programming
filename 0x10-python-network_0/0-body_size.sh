#!/usr/bin/bash
#Reads input url from args and sends request to the same.

#check if url is present (script_name="$0" url= "$1")
if [ $# -ne 1 ]; then
    echo "Used as: $0 <URL> "
    exit 1
fi

#get url from args
url="$1"

#Create temporary file to hold curl respose
#initiale curl Get request
curl_response=$(mktemp)
curl -s -o "curl_response" "$url"

# Check if curl encountered an error
# Use 'stat' to get the size of the response body in bytes
if [ $? -ne 0 ]; then
  echo "Error: Failed to retrieve the URL."
  exit 1
fi
response_size=$(stat -c %s "$curl_response")

# Display the response bodey size
# remove temporary curl_response file
echo "Response body size: $response_size bytes"
rm "$curl_response"

