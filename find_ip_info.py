import subprocess
import requests
import sys

def get_info(ip):
    '''
    Communicate with iplist.cc API to get information
    '''
    url = f"https://iplist.cc/api/{ip}"
    return requests.get(url).json()

def _get_grep(property, ip):
    '''
    grep for a particular property
    '''
    result = ''
    i = 0
    while result == '':
        result = subprocess.check_output(
                    f'whois {ip} | grep -i {property[i]} | head -n 1', 
                    shell = True, text = True)
        i += 1
    return result.split(':')[-1].replace(' ', '').replace('\n', '')

def get_info_local(ip):
    '''
    Use locally installed whois command to get information
    '''
    orgname = _get_grep(['role', 'org.*name', 'netname'], ip)
    country = _get_grep(['country'], ip)
    return {'ip': ip, 'org': orgname, 'country': country}

def pretty_print(response):
    '''
    Print only relevant information
    '''
    print(f"IP:       {response['ip']}")
    print(f"Provider: {response['org']}")
    print(f"Country:  {response['country']}\n")


if __name__ == '__main__':
    # Parse all IP addresses from CLI and search info
    try:
        for ip in sys.argv[1].split(','):
            ip_info  = get_info_local(ip)
            pretty_print(ip_info)
    except IndexError:
        print('Argument format: ip or ip1,ip2,ip3')
