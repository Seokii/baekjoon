n = int(input())
answer = 0

for _ in range(n):
    time = input().split()
    tmp = []
    for i in range(int(time[1])):
        tmp.append(int(time[0].replace(":",""))+i)
    for i in tmp:
        cal = i % 100
        if cal // 60 == 1: i += 40
        if 700 <= i < 1900: answer += 10
        else: answer += 5

print(answer)