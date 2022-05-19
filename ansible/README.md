# Ansible Scripts
## About the directory
Directory contains configuration files and ansible playbooks.  
They are meant to be used together with the Vagrant setup at ../vagrant.  

## Install
* install ansible
```
python3 -m pip install ansible
```
* append your nodes to the ```inventory``` file at /etc/hosts
* for jenkins.yaml external library is required, to install:
```
ansible-galaxy collection install community.docker
```  

## Run
* test connectivity with the nodes:  
```
ansible all -m ping
```
* if to connection is established, run the playbook: 
```
ansible-playbook -i inventory <playbook>.yaml
```

## Playbooks
* docker.yaml: install Docker on and enable in on Fedora Linux
* jenkins.yaml: install Jenkins as a Docker container on Fedora Linux
* init_config.yaml: inistial OS configuration

