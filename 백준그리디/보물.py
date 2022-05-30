n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
largest = 0
sum = 0
for i in range(n):
    largest = max(B)
    sum += A[i]*largest
    idx = B.index(largest)
    del B[idx]
print(sum)


# 처음에는 A배열 B배열 둘다 반대 방향으루 정렬시켜서 그냥 곱하려구 했으나 B배열은 순서를 바꿀수 없다고 해서 일단 A배열을 정렬 시키고 생각
#처음 생각처럼 그냥 A배열에 있는 젤 작은 수 와 B배열의 가장 큰 수를 곱하면 되겠다 생각함
#그래서 처음에 input 받은 n만큼 포문을 돌리면서 B배열의 최고값을 max함수로 찾아낸 뒤 index함수를 통해 그 값의 인덱스를 알아내서 del로 빼버림
# 그러면 최고값이 빠진 배열 B에서 그다음 최고값이 for문을 돌면서 하나씩 나오게 되기때문에 A배열 순서대로 곱해서 더하면 결과를 도출할 수 있음
# 여기서 한번 공부하게 된 함수 .index, del

