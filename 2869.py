import math

a,b,v = map(int, input().split())
answer = (v-b) / (a-b)
print(math.ceil(answer))