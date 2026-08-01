#!/bin/bash
# displays the body of a 200 status GET response, following redirects
[ "$(curl -s -o /dev/null -w "%{http_code}" -L "$1")" = "200" ] && curl -s -L "$1"
