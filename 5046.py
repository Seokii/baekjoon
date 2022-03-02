n,b,h,w = map(int, input().split())
answer = []
for _ in range(h):
    p = int(input())
    a = list(map(int, input().split()))
    if max(a) >= n and b >= p*n:
        answer.append(p*n)

if len(answer) == 0:
    print("stay home")
else:
    print(min(answer))