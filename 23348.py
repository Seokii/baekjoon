a,b,c = map(int, input().split())
n = int(input())
answer = 0

for _ in range(n):
    tmp = 0
    for _ in range(3):
        cal1,cal2,cal3 = map(int, input().split())
        tmp += cal1*a + cal2*b + cal3*c
    if tmp > answer:
        answer = tmp

print(answer)