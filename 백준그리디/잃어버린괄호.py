arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    if arr[0] == '':
        break
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
#-와 - 사이를 괄호로 묵으면 최소의 값이 나온다 식 처음에 -가 나올걸 대비해 break를 했다