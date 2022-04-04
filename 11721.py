n = input()

answer = ""
for i in n:
    answer += i
    if len(answer) == 10:
        print(answer)
        answer = ""
print(answer)