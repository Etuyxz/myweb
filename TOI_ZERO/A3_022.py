import sys
input = sys.stdin.readline
n = int(input())
light = []
while n > 0:
    a,b = map(int,input().split())
    if a > b:
        b += 360
    light.append((a,b))
    n -= 1
    
time = []
light.sort(key=lambda x:x[0])
sum = 0
check = []
for i in light:
    if len(check) == 0:
        check.append(i[0])
        check.append(i[1])
        sum = i[1] - i[0]
    else:
        if check[1] < i[0]:
            time.append(sum)
            sum = 0
            check[0] = i[0]
            check[1] = i[1]
            sum = check[1] - check[0]
        else:
            if check[1] < i[1]:
                sum += i[1] - check[1]
                check[1] = i[1]
            elif check[0] > i[0]:
                sum += check[0] - i[0]
                check[0] = i[0]

time.append(sum)         
if max(time) >= 360:
    print(360)
else:
    print(max(time))
