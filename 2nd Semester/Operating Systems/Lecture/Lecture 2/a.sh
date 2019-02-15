#!/bin/bash
A=5
B="mere"

echo "Ana are $A $B"
echo 'Ana are $A $B'

echo $0

echo $*
echo $1 $2 $3 $4 $5 $6 $7 $8 $9
shift
echo $1 $2 $3 $4 $5 $6 $7 $8 $9
shift 3
echo $1 $2 $3 $4 $5 $6 $7 $8 $9
echo $*
