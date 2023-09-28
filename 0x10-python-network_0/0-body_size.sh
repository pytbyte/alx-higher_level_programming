#!/usr/bin/bash
#Reads input url from args and sends request to the same.
#!/bin/bash

url="$1"
curl -s -o /tmp/response.txt "$url"
stat -c %s /tmp/response.txt
