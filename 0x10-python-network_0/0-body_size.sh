#!/bin/bash
# This script takes in a URL, it sends a request and displays the size of the body of the response
curl -s "$1" | wc -c
