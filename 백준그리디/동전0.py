n, k = map(int, input().split())
m = []

counter = 0

for _ in range(n):
    m.append(int(input()))
m.sort(reverse=True)
for i in m:
        if k ==0:
            break
        counter += k//i
        k %= i
print(counter)


# m에 들은 값들을 큰거에서 작은거순서로 빼면 다시 뒤로 안돌아가도됨 처음엔 작은 값부터 꺼내서 비교하고 맞으면 다시 새로 시작했더니 시간초과가 나왔음
# %= 은 왼쪽 값에서 오른쪽 값을 나누고 나머지를 왼쪽에 저장
# if k > 0:
#     for i in range(len(m)):
#         if m[i] <= k:
#             continue
#         elif m[i] > k:
#             # if k>= m[i-1]:
#             sub = k//m[i-1]
#             k = k-(sub*m[i-1])
#             counter += sub
#             i = 0
#
#         # elif k == 0:
#         #     break
# print(counter)
#

