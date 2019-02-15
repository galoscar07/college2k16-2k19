#!/bin/bash

C=asdf.c
E=asdf

cat > $C <<EOF
#include <stdio.h>
int main() {
    printf("da, da, eu sunt");
    return 0;
}
EOF

for G in $*; do
    if [ ! -f $G ] || [ ! -x $G ]; then
        continue
    fi

    $G -Wall -o $E $C > /dev/null 2>&1 || continue
    if [ ! -f $E ] || [ ! -x $E ]; then
        continue
    fi
    
    ./$E > /dev/null || continue

    if [ ! "`./$E`" = "da, da, eu sunt" ]; then
        continue
    fi
    echo $G este GCC
done

#rm $C $E > /dev/null 2>&1
