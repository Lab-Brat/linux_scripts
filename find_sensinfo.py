#!/usr/bin/python3
import sys
import subprocess

path = str(sys.argv[1])
try:
    exclude_dir = str(sys.argv[2])
except:
    exclude_dir = '{venv,__pycache__}'

def get_output(command):
    return subprocess.run(command, capture_output=True)

def print_decode_output(output):
    for line in output.stdout.decode('utf-8').split('\n'):
        print(line)

ip_regex = '"\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b"'
grep_ip = ["grep", "-roE", ip_regex, exclude_dir, path]
grep_pass = ["grep", "-ri", "password", exclude_dir, path]
print("Found IP addresses: ")
print_decode_output(get_output(grep_ip))
print("Found Passwords: ")
print_decode_output(get_output(grep_pass))
