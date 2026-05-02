import sys
input = sys.stdin.readline
n,l = map(int,input().split())
keep = []
road = []
sum = 1
while n > 0:
    s,t = map(int,input().split())
    keep.append((s,t))
    n -= 1

keep.sort(key=lambda x: x[0])
for i in keep:
    if len(road) == 0:
        road.append(i[0])
        road.append(i[1])
    else:
        if i[0] > road[0] and i[0] < road[1]:
            road[0] = i[0]
        if i[1] < road[1]:
            road[1] = i[1]
        elif road[1] < i[0]:
            sum += 1
            road[0] = i[0]
            road[1] = i[1]
            
print(sum)
