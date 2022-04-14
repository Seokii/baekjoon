n = int(input())

while True:
    checked = True
    for k in str(n):
        if k != '7' and k != '4':
            checked = False
    n -= 1
    if checked:
        print(n+1)
        break