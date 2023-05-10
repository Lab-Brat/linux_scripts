# Linux scripts
## About the Repo
This repository is a collection of scripts, written to automate some daily linux administation tasks.

## Table of Contents
- [Set Up](#set-up)
- [Using](#using)
   - [bash](#bash) 
   - [ipfind](#ipfind)
   - [sensfind](#sensfind)
   - [separator](#separator)
   - [show](#show)
   - [ssh](#ssh)
   - [sysd](#sysd)

## Set Up
Clone the repository and navigate to it
```bash
git clone https://github.com/Lab-Brat/linux_scripts.git
cd linux_scripts
```  

Then, install virtual enironment and build the app with setup.py
```bash
virtualenv venv
. venv/bin/activate
pip install --editable .
admin
```

## Using
#### ipfind
Use locally installed `whois` command to find information about IP provider 
and parse the output.
Examples:
```
# find IP provider info of address 8.8.8.8
admin ipfind -i 8.8.8.8
```

#### sensfind
Do a recursive search on a specified directory to look for IP addresses 
and passwords. 
Might come in handy to check sensitive info in a git repository 
before pushing it.
Examples:
```
# Search for sensitive info in current directory
admin sensfind -p ./
```


#### separator
Create a line separator for scripts. 
Default value is 79, which is recommend line length for Python code.
Examples:
```
# Print a separator line titled 'florples', length = 79
admin separator -t 'flroples'

# Print a separator line titled 'florples', length = 20
admin separator -t 'flroples' -n 20
```

#### show
Show available Python and Bash scripts.
Examples:
```
# Show Python scripts
admin show

# Show Bash scripts
admin show --bash
```

#### ssh
Add SSH public key to a host's `authorized_keys` file. 
Script relies on environmental variables. They can be difined in Linux envirnment file (.zshrc, for example):
```
# Variables from admin.ssh
export sc_name_1='vg'
export sc_user_1='vagrant'
export sc_key_1='/path/to/key'
export sc_pas_1='vagrant'

export sc_name_2=....
....
```
4 variables are mandatory, but you can have as many variable sets as you please, as long as they are numbered appropriately. 
To pick a set, define ADMIN_SSH_CRED and run the app.  

Couple things to note:
- Script uses key based authentication for the `-c` flag, and password authentication for `-k` flag
- If a key is already added, `sc_pas_*` can be an empty string
- Key itself is not created by the scrip, because it can easily be created by a one liner `ssh-keygen -P '' -q -f <path/to/key>`


**Examples**
```
# define credentials
ADMIN_SSH_CRED=vg

# add key to a host
admin ssh -h 192.168.56.111 -k

# run a single command on the host
admin ssh -h 192.168.56.111 -c 'ls -l /'
```

#### sysd
Create a systemd service or timer. 
Command creates a file in `/etc/systemd/system`, therefore requires sudo privileges.
Examples:
```
# Create a test service and a test timer
sudo admin sysd --service -f 'test.service' -v '{"desc": "Test service", "exec": "/home/labbrat/test.sh"}'
sudo admin sysd --timer   -f 'test.timer'   -v '{"desc": "Test timer", "service": "test.service", "time_interval": "00:00:00"}'
```
