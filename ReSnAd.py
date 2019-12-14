#! /usr/bin/env python
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
            assert d != 1
            dmp1 = d%(p-1)
            dmq1 = d%(q-1)
            iqmp = inverse(q,p)
            ipmq = inverse(p,q)
            return p,q,n,e,phi,d,dmp1,dmq1,iqmp,ipmq

p,q,n,e,phi,d,dmp1,dmq1,iqmp,ipmq = genkey(1024)

assert e == 65537

def encrypt(data):
    num = bytes_to_long(data)
    result = pow(num,e,n)
    return long_to_bytes(result)

def decrypt(data):
    num = bytes_to_long(data)
    v1 = pow(num, dmp1, p)
    v2 = pow(num, dmq1, q)
    result = (v2*p*ipmq + v1*q*iqmp) % n
    return long_to_bytes(result)
    

def hint_msg():
    print "[+]hint:[e = {0},phi = {1},iqmp = {2},ipmq = {3}]".format(e,phi,iqmp,ipmq)

def main():
    flag = "fff"
    enc = encrypt(flag)
    assert decrypt(enc) == flag
    hint_msg()
    print enc.encode('hex')

if __name__ == '__main__':
    main()



