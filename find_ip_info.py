#!/usr/bin/python3
import requests
import json
import sys

def get_info(ip):
    '''
    Communicate with iplist.cc API to get information
    '''
    url = f"https://iplist.cc/api/{ip}"
    return requests.get(url).json()

def pretty_print(response):
    '''
    Print only relevant information
    '''
    print(f"IP:       {response['ip']}")
    print(f"Provider: {response['asn']['name']}")
    print(f"Country:  {response['countryname']}\n")


# Parse all IP addresses from CLI and search info
try:
    for ip in sys.argv[1].split(','):
        pretty_print(get_info(ip))
except IndexError:
    print('Argument format: ip or ip1,ip2,ip3')

# Run in terminal
# ./find_ip_info.py 8.8.8.8
# IP:       8.8.8.8
# Provider: Google
# Country:  United States of America
