import sys
input = sys.stdin.readline
n,l = map(int,input().split())
q = []
for _,x in zip(range(n),map(int,input().split())):
    q.append(x)
    
for _,y in zip(range(l),map(int,input().split())):
    ry = y-1
    if ry == 0:
        print(0)
    else:
        arr = max([q[j] for j in range(ry)])
        if q[ry] <= arr:
            print(arr+1-q[ry])
        else:
            print(0)
