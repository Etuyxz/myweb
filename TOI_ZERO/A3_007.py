import sys
input = sys.stdin.readline
l,n = map(int,input().split())
row = 1
n -= 1
while True:
    if n > 0:
        row += 1
        n -= row
    else:
        break

num = 0
ans = 1
while True:
    if num < row :
        num = ans*l
        ans += 1
    else:
        ans -= 1
        break
    
print(ans)