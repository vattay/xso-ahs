#!/usr/local/bin/python

import crypt
import sys
import hashlib
import binascii
import base64
from sys import argv

def testPass(entropy, iterations, salt):
	for word in open(sys.argv[1]).readlines():
		word = word.strip()
		wordEntropy = hashlib.pbkdf2_hmac('sha512', word, base64.b64decode(salt), int(iterations), 128)
		wordEntropyBase64 = base64.b64encode(wordEntropy)
		if (wordEntropyBase64 == entropy):
			print "[+] Found Password: " + word + "\n"
			return
	print "[-] Password not found"
	return

def main():
	counter = 1
	lines = sys.stdin.readlines()
	for line in lines:
		lineParts = line.split("$")
		iterations = lineParts[2].strip()
		salt = lineParts[3].strip()
		entropy = lineParts[4].strip()
		print "[*] Attempting to crack hash " + str(counter) + "/" + str(len(lines))
		testPass(entropy, iterations, salt)
		counter += 1;

if __name__ == "__main__":
	main()

