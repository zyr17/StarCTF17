
import os,socket,subprocess
import math
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('pwn.sixstars.team',23203))

buffer = []
lines = []

def readint():
    global buffer
    global lines
    if len(buffer) == 0:
        while True:
            if len(lines) == 0:
                input = str(s.recv(10000000), 'ascii').strip().split('\n')
                lines += input
            input = lines[0]
            lines = lines[1:]
            print(input)
            if str(input[:6]) == 'fductf':
                continue
            input = map(int, input.split(' '))
            buffer += input
            break
    ret = buffer[0]
    buffer = buffer[1:]
    return ret

def cmp(input):
    x, y = input
    a = 0
    if x < 0 and y >= 0:
        a = 1
    if x <= 0 and y < 0:
        a = 2
    if x > 0 and y <= 0:
        a = 3
    return 10000 * a + math.atan2(y, x)

def chaji(x, y):
    return (x[0] * y[1] - x[1] * y[0]) / 2

def check(input):
    input.append(input[0])
    res = 0
    for x, y in zip(input[:-1], input[1:]):
        res += chaji(x, y)
    return abs(res)

def func():
    n = readint()
    points = []
    for i in range(n):
        x = readint()
        y = readint()
        points.append([x, y])
    points.sort(key = cmp)
    res = [0]
    for i in points:
        for j in points:
            for k in points:
                for l in points:
                    now = check([i, j, k, l])
                    if now > res[0]:
                        res = [now, i, j, k, l]
    print(res)
    return res[0]

input = s.recv(12)
print(input)
input = s.recv(13)
print(input)
while True:
    res = func()
    s.send(bytes(str(res), 'ascii'))