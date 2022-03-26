#!/bin/bash

# run ansible playbook to install build-essential

# download and run installer
curl https://sh.rustup.rs -sSf | sh
source $HOME/.cargo/env

