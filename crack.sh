#!/bin/bash

usage="$0 <dictionary file path>"

if [ $# -eq 0 ]; then
	echo "Missing argument: $usage"
	exit 1
fi

echo "[*] Starting..."
sudo ./extract_plists.sh | ./transform.py | ./crack.py "$1"
echo "[*] Done." 