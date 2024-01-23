#!/bin/bash

vim_num=$(ps aux | grep vim | wc -l)

if [ $vim_num -gt 1 ]; then
    pids=$(ps aux | grep vim | head -n $(($vim_num - 1)) | awk '{print $2}')
    for value in $pids; do
        echo "[# Terminating Process $value #]"
        sudo kill -9 $value
    done

else
    echo "[# Vim is NOT Running #]"
fi
