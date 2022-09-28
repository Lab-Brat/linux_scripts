# Linux scripts
## About the Repo
This repository is a collection of scripts, written to automate some daily linux administation tasks.

## Table of Contents
- [ansible](#ansible)
- [get_packs](#get_packs)
- [ssh](#ssh)
- [vagrant](#vagrant)
- [exitVim](#exitvim)
- [get-info](#get-info)
- [find_sensinfo](#find_sensinfo)
- [install-rust](#install-rust)
- [show_plan](#show_plan)
- [validate_ip](#validate_ip)
 
## ansible
collection of ansible playbooks

## get_packs
download all package dependencies from the repository

## ssh
scripts to automate ssh key creation

## vagrant
storage for different Vagrantfiles

## exitVim
my [pull request](https://github.com/hakluke/how-to-exit-vim/pull/246) (not accepted yet) to the [how-to-exit-vim](https://github.com/hakluke/how-to-exit-vim) repository.  
essentially, the script kills active vim session using cron job.  To use the script, put ```exitVim.sh``` in the ```$HOME``` directory.  
Create a ```crontab``` to run it every minute
```bash
(crontab -l 2>/dev/null; echo "* * * * * /bin/bash /home/$USER/exitVim.sh") | crontab -
```  
Profit! 

## get-info
output system specs: CPU, RAM, free space etc.

## find_sensinfo
find IP address and password in a every file.

## install-rust
install rust on a linux machine

## show_plan
read ```__PLAN__.md``` and echo the things planned for current month.  
Available options:
* all  : show plan for all the months
* next : show plan for next month
Example of a plan
```
#### Programming
Python
* Fluent Python (AugSep2022)
C
* Dr. Chukc's C Youtube course (Sep2022)
Javascript
* Udemy course
```
the script will use ```date``` command to find current month (Aug,Sep,Oct etc.) in the plan, and then print the line without the part in the parentheses.

## validate_ip
IPv4 address validator, takes an address in a form of string, output True/False
