#!/bin/bash

PREV=""
while true; do
    if [ -z "$PREV" ]; then
        PREV=`ls -Rl`
    fi
    sleep 1
    NOW=`ls -Rl`
    if [ ! "$PREV" = "$NOW" ]; then
        echo cineva a schimbat ceva
    fi
    PREV=$NOW
done


