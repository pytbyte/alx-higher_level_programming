#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response and Display only body of a 200 status code response
curl -sL "$1" -o "output" -D "header" && grep -q "200 OK" "header" && cat "output"
