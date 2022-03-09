n = int(input())
store = list(map(int, input().split()))
prev = 0
answer = 0
not_first = False

for i in store:
    if prev == 0 and i == 0 and not_first == False:
        answer += 1
        prev = 0
        not_first = True
    elif prev == 0 and i == 1 and not_first == True:
        answer += 1
        prev = 1
    elif prev == 1 and i == 2 and not_first == True:
        answer += 1
        prev = 2
    elif prev == 2 and i == 0 and not_first == True:
        answer += 1
        prev = 0

print(answer)