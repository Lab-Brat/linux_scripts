#!/usr/bin/python3
import sys
import subprocess


# ------------------------------ Script Logic ------------------------------- #
def split_dir(exclude_dir):
    '''
    Read a string of excluded directories,
    return a list of type ['--exclude-dir', 'dir', ...]
    '''
    if exclude_dir is None:
        return []
    split_dir = exclude_dir.split(',')
    flags = ('--exclude-dir,'*len(split_dir)).split(',')
    return [flag for dir in zip(flags, split_dir) for flag in dir] 

def get_output(command):
    '''
    Get output (in bytes) from running grep
    '''
    return subprocess.run(command, capture_output=True)

def print_decode_output(output):
    '''
    Decoded the output into string a print it line by line
    '''
    for line in output.stdout.decode('utf-8').split('\n'):
        print(line)

def find_info(path, exclude_dir):
    '''
    Grep regular expressions, output all matches.
    '''
    ip_regex = "\\b([0-9]{1,3}\.){3}[0-9]{1,3}\\b"
    grep_ip = ["grep", "-roE", ip_regex, path]
    grep_ip.extend(split_dir(exclude_dir))
    grep_pass = ["grep", "-ri", "password", path]
    grep_pass.extend(split_dir(exclude_dir))
    
    print("Found IP addresses: ")
    print_decode_output(get_output(grep_ip))
    print("Found Passwords: ")
    print_decode_output(get_output(grep_pass))


# ------------------------------- Run Script -------------------------------- #
if __name__ == '__main__':
    try:
        path = str(sys.argv[1])
    except IndexError:
        print('[ERROR!] Please specify grep location')
        sys.exit(1)

    try:
        exclude_dir = sys.argv[2]
    except IndexError:
        print('[WARNING!] exclude-dir not specified, '
            'using defauls: venv,__pycache__')
        exclude_dir = 'venv,__pycache__'

    find_info(path, exclude_dir)

# run in terminal
# ./find_sensinfo.py /opt/data 'folder1,folder2,venv'
#
# Result:
# Found IP addresses: 
# /opt/data/secret_file.txt:10.10.1.13

# Found Passwords: 
# /opt/data/secret_file.txt:my password: 123456
