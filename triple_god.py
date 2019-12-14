from random import choice as c
from itertools import permutations as p

white_list = ['==','(',')','A','B','C','X','0','1','2']

import os,string,signal
import random
import SocketServer
from hashlib import sha256
from Crypto.Util.number import *
import time
import sys

log = open('t.out', 'w')

class Task:
    def proof_of_work(self):
        return True
    def dosend(self, msg):
        print(msg)
        sys.stdout.flush()
        log.write('server: ' + msg + '\n')
        log.flush()
    def calc(self,gods, ans, mask_gods, X, i, expr):
        try:
            A, B, C = mask_gods
            r = eval(expr)
        except Exception as e:
            self.dosend("Nonsense!" +  str(e))
            exit(0)
        return ans[X](gods[mask_gods[i]](r))

    def do_round(self):
        truth=lambda r: not not r
        lie=lambda r: not r
        chaos=lambda r: c((True, False))
        gods =(truth, lie, chaos)
        ans = (truth, lie)
        mask_gods = c(list(p(range(len(gods)))))
        mask_ans = c(range(len(ans)))
        for _ in range(3):
            self.dosend("You may ask a question:")
            inp=self.recv(1024).split(" ")
            question = [word for word in inp if word in white_list]
            print question
            self.dosend('One of the gods answered "{}"\n'.format(self.calc(gods, ans, mask_gods, mask_ans, int(question[0]), "".join(question[1:]))))

        self.dosend("Now reveal their identites:" + str(mask_gods))
        return mask_gods == tuple(map(int, self.recv(1024).split(" ")))

    def recv(self, sz):
        while True:
            res = raw_input().strip()
            if len(res) != 0:
                break
        log.write('client: ' + res + '\n')
        log.flush()
        return res
    def handle(self):
        if not self.proof_of_work():
            exit(0)
        for i in range(50):
            if not self.do_round():
                self.dosend("Nonsense!\n")
                exit(0)
            else:
                self.dosend("Good.\n")
        self.dosend("Well played. \n")
        exit(0)
        
        
task = Task()
task.handle()




