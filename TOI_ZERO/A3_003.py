import sys
input = sys.stdin.readline
n = int(input())
s1 = [1]
s2 = [1]
for _,x in zip(range(n),map(int,input().split())):
    s1.append(x)
    
for _,y in zip(range(n),map(int,input().split())):
    s2.append(y)
 
sum = 0   
for i in range(1,n+1):
    sh =[s2[i],s2[i-1]]
    sh = sorted(sh)
    if s1[i] > sh[0] and s1[i] < sh[1]:
        if s1[i-1] < sh[0] or s1[i-1] > sh[1]:
            sum += 1
    elif s1[i] == sh[0] or s1[i] == sh[1]:
        if s1[i-1] == sh[0] or s1[i-1] == sh[1]:
            sum += 1
    elif s1[i] < sh[0] or s1[i] > sh[1]:
        if s1[i-1] > sh[0] and s1[i-1] < sh[1]:
            sum += 1     
print(sum)