import sys
input = sys.stdin.readline
n,l = map(int,input().split())
q = []
chair = []
for _,x in zip(range(n),map(int,input().split())):
    q.append(x)
    
for _,y in zip(range(l),map(int,input().split())):
    chair.append(y-1)
    
add = []
for i in chair:
    if i == 0:
        add.append(0)
    else:
        arr = max([q[j] for j in range(i)])
        if q[i] <= arr:
            add.append(arr+1-q[i])
        else:
            add.append(0)


for k in add:
    print(k)