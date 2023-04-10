#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 domain"
    exit 1
fi

domain=$1
whois_output=$(whois "$domain")

# Extract relevant information using regular expressions
if [[ -n $(echo $whois_output |   grep -i amazon ) ]] ; then  owner="AWS"
elif [[ -n $(echo $whois_output | grep -i atman ) ]] ;  then  owner="Atman"
elif [[ -n $(echo $whois_output | grep -i azure ) ]] ;  then  owner="Azure"
elif [[ -n $(echo $whois_output | grep -i hetzner ) ]] ;    then  owner="Hetzner"
elif [[ -n $(echo $whois_output | grep -i hivelocity ) ]] ; then  owner="Hivelocity"
elif [[ -n $(echo $whois_output | grep -i digitalocean ) ]] ; then  owner="DigitalOcean"
else
	owner=$(echo "$whois_output" | grep -E -i "org-name|orgname" \
	                             | tail -n 1 \
								 | awk '{print $2}')
fi
country=$(echo "$whois_output" | grep -i "Country:" \
                               | tail -n 1 \
							   | awk '{print $2}')

# Display the extracted information
echo "Domain Information:"
echo ">=> IP:       $1"
echo ">=> Provider: $owner"
echo ">=> Country:  $country"
