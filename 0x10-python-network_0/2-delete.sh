#!/bin/bash
#sends a Delete request and prints body response 
curl -sX DELETE "$s1" -o "output" -D "Header" && cat "output"
