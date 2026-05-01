import sys
input = sys.stdin.readline
n,k = map(int,input().split())
pasg = [0]*(k+1)
sum = 0
while n > 0:
    x = int(input())
    sum += 1
    pasg[x] += 1
    n -= 1
    
pasg.pop(0)
print(sum - k*min(pasg))

