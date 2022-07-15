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
* for app_forms.yaml external library is required, to install:
```
ansible-galaxy collection install community.postgresql
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
* app_forms: install flask-masque web app, all the dependencies, PostgreSQL on AlmaLinux 8
* docker.yaml: install Docker on and enable in on Fedora Linux
* init_config.yaml: inistial OS configuration
* jenkins.yaml: install Jenkins as a Docker container on Fedora Linux (requires ```docker-compose.yaml``` file in ```configs``` directory)
* moderen_commands.yaml: install modern alternative to classic linux commands, line ```lsd``` for ```ls```, ```bat``` for ```cat``` etc.
