#!/usr/bin/env python

import sys
import optparse

def main():
    try:length = int(sys.argv[1])
    except:print "[+] Usage : pattern_create.py <length>" % sys.argv[0]; sys.exit(1)

    string = ""
    seta = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    setb = "abcdefghijklmnopqrstuvwxyz"
    setc = "0123456789"
    a=0
    b=0
    c=0
    file = open("pattern.txt", "w")

    while (len(string)< length):
        string += seta[a] + setb[b] + setc[c]
        c += 1
        if c == len(setc):
            c = 0
            b = b + 1
        if b == len(setb):
            b = 0
            a = a + 1
        if a == len(seta):
            a = 0

    

    print "-----------------------------------------------------------------------"
    print string[:length]
    print "--------------------------------------------------------------------------"
    print "Length : %i" %length
    pattern = string[:length]
    file.write(pattern)


if __name__ == "__main__" :
    main()
