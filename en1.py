def func(l, r, k):
    res = 0
    for i in range(l, r + 1):
        sum = 0
        while i > 0:
            sum += i % 10
            i /= 10
        if sum == k:
            res += 1
    return res

import os,socket,subprocess
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('pwn.sixstars.team',23201))

input = s.recv(1000)
print(input)
count = 0
start_time = time.time()
while True:
    count += 1
    input = str(s.recv(1000)).strip()
    if len(input) != 0:
        print(count, time.time() - start_time, input)
    if input[:6] == 'fductf' or len(input) == 0:
        continue
    input = map(int, str(input).strip().split(' '))
    res = func(*input)
    s.send(bytes(str(res)))