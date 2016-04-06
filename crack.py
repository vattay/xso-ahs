import crypt
import sys
import xml.etree.ElementTree as ET
import hashlib
import binascii
import base64
from sys import argv

def testPass(entropy, iterations, salt, dictionaryFile):
	for word in dictionaryFile.readlines():
		word = word.strip('/n')
		wordEntropy = hashlib.pbkdf2_hmac('sha512', word, base64.b64decode(salt), int(iterations), 128)
		if (base64.b64encode(wordEntropy) == entropy):
			print "[+] Found Password: " + word + "\n"
			return
	print "[-] Password not found"
	return

def main():
	dictionaryFile = open(sys.argv[1])

	for line in sys.stdin.readlines():
		root = ET.fromstring(line)
		for child in root.findall(".//data[1]"):
			entropy = child.text.replace(" ","").strip()
		for child in root.findall(".//integer[1]"):
			iterations = child.text
		for child in root.findall(".//data[2]"):
			salt = child.text
		testPass(entropy, iterations, salt, dictionaryFile)

if __name__ == "__main__":
	main()

