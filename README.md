# Linux scripts
## About the Repo
This repository is a collection of scripts, written to automate some daily linux administation tasks.

## Table of Contents
- [get_packs](#get_packs)
- [systemd_service](#systemd_service)
- [vagrant](#vagrant)
- [admin](#admin)
- [create_boundary](#create_boundary)
- [exitVim](#exitvim)
- [get-info](#get-info)
- [find_ip_info](#find_ip_info)
- [find_sensinfo](#find_sensinfo)
- [show_plan](#show_plan)
- [ssh_connect](#ssh_connect)
- [validate_ip](#validate_ip)

## get_packs
Download all package dependencies from the repository.

## systemd_service
Python script that creates systemd service and timer.

## vagrant
Storage for different Vagrantfiles.

## admin
One script to run them all.

## create_boundary
Dynamically create line separators in Python programs.

## exitVim
My [pull request](https://github.com/hakluke/how-to-exit-vim/pull/246) (not accepted yet) to the [how-to-exit-vim](https://github.com/hakluke/how-to-exit-vim) repository.  
essentially, the script kills active vim session using cron job.  To use the script, put ```exitVim.sh``` in the ```$HOME``` directory.  
Create a ```crontab``` to run it every minute.
```bash
(crontab -l 2>/dev/null; echo "* * * * * /bin/bash /home/$USER/exitVim.sh") | crontab -
```  
Profit! 

## get-info
Output system specs: CPU, RAM, free space etc.

## find_ip_info
Find IP address provider using whois or API.

## find_sensinfo
Find IP address and password in a every file.

## show_plan
Read ```__PLAN__.md``` and echo the things planned for current month.  
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

## ssh_connect
Script that assists with SSH connection and SSH config management.

## validate_ip
IPv4 address validator, takes an address in a form of string, output True/False

