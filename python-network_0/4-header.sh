#!/bin/bash
# sends a GET request with a custom user-id header and displays the body
curl -s -H "X-HolbertonSchool-User-Id: ${2:-98}" "$1"
