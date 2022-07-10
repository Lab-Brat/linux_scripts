# Linux scripts
## About the Repo
This is a collection of scripts, written to automate some daily linux administation tasks.

## Table of Contents
- [ansible](#ansible)
- [get_packs](#get_packs)
- [ssh](#ssh)
- [vagrant](#vagrant)
- [exitVim](#exitvim)
- [get-info](#get-info)
- [install-rust](#install-rust)
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

## install-rust
install rust on a linux machine

## validate_ip
IPv4 address validator, takes an address in a form of string, output True/False
