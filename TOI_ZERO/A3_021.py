import sys
input = sys.stdin.readline
n,k = map(int,input().split())
n1 = n

x1 = []
while n > 0:
    x = int(input())
    x1.append(x)
    n -= 1
     
x1 = sorted(x1)
ans = 1
for i in range(1,n1):
    if (k-1)*x1[i] < k*x1[0]:
        ans += 1
    else:
        break

print(ans)