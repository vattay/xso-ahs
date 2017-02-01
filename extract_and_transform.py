#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import os
import subprocess
import fnmatch
import xml.etree.ElementTree as ET
import string


class Extractor:
    basepath = '/var/db/dslocal/nodes/Default/users/'

    def get_user_plist_filenames(self):
        files = []
        for filename in os.listdir(self.basepath):
            if fnmatch.fnmatch(filename, '[!_|!nobody]*.plist'):
                files.append(filename)

        return files

    def get_plist_contents_from(self, filename):
        path = self.basepath + filename
        result = subprocess.run([
            u"sudo /usr/bin/defaults read {}".format(path) +
            u" ShadowHashData 2>/dev/null|tr -dc 0-9a-f|xxd -r -p|" +
            u"plutil -convert xml1 - -o -"
        ], universal_newlines=True, shell=True,
           stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        return result.stdout

    def remove_whitespace(self, hash_str):
        return hash_str.translate({
            ord(x): '' for x in set(string.whitespace)
        })

    def parse_plist(self, plist_str):
        root = ET.fromstring(plist_str)
        for child in root.findall(".//data[1]"):
            entropy = child.text.replace(" ", "").strip()
        for child in root.findall(".//integer[1]"):
            iterations = child.text.strip()
        for child in root.findall(".//data[2]"):
            salt = child.text.strip()

        return {
            "entropy": entropy,
            "iterations": iterations,
            "salt": salt
        }

    def format_hash(self, hash_components):
        hash_str = self.remove_whitespace(
            u"$ml$" +
            hash_components["iterations"] +
            u"$" +
            hash_components["salt"] +
            u"$" +
            hash_components["entropy"]
        )
        return hash_str

    def make_crypt_format(self, user, hash_str):
        fmtd = "{}:{}".format(user, hash_str)
        return fmtd

    def extract_password_hashes(self):
        hashes = []
        files = self.get_user_plist_filenames()
        for filename in files:
            user = filename.split('.')[0]
            plist_contents = self.get_plist_contents_from(filename)
            try:
                hash_components = self.parse_plist(plist_contents)
                formatted_hash = self.format_hash(hash_components)
                hashes.append(self.make_crypt_format(user, formatted_hash))
            except:
                hashes.append(u"Oops! Something went wrong trying to extract" +
                              u" {}'s password hash!".format(user))
        return hashes


if __name__ == '__main__':
    extractor = Extractor()
    hashes = extractor.extract_password_hashes()
    for hash_val in hashes:
        print(hash_val)
