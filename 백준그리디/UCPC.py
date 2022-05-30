
s = input()
ucpc = ['U', 'C', 'P', 'C']
check = True
for i in range(len(ucpc)):
    if ucpc[i] in s:
        idx = s.find(ucpc[i])
        check = True
        s = s[idx+1:]
    else:
        check = False
        break
if check == True:
    print("I love UCPC")
else:
    print("I hate UCPC")


#  UCPC 가 들어있는 배열을 만든뒤 그 순서대로 하나씩 꺼내서 인풋 받은 문장에 있나 없나 검사후, 만약 있다면 그 철자가 있는 위치의 인덱스 값을 구해서
    #포문을 다시 돌때 새로 시작을 인덱스 값+1을 해서 찾은 글자 뒤부터 다시 돌기, 만약 없다면 False 만들고 for문 끝내기