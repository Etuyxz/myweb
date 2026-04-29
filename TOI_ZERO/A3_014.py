import sys
input = sys.stdin.readline
n = int(input())
h1 = []
h2 = []
time = 0
while n > 0:
    x = int(input())
    if x > 18:
        h2.append(x)
    else:
        h1.append(x)
    n -= 1

if len(h1) >= len(h2):
    print(len(h1)+len(h2))
else:
    h = len(h2) - len(h1)
    print(2*len(h1)+(h+h-1))
    
        
    