# 0이나 1일때만 더하고 나머지는 곱하면 될거같음 -> 기존에 있던 값이 0이나 1일때도 생각을 했어야 했음
data = input()
data = list(data)
for i in range(len(data)):
    data[i] = int(data[i])
mt = 0

for i in data:
    if i == 0 or i == 1 or mt == 0 or mt == 1:
        mt += i

    elif i != 1 and i != 0 and  mt != 0 or mt != 1:
        mt = mt*i

print(mt)
