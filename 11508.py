n = int(input())
arr = []
answer = 0
cnt = 0
for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(len(arr)):
    if cnt != 2:
        cnt += 1
        answer += arr[i]
    elif cnt == 2:
        cnt = 0

print(answer)