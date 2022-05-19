This repository contains Vagrantfiles  
To use them, download the script locally and rename it to 'Vagrantifile' 

#### Prerequisites
- install Vagrant (RHEL based distros)
```
sudo dnf install vagrant
```
- create a directory named ```vagrant``` and generate keys
```
mkdir /home/$USER/vagrant
ssh-keygen -P '' -q -f /home/$USER/vagrant/vg_box
```
- rename one of the vagarnt files to ```Vagrantfile``` and place it in the directory
- run the script
```vagrant up```
- to stop VMs, run
```vagrant halt```  
\
\* Windows users might need to turn off antivirus when running script for the first time, because Vagrant will need to download images and antivirus might block it.

#### Contents
- ansible_nodes_2: create 2 VMs with static IPs on bridge adapter
- simple_nodes_2: create 3 VMs with static IPs on host-only adapter and NAT

