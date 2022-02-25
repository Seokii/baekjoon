n, l = map(int, input().split())
h = list(map(int, input().split()))
min_value = min(h)

while min_value <= l:
    h.sort()
    if l >= h[0]:
        l += 1
        del h[0]
    if len(h) >= 1:
        min_value = min(h)
    else:
        break

print(l)