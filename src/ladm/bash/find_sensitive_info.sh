#!/bin/bash

# Read a string of excluded directories,
# return a list of type ['--exclude-dir', 'dir', ...]
function split_dir {
    exclude_dir="$1"
    if [[ -z "$exclude_dir" ]]; then
        echo ""
    else
        IFS=","
        for dir in $exclude_dir; do
            printf -- "--exclude-dir=%s " "$dir"
        done
    fi
}

# Grep regular expressions, output all matches.
function find_info {
    path="$1"
    exclude_dir="$2"

    ip_regex="\\b([0-9]{1,3}\\.){3}[0-9]{1,3}\\b"
    exclude_flags=$(split_dir "$exclude_dir")

    echo "Found IP addresses:"
    grep -roE "$ip_regex" "$path" $exclude_flags

    echo "Found 'password' keywords:"
    grep -ri "password" "$path" $exclude_flags

    echo "Found Passwords:"
    password_regex="\b(?=\w*[a-z])(?=\w*[A-Z])(?=\w*\d)\w{6,}\b"
    grep -rioP "$password_regex" "$path" $exclude_flags
}

if [[ $# -lt 1 ]]; then
    echo "[ERROR!] Please specify grep location"
    exit 1
fi

path="$1"
exclude_dir="${2:-venv,__pycache__}"

if [[ -z "$2" ]]; then
    echo "[WARNING!] exclude-dir not specified, using defaults: venv,__pycache__"
fi

find_info "$path" "$exclude_dir"
