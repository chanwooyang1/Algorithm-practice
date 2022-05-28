n,m = map(int,input().split())
d = list(map(int, input().split()))
p1= 0
p2 = 1
count = 0

while True:
    if d[p1] != d[p2] and p2 != n:
        count += 1
        p2 += 1

    elif d[p1] == d[p2] and p2 != n:
        p2 += 1
    if p2 == n and p1 != n:
        p1 += 1
        p2 = p1 + 1
    if p1 == n-1:
        break
print(count)