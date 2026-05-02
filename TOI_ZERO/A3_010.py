import sys
input = sys.stdin.readline
n,k,t = map(int,input().split())
people = 1
gift = 1
while True:
    gift = (gift + k - 1) % n + 1
    
    if gift == 1:
        break
    
    people += 1
    
    if gift == t:
        break
    
print(people)