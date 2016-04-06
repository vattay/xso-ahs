# xso-ahs
How to retrieve OSX 10.7+ hashes and a toy  dictionary attack.

As of OSX 10.7 password hashes are stored in separate plist files per user. 
This script combines some known bash shortcuts to get at these hashes, if you have root access.

It also has a dictonary cracker, mainly as an example of how to extend the password cracker example from
[Violent Python](http://www.amazon.com/Violent-Python-Cookbook-Penetration-Engineers/dp/1597499579) to modern OSX.

The cracker IS a toy, it is very slow. Use a real cracker or fork this and improve it if you actually want it to
finish before the sun runs out with a large dictionary.
