#!/usr/local/bin/python

# Transform a plist xml export into hashcat format.
# Reads from STDIN

import xml.etree.ElementTree as ET
import sys

def main():
	for line in sys.stdin.readlines():
		root = ET.fromstring(line)
		for child in root.findall(".//data[1]"):
			entropy = child.text.replace(" ","").strip()
		for child in root.findall(".//integer[1]"):
			iterations = child.text.strip()
		for child in root.findall(".//data[2]"):
			salt = child.text.strip()
		print "$ml$"+iterations+"$"+salt+"$"+entropy

if __name__ == "__main__":
	main()

