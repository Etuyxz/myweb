import sys
input = sys.stdin.readline
n = int(input())
sao = []
while n > 0:
    x = int(input())
    sao.append(x)
    n -= 1
    
sao = sorted(sao)
nsao = [0]*(len(sao)+1)
sum = 0
for i in range(len(sao)):
    if i == 0:
        nsao[i] = sao[0]
    else:
        nsao[i] = nsao[i-1] + sao[i]
        
    sum += nsao[i]
print(sum*2)