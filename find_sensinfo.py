#!/usr/bin/python3
import sys
import subprocess

path = str(sys.argv[1])
try:
    exclude_dir = sys.argv[2]
except:
    exclude_dir = 'venv,__pycache__'

def split_dir(exclude_dir):
    split_dir = exclude_dir.split(',')
    flags = ('--exclude-dir,'*len(split_dir)).split(',')
    all = []
    for dir, flag in zip(split_dir, flags):
        all.append(flag)
        all.append(dir)
    return all

def get_output(command):
    return subprocess.run(command, capture_output=True)

def print_decode_output(output):
    for line in output.stdout.decode('utf-8').split('\n'):
        print(line)

ip_regex = "\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b"
grep_ip = ["grep", "-roE", ip_regex, path]
grep_ip.extend(split_dir(exclude_dir))
grep_pass = ["grep", "-ri", "password", path]
grep_pass.extend(split_dir(exclude_dir))

print("Found IP addresses: ")
print_decode_output(get_output(grep_ip))
print("Found Passwords: ")
print_decode_output(get_output(grep_pass))
