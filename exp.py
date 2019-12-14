#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 zzj <m18639247977_1@163.com>
#
# Distributed under terms of the MIT license.
from pwn import *
from pwnlib.util.iters import bruteforce
import sys
import hashlib
from Crypto.Util.number import *
import numpy as np
context.log_level = "debug"
def hash(x):
    return hashlib.sha256(x).hexdigest()

class inout():
    def __init__(self):
        self.buf = ''
    def recvuntil(self, string):
        length = len(string)
        res = ''
        while len(res) < length or res[-length:] != string:
            while self.buf == '':
                self.buf = raw_input()
            res += self.buf[0]
            self.buf = self.buf[1:]
        return res
    def sendline(self, string):
        print(string + '\n')
        sys.stdout.flush()


def rev1(i):
    top14 = i >> 18
    last14 = (i & 0x00003fff) ^ top14
    mid4 = (i & 0x0003ffff) >> 14
    print (hex(top14), hex(mid4), hex(last14))
    return (top14 << 18) + (mid4 << 14) + last14
def rev2(i):
    last17 = i & 0x001ffff
    top15 = (((last17 << 15) & 0xefc60000) ^ i) >> 17
    return (top15 << 17) + last17
def rev3(i):
    last7 = i & 0x7f
    midlast7 = ((i & 0x3fff) >> 7) ^ (last7 & 0x2d)
    mid7 = ((i & 0x1fffff) >> 14) ^ (midlast7 & 0x31)
    midtop7 = ((i & 0xfffffff) >> 21) ^ (mid7 & 0x69)
    top4 = i >> 28 ^ (midtop7 & 0x9)
    result = (top4 << 28) + (midtop7 << 21) + (mid7 << 14) + (midlast7 << 7) + last7
    print hex(result)
    return result
def rev4(i):
    top11 = i >> 21
    mid11 = ((i & 0x1fffff) >> 10) ^ top11
    last10 = (i & 0x3ff) ^ (mid11 >> 1)
    return (top11 << 21) + (mid11 << 10) + last10

