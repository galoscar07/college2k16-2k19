#!/bin/sh
#Write a shell script that will monitor the content of a folder (given in the command line) and notify if files or folders are created or deleted from it.
if [ -d $1 ] ; then
	before=`ls -A $1 | wc -l`
	while [ 10 -lt 11 ]; do
    		if [ `ls -A $1 | wc -l` -gt $before ]; then
      			 echo "New something has been created!"
		fi
   		if [ `ls -A $1 | wc -l` -lt $before ]; then
      			 echo "Something has been deleted!"
   		fi
   		before=`ls -A $1 | wc -l`
   		sleep 1
	done
else echo "The parameter is not a directory"
fi
exit 0 
