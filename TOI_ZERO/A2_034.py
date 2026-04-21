import sys
input = sys.stdin.readline
n = int(input())
arr = [True]*(32768+1)
arr[0] = arr[1] = False
m = int(n**0.5)
for i in range(2,m+1):
    if arr[i] == True:
        for j in range(i*i,n+1,i):
            arr[j] = False
            

if arr[n] == False:
    print("No")
else:
    print("Yes")
    for k in range(n+1):
        if arr[k] == True:
            print(k,end=" ")
            