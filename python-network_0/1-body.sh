#!/bin/bash
curl -s -o /tmp/body_$$ -w "%{http_code}" "$1" | {
    read code
    if [ "$code" -eq 200 ]; then
        cat /tmp/body_$$
    fi
}
rm -f /tmp/body_$$
