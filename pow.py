#!/usr/bin/env python
# coding=utf-8

import SocketServer
import signal
import os
import random
import string
from hashlib import sha256
from secret import flag
from Crypto.Util.number import *


class handler(SocketServer.BaseRequestHandler):
    def send(self, msg):
        self.request.sendall(msg+b'\n')

    def recv(self, n):
        return self.request.recv(n)

    def exit(self, msg):
        self.send(msg)
        self.request.close()
        exit()

    def proof_of_work(self):
        proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
        proof = proof.encode('ascii')
        digest = sha256(proof).hexdigest()
        self.send("sha256(XXXX+{0}) == {1}".format(proof[4:],digest))
        self.send(b'Give me XXXX:')
        x = self.recv(4)
        if len(x) != 4 or sha256(x+proof[4:]).hexdigest() != digest: 
            self.exit(b'No no no :(')
    

    def handle(self):
        signal.alarm(400)
        self.proof_of_work()
        signal.alarm(300)
        self.send(flag)
        self.request.close()

class ForkingServer(SocketServer.ForkingTCPServer, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 13337
    ForkingServer.allow_reuse_address = True
    server = ForkingServer((HOST, PORT), handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutdown!')
        server.shutdown()
