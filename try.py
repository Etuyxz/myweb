import sys
input = sys.stdin.readline
n = int(input())
block = []
for _,x in zip(range(n),map(int,input().split())):
    block.append(x)
       
maxblock = 0
sum = 0
for i in range(n):
    if maxblock > block[i]:
        sum += maxblock - block[i]
    else:
        maxblock = block[i]
  
maxleft = 0     
for i in range(n-1,-1,-1):
    if block[i] > maxleft:
        sum -= maxblock - block[i]
        maxleft = block[i]
    else:
        sum -= maxblock - maxleft
    
print(sum)