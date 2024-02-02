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
   - [ssh](#ssh)

## Set Up
Clone the repository and navigate to it
```bash
git clone https://github.com/Lab-Brat/linux_scripts.git
```  

Then, install virtual enironment and build the app with setup.py
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install .
ladm --help
```

## Using
#### bash
Show available Bash scripts or run them.
Examples:
```
# Show Bash scripts
ladm bash show

# Show Bash scripts
ladm bash --run <script.sh>
```

#### ipfind
Use locally installed `whois` command to find information about IP provider 
and parse the output.
Examples:
```
# find IP provider info of address 8.8.8.8
ladm ipfind -i 8.8.8.8
```

#### sensfind
Do a recursive search on a specified directory to look for IP addresses 
and passwords. 
Might come in handy to check sensitive info in a git repository 
before pushing it.
Examples:
```
# Search for sensitive info in current directory
ladm sensfind -p ./
```

#### separator
Create a line separator for scripts. 
Default value is 79, which is recommend line length for Python code.
Examples:
```
# Print a separator line titled 'florples', length = 79
ladm separator -t 'flroples'

# Print a separator line titled 'florples', length = 20
ladm separator -t 'flroples' -n 20
```

#### ssh
A tool that configures `~/.ssh/config` via a yaml file that support 
editing it via CLI instead of doing it manually.  

Configuration file is stored in `~/.ladm/ssh_conf.yaml`, and looks 
something like this:
```yaml
general_settings:
- ServerAliveInterval 120
- IdentitiesOnly yes
- StrictHostKeyChecking no
identities:
  personal:
  - User labbrat
  - IdentityFile /path/to/personal_key
  root:
  - User root
  - IdentityFile /path/to/root_key
pairings:
  host1:
    host:
    - hostname-1.com
    - hostname-2.com
    identity: personal
    options: []
  host2:
    host:
    - hostname-3-*.com
    identity: root
    options:
    - Port 69
```

And here are some example of how to use it:
```bash
# overwrite ~/.ssh/config with yaml configuraion
ladm ssh -a

# update identity of a host and write ssh/config
ladm ssh -u 'host2 identity x personal' -a

# show yaml config
ladm ssh -s
```
