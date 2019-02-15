#!/bin/bash

while read -p "Student si nota:" S N; do
    if [ -z "$S" ]; then
        echo "vreau nume" >&2
        continue
    fi
    if [ -z "$N" ]; then
        echo "vreau nota" >&2
        continue
    fi
    if [ $N -lt 5 ]; then
        echo "of of of $S"
    fi
done
