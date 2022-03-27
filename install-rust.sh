#!/bin/bash

# detect os and install build-essential
osfam=$(cat /etc/os-release | grep -i id_like | tr -d '"' | sed 's/.*=//')
if [ "$osfam" == 'debian' ]; then
	sudo apt install build-essential
else
	sudo dnf group install "Development Tools"
fi

# download and run installer
curl https://sh.rustup.rs -sSf | sh
source $HOME/.cargo/env

