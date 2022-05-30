# 1 3 6 10 15 21 28 36 45 55 66 78 91 105 120 136 153 171 190 210

# n = int(input())
# i = 0
# answer = 0
# while True:
#     if n ==0:
#         break
#     if i == n:
#         answer = i
#         print(answer)
#         break
#     elif i > n:
#         answer = i-1
#         print(answer)
#         break
#     n -= i
#     i += 1

    #다른 사람 풀이를 보니 무한루프로 i를 계속 더하면서 n과 크기비교, 더한값이 n이랑 같아질떄까지 포문을 돌고 , 더한값이 더 커졌을때만 i-1을 출력
    # 답은 풀었지만 메모리나 시간이 너무 소모됨 하지만 다른 사람 풀이를 넣어보니 나랑 똑같이 메모리나 시간소모가 나옴.. 알고보니 저 사람은 python 3 으로 제출함

S = int(input())

Sum = 0
i = 0
while Sum <= S:
    i += 1
    Sum += i
print(i-1)