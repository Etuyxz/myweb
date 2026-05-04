import sys
input = sys.stdin.readline
n,s = map(int,input().split())
n1 = n
tor = [0]
while n > 0:
    x = int(input())
    tor.append(x)
    n -= 1

visit = [False]*(n1+1)
sum = 1
while True:
    i = tor[s]
    if i == 0 or visit[i] == True:
        break

    visit[i] = True
    s = i
    sum += 1
        
print(sum)