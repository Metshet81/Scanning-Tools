#!/bin/bash

# Check if 2 arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <target_ip> <nse_script_name>"
    echo "Example: $0 192.168.1.1 http-title"
    exit 1
fi

TARGET_IP=$1
NSE_SCRIPT=$2

# Run nmap with provided script
echo "Running Nmap scan on $TARGET_IP with NSE script: $NSE_SCRIPT"
nmap -sV --script="$NSE_SCRIPT" $TARGET_IP
