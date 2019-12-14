import os,random, string,signal,datetime
import SocketServer
from hashlib import sha256
from random import getrandbits

class Task(SocketServer.BaseRequestHandler):
	def proof_of_work(self):
		random.seed(os.urandom(8))
		proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in xrange(20)])
		digest = sha256(proof).hexdigest()
		self.request.send("sha256(XXXX+%s) == %s\n" % (proof[4:],digest))
		self.request.send('Give me XXXX:')
		x = self.request.recv(10)
		x = x.strip()
		if len(x) != 4 or sha256(x+proof[4:]).hexdigest() != digest: 
		    return False
		return True
	def dosend(self, msg):
		try:
		    self.request.sendall(msg)
		except:
		    pass
	def recv(self, sz):
		try:
		    r = sz
		    res = ''
		    while r>0:
		        res += self.request.recv(r)
		        if res.endswith('\n'):
		            r = 0
		        else:
		            r = sz - len(res)
		    res = res.strip()
		except:
		    res = ''
		return res
	def handle(self):
		signal.alarm(60)
		if not self.proof_of_work():
			exit(0)
		signal.alarm(30)
		seed=os.urandom(8)
		random.seed(seed)
		self.dosend(seed.encode('hex')+'\n')
		with open('flag1') as f:
			flag=f.read().strip()
		while True:
			self.dosend('input your number:\n')
			rec=self.recv(200)
			ans=getrandbits(32)
			if rec==str(ans):
				self.dosend("here's your reward:"+flag+'\n')
				exit(0)
			else:
				self.dosend("last lucky number:"+str(ans)+'\n')
        
class ForkingServer(SocketServer.ForkingTCPServer, SocketServer.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10005
    ForkingServer.allow_reuse_address = True
    server = ForkingServer((HOST, PORT), Task)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutdown!')
        server.shutdown()
