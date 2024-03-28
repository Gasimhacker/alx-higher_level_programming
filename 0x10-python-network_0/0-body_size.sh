#!/bin/bash
# A script takes in a URL, sends a request and display the body
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2 
