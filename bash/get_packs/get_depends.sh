#!/bin/bash
# script reads the depencies list from depends.txt line by line,
# downloads if available, if error is encountered, record in err.txt
#
echo "" > dwn.txt
echo -n "input package name: "
read pack

apt-cache showpkg $pack | awk '/Dependencies:/,/Provides:/ {for(i=1;i<NF;i++) {if(i%3==0) {print $i}}}' | tee depends.txt

FILE="depends.txt"
LINES=$(cat $FILE)

for LINE in $LINES
do
	apt-get download --print-uris "$LINE" | grep ^\' | cut -d\' -f2 \
	1>> dwn.txt 2>> err.txt
	wget -nv -P ./packs $(tail -n 1 dwn.txt) 
done

