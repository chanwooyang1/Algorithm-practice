h,w = map(int,input().split())
d=[]
n = int(input())

for i in range(h+1) :
  d.append([])
  for j in range(w+1) :
    d[i].append(0)




for i in range(n):
    l,b,x,y= input().split()
    l = int(l)
    b = int(b)
    x = int(x)
    y = int(y)
    for _ in range(l):
        d[x][y] = 1
        if b == 0:
            y += 1
        if b == 1:
            x += 1

for i in range(1, h + 1):
    for j in range(1, w + 1):
        print(d[i][j], end=' ')
    print()

