#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
from Crypto.Util.number import *
from secret import flag

p = getPrime(1024)

def genkey(bits):
    while True:
        q = getPrime(1024)
        n = p*q
        e = 65537
        if GCD(e,(p-1)*(q-1)) == 1:
            return n,e


def encrypt(n,e,data):
    num = bytes_to_long(data)
    return long_to_bytes(pow(num,e,n)).encode('hex')


def main():
    n1,e1 = genkey(1024)
    print n1
    print encrypt(n1,e1,flag)
    n2,e2 = genkey(1024)
    print n2
    print encrypt(n2,e2,flag)

if __name__ == "__main__":
    main()

