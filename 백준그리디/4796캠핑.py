import sys
# l= 사용할수 있는 기간 p = 연속하는 날 v= 휴가기간

answer = 0


i = 1
while True:

    l, p, v = map(int, input().split())
    if l+p+v == 0:
        break
    answer = ((v // p) * l)
    answer += min((v%p), l)

    print('Case %d: %d' %(i, answer))

    i += 1
    # 문제 풀면서 어려웠던 점 1. 인풋의 횟수를 모를때 루프를 어떻게 돌려서 입력값을 받아야 하는가?
    # 2. 휴가기간중 연속하는날을 나누고 나머지 값을 그냥 더했었는데 그게 사용할수 있는 값과 비교해서 더 작은값을 더해야 했음
    # 여러 케이스를 더 다양하게 생각해보기
    


