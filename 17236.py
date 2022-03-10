import math
h1 = float(input())
h2 = float(input())
h3 = float(input())

def heron(a,b,c):
    s = (a+b+c) / 2
    return math.sqrt(s * (s-a)*(s-b)*(s-c))

def judge(s):
    a = 2.0 * s / h1
    b = 2.0 * s / h2
    c = 2.0 * s / h3
    k = heron(a,b,c)
    differ = abs(s-k)
    if differ < 0.000001: return 0
    elif s > k: return 1
    else: return 2

answer = 0
left = 0
# right = float('inf')
right = 123456789.0
while (left < right):
    mid = (left+right) / 2
    tmp = judge(mid)
    if tmp == 0:
        answer = mid
        break
    elif tmp == 1: left = mid
    else: right = mid

print(answer)