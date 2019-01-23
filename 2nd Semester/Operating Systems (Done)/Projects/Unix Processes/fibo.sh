#!/bin/bash 

n1=1
n2=1
n3=0
if [ $1 -lt 3 ]; then
	echo '1'
fi

for i in `seq 3 $1`;do
	n3=`expr $n1 + $n2`
	n1=$n2
	n2=$n3
done

echo $n2
