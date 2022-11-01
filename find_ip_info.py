import requests
import json
import sys

def get_info(ip):
    url = f"https://iplist.cc/api/{ip}"
    return requests.get(url).json()

def pretty_print(response):
    print(f"IP:       {response['ip']}")
    print(f"Provider: {response['asn']['name']}")
    print(f"Country:  {response['countryname']}\n")


try:
    for ip in sys.argv[1].split(','):
        pretty_print(get_info(ip))
except IndexError:
    print('Argument format: ip or ip1,ip2,ip3')
