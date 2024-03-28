#!/bin/bash
# Sends a request t o a URL passed as an argument, and displays only the status code of the response
curl -sLw "%{http_code}" -o /dev/null "$1"
