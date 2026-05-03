import sys
input = sys.stdin.readline
n = int(input())
price = set()
store = []
for _,x in zip(range(n),map(int,input().split())):
    store.append(x)
    
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += store[j]
        price.add(sum)
        
print(len(price))