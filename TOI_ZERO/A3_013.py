import sys
input = sys.stdin.readline
n,s = map(int,input().split())
smin = 0
smax = 0
while n > 0:
    x = int(input())
    if x % 3 == 0 and x % 4 == 0:
        x1 = x // 3
        x2 = x // 4
        smin += 2*5*x1
        smax += 2*5*x2
    elif x % 4 == 0:
        x //= 4
        smin += 2*5*x
        smax += 2*5*x
    else:
        x //= 3
        smin += 2*5*x
        smax += 2*5*x
    n -= 1
    
print(s-smin,end=" ")
print(s-smax)