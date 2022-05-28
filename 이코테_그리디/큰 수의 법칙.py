a,b,c = map(int, input().split())
data = list(map(int,input().split()))
data.sort()
first = data[a-1]
second = data[a-2]
result = 0
while True:
    for i in range(c):
        if b == 0:
            break
        result += first
        b -= 1
    if b == 0:
        break
    result += second
    b -= 1
print(result)

# a 는 배열의 크기 b는 숫자가 더해지는 횟수 c는 연속으로 같은 값을 더할 수 있는 횟수
# while true 를 통해 무한 루프를 돌린 뒤 break로 조건이 맞으면 빠져 나옴
# 최고 값을 c번 더하고 2번째 값을 한번 더하고 다시 최고값으로 반복하면 되므로 sort를 통해 최고값과 두번째 값을 먼저 찾기
# c번 더하고 한번 더하는걸 하기 위해 c번 for문을 돌아서 더하고 빠져 나왔을때 second 한번 더하기 항상 b값이 0일때를 체크하고 무한루프 돌기