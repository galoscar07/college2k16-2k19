#!/bin/bash

N=$1
shift

for U in $*; do
    K=`ps -u $U | wc -l`
    K=`expr $K - 1`

    if [ $K -gt $N ]; then
        echo $U
    fi
done
