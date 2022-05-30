# 5--2--4--1
#   2  3  1
n = int(input())
d = list(map(int,input().split()))
p = list(map(int,input().split()))
answer = 0
price = 0
for i in d:
    for j in p:
        if price == 0:
            price = int(j)
            answer = int(i)*int(j)
            del p[0]
            break
        elif j >= price:
            answer += price * int(i)
            del p[0]
            break
        elif j < price:
            price = int(j)
            answer += int(i) * int(j)
            del p[0]
            break
print(answer)

#포문 두개를 돌려서 풀었지만 더 빠른 수가 있을거 같아서 더 생각해봐야 할 문제 price에 기름값을 넣어 새로운 기름값과 크기를 비교해서 작은값을 price에 넣고 반복하는 방법