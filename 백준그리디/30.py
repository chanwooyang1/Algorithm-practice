n = list(map(str,(input())))
n.sort(reverse=True)
sum = 0
if '0' not in n:
    print(-1)
else:

    for i in n:
        sum += int(i)
    if sum % 3 !=0:
        print(-1)
    else:
        print(''.join(n))

        # 30의 배수 조건을 따져봐야 했던 문제, 다행히도 30의 배수 조건이 리버스정렬을 하면 충분히 구할수 있도록 만들어져서 조건만 따지면 알 수 있었다