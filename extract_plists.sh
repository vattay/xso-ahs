#!/bin/bash

pat="^[0-9a-zA-Z ]{1,}\.plist"
xml_pat="^<\?xml.*"

if [[ $EUID -ne 0 ]]; then
	echo "[-] Not running as root, you probably won't see any results."
fi

for f in /var/db/dslocal/nodes/Default/users/*
do
	basefile=$(basename $f)
	if [[ $basefile =~ $pat ]]; then
		xml=$(defaults read $f ShadowHashData 2>/dev/null|tr -dc 0-9a-f|xxd -r -p|plutil -convert xml1 - -o -)
		if [ $? -eq 0 ]; then
			if [[ $xml =~ $xml_pat ]]; then
				echo $xml
			fi	
		fi
	fi
done
