#!/bin/bash
# A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response

body_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}' | tr -d '\r\n')

echo "${body_size}"
