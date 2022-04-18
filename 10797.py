date = int(input())
check = list(map(int, input().split()))
cnt = 0
for i in check:
    if i == date:
        cnt += 1
print(cnt)