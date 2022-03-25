t = int(input())

for _ in range(t):
    arr = list(input())
    answer = 0
    cnt = 0
    for i in arr:
        if i == 'O':
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    print(answer)
    answer = 0