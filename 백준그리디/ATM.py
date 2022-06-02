n = int(input())
data = list(map(int, input().split()))
data.sort()
res = 0
t = 0
for i in data:
    res = res + i
    t += res
print(t)

# for문을 돌면서 각 사람마다 기다리는 시간이 나오고 그 각각의 값을 새로운 곳에 하나하나 저장하여 해결
