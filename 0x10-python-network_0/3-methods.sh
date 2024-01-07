#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
allowed_methods=$(curl -sI -X OPTIONS "$1" | awk '/Allow/ {print $2}'); echo "$allowed_methods"
