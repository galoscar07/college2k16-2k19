#!/bin/bash

for E in $*; do
#    for F in *.$E; do
    for F in `find . -name "*.$E" -type f`; do
        if [ ! -f $F ] || [ ! -r $F ]; then
            continue
        fi

#        if ! file $F | grep -q "ASCII text"; then
#            continue
#        fi

#        if [ "`file $F | grep 'ASCII text'`" = "" ]; then
#            continue
#        fi

#        if [ -z "`file $F | grep 'ASCII text'`" ]; then
#            continue
#        fi

        if test -z "`file $F | grep 'ASCII text'`"; then
            continue
        fi

        if [ `cat $F | wc -l` -lt 7 ]; then
            continue
        fi

        echo
        echo $F
        echo ========================
        tail -n +5 $F | head -3
    done
done
