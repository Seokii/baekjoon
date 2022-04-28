n = int(input())
for _ in range(n):
    answer = ''
    sentence = list(input())
    if 97 <= ord(str(sentence[0])) <= 122:
        sentence[0] = chr(ord(sentence[0])-32)
    for i in sentence:
        answer += i
    print(answer)

# easy code
"""
for _ in range(int(input())):
    c = list(input())
    c[0] = c[0].upper()
    print("".join(c))
"""
