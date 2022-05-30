n = int(input())

lope = []
for i in range(n):
    w = int(input())
    lope.append(w)
lope.sort(reverse=True)
for i in range(n):
    lope[i] = lope[i]*(i+1)


print(max(lope))

#처음에는 모든 로프를 사용해야 하는지 알고 그냥 로프가 버틸수 있는 무게를 리스트에 하나하나 넣고 그중 미니멈을 찾아서 n을 곱해서 나오는 무게가 버틸 수 있는 최고 무게라고 생각했다
#하지만 꼭 모든 로프를 사용하지 않아도 되기 때문에 버틸수 있는 무게가 젤 큰 로프 x 1 그 다음 높은 로프 x 2 이런식으로 젤 약한 로프 x n 해서 각 케이스별로 무게를 구한 뒤
# max 함수를 이용해서 그 중 가장 큰 케이스의 무게를 출력한다