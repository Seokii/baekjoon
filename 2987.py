from shapely.geometry import Point, Polygon, LineString

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
n = int(input())
apple_tree = []
for _ in range(n):
    apple_tree.append(list(map(int, input().split())))

area = abs(a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1])) / 2
print(area)

cnt = 0
polygon = Polygon([(a[0], a[1]), (b[0], b[1]), (c[0], c[1])])
for i in range(len(apple_tree)):
    tmp = Point(apple_tree[i][0], apple_tree[i][1])
    if tmp.within(polygon) == True: cnt+= 1
    elif LineString([(a[0], a[1]), (b[0], b[1])]).contains(tmp): cnt+=1
    elif LineString([(a[0], a[1]), (c[0], c[1])]).contains(tmp): cnt+=1
    elif LineString([(b[0], b[1]), (c[0], c[1])]).contains(tmp): cnt+=1

print(cnt)

"""
def ccw(x1, y1, x2, y2, x3, y3):
    temp = x1*y2 + x2*y3 + x3*y1
    temp = temp - y1*x2 - y2*x3 - y3*x1
    if temp > 0: return 1
    elif temp < 0: return -1
    else: return 0
"""

