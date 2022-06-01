n = int(input())
sum= 0
data = list(map(int, input().split()))
data.sort()
print(data[(n-1)//2])
# 처음엔 전체 값을 다 더해서 2로 나눈뒤 비교하려고 했으나 생각해보니 그냥 입력받은 값들중 중간에 위치하는 값이 무조건 최소값인걸 알게되었음