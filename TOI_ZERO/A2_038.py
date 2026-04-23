import sys
input = sys.stdin.readline
n = int(input())
sumreal = 0
fwe = [0]*(3)
while n > 0:
    F1, W1, E1, F2, W2, E2 = map(int,input().split())
    sum1 = F1 + W1 + E1
    sum2 = F2 + W2 + E2
    r1 = [F1, W1, E1]
    r2 = [F2, W2, E2]
    
    if sum1 > sum2:
        sumreal += sum1
        for j in range(3):
            fwe[j] += r1[j]
    elif sum1 == sum2:
        w = 0
        for i in range(3):
            if r1[i] > r2[i]:
                w += 1
        
        if w == 2:
            sumreal += sum1
            for k in range(3):
                fwe[k] += r1[k]
        else:
            sumreal += sum2
            for w in range(3):
                fwe[w] += r2[w]
    else:
        sumreal += sum2
        for u in range(3):
            fwe[u] += r2[u]  
    n -= 1

print(sumreal)
for num in fwe:
    print(num,end=" ")
    
print()
if fwe[0] > fwe[1] + fwe[2]:
    print("YES")
else:
    print("NO")