#!/usr/bin/python
# Original code to xor a file into another file. NOT used by XorDecryptor.py.
# It is included in case you want to xor some plain text to test.

import sys
import detectEnglish

if len(sys.argv) != 4:
  print "Usage: ./xor1 infile outfile k"
  print "k is a one-character XOR key"
  print "For hexadecimal keys, use $'\\x01'"
  exit()

f = open(str(sys.argv[1]), "rb")
g = open(str(sys.argv[2]), "a")
k = ord(sys.argv[3])
result = ""

try:
    byte = f.read(1)
    while byte != "":
        xbyte = ord(byte) ^ k
        g.write(chr(xbyte))
        byte = f.read(1)
finally:
    f.close()

g.close()
