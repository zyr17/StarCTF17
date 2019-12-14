#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

from Crypto.Util.number import *
def genkey(bits):
    while True:   
        p = getPrime(bits)
        q = getPrime(bits)
        n = p*q
        e = 65537
        phi = (p-1)*(q-1)
        if GCD(e,phi) == 1:
            d = inverse(e,phi)
            return p,q,n,e,d


def encrypt(n,e,data):
    num = bytes_to_long(data)
    return long_to_bytes(pow(num,e,n)).encode('hex')

def main():
    p,q,n,e,d = genkey(1024)
    print ("hint:we found n factor : n = {0}*{1}".format(p,q))
    print (encrypt(n,e,b"123"))

if __name__ == "__main__":
    main()
