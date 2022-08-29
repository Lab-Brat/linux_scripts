#!/bin/bash

plan='/path/to/plan/__PLAN__.md'

if [[ $1 == 'next' ]]
then
	date=$(date --date="$(date +%Y-%m-15) +1 month" +%b)
else
	date=$(date +%b)
fi

grep $date $plan | awk '{$(NF--)=""; print}'

