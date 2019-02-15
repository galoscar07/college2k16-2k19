#!/bin/bash

if test -e $1; then
    echo exista
else
    echo nu exista
fi

if test -e $1 && ! test -d $1; then
    echo exista dar nu e director
elif test -d $1; then
    echo director
else
    echo am ajuns la else
fi

if [ -e $1 ] && [ ! -d $1 ]; then
    echo exista dar nu e director
elif [ -d $1 ]; then
    echo director
else
    echo am ajuns la else
fi