def expPow():
    
    r.recvuntil('sha256(XXXX+')
    prefix = r.recvuntil(')')[:-1]
    print prefix
    r.recvuntil('== ')
    result = r.recvline()[:-1]
    print result
    x = bruteforce(lambda x:hash(x+prefix)==result,string.ascii_letters+string.digits,length=4,method='downfrom')
    r.sendline(x)
    '''
    #六星福利彩票2
    r.sendline('0\n')
    number = r.recvuntil('last lucky number:')
    number = r.recvuntil('\n')[:-1]
    print(number)
    seed = rev4(rev3(rev2(rev1(int(number)))))
    seed=(seed*25214903917+11)&0xffffffff
    res=seed
    res^=(res>>11)
    res^=(res<<7)&0x9d2c5680
    res^=(res<<15)&0xefc60000
    res^=(res>>18)
    r.sendline(str(res))
    return
    '''
    '''
    #六星福利彩票1
    seed = r.recvuntil('\n')[:-1]
    print(seed)
    random.seed(seed[13:].decode('hex'))
    for i in range(10):
        r.sendline(str(random.getrandbits(32)))
        result = r.recvline()[:-1]
        sleep(0.01)
    '''
    
    #宝藏和鹦鹉
    for i in range(50):
        guess = [0, 0, 0]
        for j in range(3):
            r.recvuntil('Ask the parrot:')
            r.sendline('%s == 1' % 'ABC'[j])
            r.recvuntil('parrot: ')
            guess[j] = r.recvuntil('\n')[0] == 'T'
        diff = [0] * 3
        print(guess)
        for x in range(3):
            y = (x + 1) % 3
            r.recvuntil('Ask the parrot:')
            r.sendline('%s == %s' % ('ABC'[x], 'ABC'[y]))
            r.recvuntil('parrot: ')
            result = r.recvuntil('\n')[0] == 'T'
            if result != (guess[x] == guess[y]):
                diff[x] += 1
                diff[y] += 1
        for i in range(3):
            if diff[i] == 2:
                guess[i] = not guess[i]
        print(diff, guess)
        r.sendline(' '.join(['1' if x else '0' for x in guess]))
    
    '''
    for i in range(50):
        r.sendline('0 ( X == 0 ) == ( ( A == 0 ) == ( C == 2 ) )')
        r.recvuntil('answered "')
        res = r.recvuntil('"')[0] == 'T'
        if res:
            r.sendline('1 ( X == 0 ) == ( ( B == 0 ) == ( A == 2 ) )')
            r.recvuntil('answered "')
            resAe2 = r.recvuntil('"')[0] == 'T'
            r.sendline('1 ( X == 0 ) == ( ( B == 0 ) == ( B == 1 ) )')
            r.recvuntil('answered "')
            resBe1 = r.recvuntil('"')[0] == 'T'
            if resAe2 and resBe1:
                r.sendline('2 1 0')
            elif resAe2:
                r.sendline('2 0 1')
            elif resBe1:
                r.sendline('0 1 2')
            else:
                r.sendline('1 0 2')
        else:
            r.sendline('2 ( X == 0 ) == ( ( C == 0 ) == ( A == 2 ) )')
            r.recvuntil('answered "')
            resAe2 = r.recvuntil('"')[0] == 'T'
            r.sendline('2 ( X == 0 ) == ( ( C == 0 ) == ( C == 1 ) )')
            r.recvuntil('answered "')
            resCe1 = r.recvuntil('"')[0] == 'T'
            if resAe2 and resCe1:
                r.sendline('2 0 1')
            elif resAe2:
                r.sendline('2 1 0')
            elif resCe1:
                r.sendline('0 2 1')
            else:
                r.sendline('1 2 0')
    '''
    '''
    #数学作业
    r.recvuntil('N=')
    N = int(r.recvuntil('\n')[:-1])
    r.recvuntil('n=')
    n = int(r.recvuntil('\n')[:-1])
    r.sendline(str(n))
    r.recvuntil('=')
    r.sendline(str(n))
    r.recvuntil('=')
    r.sendline(str(n))
    r.recvuntil('=')
    a=1
    for i in range(N-n+1,N):
        a*=i
        a=a%N
    a=inverse(-a,N)
    r.sendline(str(a))
    '''
'''
#先赚一个小目标
baseprice = np.array([15, 40, 199, 690, 3500, 25000, 130000])
updown = np.array([0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.5])
def get_price():
    res = []
    for i in range(7):
        r.recvuntil('价值：', 'utf8')
        res.append(int(r.recvuntil('\n')[:-1]))
    r.recvuntil('操作', 'utf8')
    return np.array(res)
def action(act, op1 = None, op2 = None):
    r.sendline(act)
    if op1 != None:
        r.recvuntil('请', 'utf8')
        r.sendline(op1)
        r.recvuntil('请', 'utf8')
        r.sendline(op2)
        r.recvuntil('ENTER')
        r.sendline('')
        r.recvuntil('操作', 'utf8')
def sell():
    r.sendline('')
    nowmoney = 3500
    nowitem = 0
    amount = 0
    for i in range(30):
        print('----- ROUND %02d -----' % (i + 1))
        price = get_price()
        print(nowmoney, nowitem, amount)
        delta = np.array(price, dtype='float') / baseprice
        for i in range(7):
            if nowmoney + price[nowitem] * amount < price[i]:
                delta[i] = 2
        print(price, delta)
        choice = np.argmin(delta)

        if price[choice] < baseprice[choice]:
            nowmoney += price[nowitem] * amount
            action('b', str(nowitem + 1), str(amount))
            nowitem = choice
            amount = nowmoney // price[nowitem]
            nowmoney -= price[nowitem] * amount
            action('a', str(nowitem + 1), str(amount))
        elif price[nowitem] > baseprice[nowitem]:
            action('b', str(nowitem + 1), str(amount))
            nowmoney += price[nowitem] * amount
            amount = 0
        action('c')
        print(nowmoney, nowitem, amount)
        print(price, np.array(delta))
'''
r = remote("pwn.sixstars.team",23200)
r = inout()
#sell()
expPow()
r.interactive()

