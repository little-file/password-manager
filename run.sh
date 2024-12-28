#!/bin/bash

echo "version 0.4.1"

echo "1 for native and q for quit enter:" 
read input 
if [ "$input" = "d" ]; then
    docker build -t passwordmanager:latest src/.
    docker run -it --name password-manager passwordmanager:latest
    exit 0 
elif [ "$input" = "1" ]; then
    python src/main.py
    exit 0 
elif [ "$input" = "q" ]; then
    exit 0 
else
    echo "unknow input"
fi