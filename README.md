# xso-ahs

Extract OSX 10.7 password hashes (SHA512, salted, PBKDF2) as XML, one line hashes.

## Info

As of OSX 10.7 password hashes are stored in separate plist files per user. 
This script combines some known bash shortcuts to get at these hashes, if you have root access.

The ```extract_plists.sh``` just pulls out the hash data in xml format.

The ```transform.py``` script transforms this into a one line hash, which includes the iterations and salt.

It also has a dictonary cracker, ```crack.py```, mainly as an example of how to extend the password cracker example from
[Violent Python](http://www.amazon.com/Violent-Python-Cookbook-Penetration-Engineers/dp/1597499579) to modern OSX.

The cracker *IS* a toy, it is very slow. Use a real cracker or fork this and improve it if you actually want it to finish before the sun runs out with a large dictionary.

## How to use
Run the whole pipeline with

```sudo ./crack.sh dictionary.txt```

You can also just extract the plist xml like this:

```sudo ./extract_plists```

Or get them as one line hashes:

```sudo ./extract_plists.sh | ./transform.py```

Or run the whole thing without the top level script:

```sudo ./extract_plists.sh | ./transform.py | ./crack.py dictionary.txt```
