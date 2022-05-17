# Ansible Scripts
## About the directory
Directory contains configuration files and ansible playbooks.
They are meant to be used together with the Vagrant setup at ../vagrant.

## Install
* install ansible  
```python3 -m pip install ansible```
* append your nodes to the hosts file at /etc/hosts

## Run
* test the connectivity with the nodes  
```ansible all -m ping```
* if the connectivity is established, run playbook  
```ansible-playbook -i inventory <playbook>```

## Playbooks
* docker.yaml: install Docker on and enable in on Fedora server
* init_config.yaml: inistial OS configuration
