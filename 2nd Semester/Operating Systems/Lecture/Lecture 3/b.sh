#!/bin/bash

for A in safd 3245 k rrr 098; do
    echo $A
done

for A in "safd 3245 k rrr 098"; do
    echo $A
done

for A in $*; do
    echo $A
done

for A; do
    echo $A
done

for F in *; do
    file $F
done

for F in *.txt; do
    file $F
done
