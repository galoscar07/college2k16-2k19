#!/bin/bash
#Write a shell script that takes pairs of parameters (a filename and a number n) and outputs for each pair the name of the file, the number n and the nth word from each file.
while [ $# -ne 0 ]; do
    	fileName=$1 
	number=$2
	echo $1
	if [ -f $fileName ] ; then
		echo "The name of the file is: $fileName"
    		echo "The number is: $number"
    		nthword=`cat $fileName | awk -v n=$number '{ if(length($n) != 0) print $n }'`
    		echo "The word on the nth position is: $nthword"
    		shift; shift
	else echo "The variable $fileName is not a file"
	fi
done
exit 0
