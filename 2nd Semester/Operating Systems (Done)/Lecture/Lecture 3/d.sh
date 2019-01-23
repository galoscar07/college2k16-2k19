#!/bin/bash

F=$1
SUM=0
N=0
for C in `cat $F`; do
    K=`echo $C | wc -c`
    K=`expr $K - 1`
    SUM=`expr $SUM + $K`
    N=`expr $N + 1`
done

echo "S=$SUM N=$N M=`expr $SUM / $N`"
