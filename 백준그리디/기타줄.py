n,m = map(int, input().split())
s = 1001
p = 1001
for i in range(m):
    ns, np = map(int, input().split())
    s = min(ns, s)
    p = min(np ,p)
print(min((n//6)*s+(n%6)*p, ((n//6)+1)*s, n*p))
# 예외를 잘 따져봐야 하는 문제 가격에 따라 낱개로 전부를 사는게 싼 경우, 전부다 세트로 살때 싼 경우, 적절하게 세트와 낱개로 합쳐서 사야하는 경우를 따져야함