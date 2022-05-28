n = int(input())
data = list(map(int,input().split()))
min = 0
data.sort()

# i 가 1일때
for i in range(1,len(n)):
    for j in data:
        if i == j:
            break
        while i >= j :


