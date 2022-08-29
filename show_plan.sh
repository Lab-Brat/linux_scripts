#!/bin/bash

plan='/home/labbrat/Documents/notes/__PLAN__.md'


if [[ $1 == 'all' ]]
then
	for i in {0..11}
	do
		date=$(date --date="$(date +%Y-%m-15) +$i month" +%b)
		if [[ $(grep $date $plan) != '' ]]
		then
			echo "===== Plans for $date ====="
			grep $date $plan | awk '{$(NF--)=""; print}'
			echo ""
		fi
	done
	exit 0
fi


if [[ $1 == 'next' ]]
then
	date=$(date --date="$(date +%Y-%m-15) +1 month" +%b)
else
	date=$(date +%b)
fi

grep $date $plan | awk '{$(NF--)=""; print}'

