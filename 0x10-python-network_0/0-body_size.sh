#!/usr/bin/bash

url="$1"
echo "Size of the response body: $(curl -s "$url" | wc -c) bytes"
