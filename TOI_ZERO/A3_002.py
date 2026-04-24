import sys
input = sys.stdin.readline
n = int(input())
sum = 0
index = 1
row = 1
while True:
    if n > row**2:
        row += 1
        index += 2
    else:
        break

start = row**2 - index + 1
rindex = 0
for i in range(index):
    if start != n:
        start += 1
        rindex += 1
  
while row > 1:
    if rindex % 2 == 0:
        sum += 1
        rindex += 1
    else:
        sum += 1
        row -= 1
        rindex -=1
        
print(sum)

