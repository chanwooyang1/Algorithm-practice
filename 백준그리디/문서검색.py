counter = 0
d = input()
w = input()
length = len(w)
while True:
    if w in d:
       idx = d.find(w) + length - 1
       counter += 1
       d = d[idx +1:]

    else:
        break
print(counter)
# find 함수를 쓰면 찾는 문자열의 가장 첫번째 인덱스 위치를 알려줌 (이걸 잘 몰라서 문자열의[0]번째로 인덱스값을 고정시켰더니 공백을 인식을 못했음