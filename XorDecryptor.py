#!/usr/bin/python
# detectEnglish taken from http://inventwithpython.com/detectEnglish.py
# Xor code taken from https://samsclass.info/124/proj14/p13-xor.htm
# Put together by eldraco@gmail.com with some minor modifications
#
# Description:
# Take a xored file, try all the 1byte-long hexa values as xor keys and search if each result is english. If it is, say so.
#
# Example usage:
# 
# 1- create a english text:
# echo "This is an example english text" > example
#
# 2- Xor it with the letter 'm' as key
# ./xor.py example example.xor m
#
# 3- Now lets try to automatically detect which was the key, and if it was english.
# ./XorDecryptor.py example.xor
# English detected with key: 109 (m): This is an example english text


import sys
import detectEnglish

if len(sys.argv) != 2:
  print "Usage: ./xor1 xoredfile"
  exit()

f = open(str(sys.argv[1]), "rb")
result = ""

try:
    start = 0x00
    end = 0xff
    byte = f.read(1)
    for k in xrange(start, end):
        while byte != "":
            xbyte = ord(byte) ^ k
            result += chr(xbyte)
            byte = f.read(1)
        # If you need to see each ouput (maybe because you are not searchinf for english) uncomment next line
        #print result
        isEnglish = detectEnglish.isEnglish(result)
        if isEnglish:
            print 'English detected with key: {} ({}): {}'.format(k,chr(k),result)
        f.close()
        f = open(str(sys.argv[1]), "rb")
        byte = f.read(1)
        result = ""
finally:
    f.close()

