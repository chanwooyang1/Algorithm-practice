n,l = map(int, input().split())
counter = 0
covered = [False] * 1001
x = list(map(int,(input().split())))
x.sort()
for i in range(n):

    cur = x[i]
    if covered[cur] == True and cur <= 1000:
        continue
    else:
        counter += 1
        for i in range(l):
            if cur + i <= 1000:
                covered[cur+i] = True
            else: break
print(counter)

# 처음 제출했을때 런타임 오류남. 생각해보니 위치가 1000일때 길이가 2이상인 테이프를 붙이면 오류가 날 수 있어서 길이가 1000일때 까지만 돌아가도록 변경함