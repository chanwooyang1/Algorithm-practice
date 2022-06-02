n,m = map(int, input().split())
data = list(map(int,input().split()))
data.sort(reverse=True)
x = 0
y = 0
for _ in range(m):
    x = data.pop()
    y = data.pop()
    data.append(x+y)
    data.append(x+y)
    data.sort(reverse=True)
sum = 0
for i in data:
    sum += i
print(sum)
#합체놀이를 할때 최소의 값이 되려면 리스트에서 가장 작은 두 수를 꺼내서 더하고 다시 리스트에 집어넣고 리스트를 정렬시켜서 항상 작은 두 수를 꺼내도록 만들도록 하면 된다