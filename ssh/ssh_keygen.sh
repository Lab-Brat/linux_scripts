#!/bin/bash
key_name=$1
user=$2
pass=$3
host=$4
port=$5
user_ssh="$HOME/.ssh"

ssh-keygen -f "$user_ssh/$key_name" -P "" -q
#cat "$user_ssh/$key_name.pub"

sshpass -p $pass ssh-copy-id -o StrictHostKeyChecking=no \
	-i $user_ssh/$key_name -p $port $user@$host

cat << EOF >> "$user_ssh/config"
Host $host
	User $user
	Port $port
	IdentityFile $user_ssh/$key_name

EOF

