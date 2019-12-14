#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 vam <m18639247977_1@163.com>
#
# Distributed under terms of the MIT license.

from Crypto.Util.number import *
from secret import flag

def genkey(bits):
    while True:
        p = getPrime(bits)
        q = getPrime(bits)
        e = 65537
        n = p*q
        phi = (p-1)*(q-1)
        if GCD(e,phi) == 1:
            d = inverse(e,phi)
            return p,q,n,e,d

p,q,n,e,d = genkey(512)

def encrypt(data):
    num = bytes_to_long(data)
    enc = pow(num,e,n)
    return long_to_bytes(enc).encode('hex')


def main():
    enc = encrypt(flag)
    print 'dp = {0}'.format(d%(p-1))
    print 'n = {0}'.format(n)
    print 'e = {0}'.format(e)
    print 'enc = {0}'.format(enc)

if __name__ == "__main__":
    main()
