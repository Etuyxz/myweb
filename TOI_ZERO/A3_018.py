import sys
input = sys.stdin.readline
l,n = map(int,input().split())
som = [0]*(l)
row = 0
for i in range(1,l+1):
    som[i-1] = i**2
    if n > som[i-1]:
        n -= som[i-1]
        som[i-1] = 0
    else:
        som[i-1] -= n
    
    if som[i-1] > 0:
        row += 1
        
print(row)
