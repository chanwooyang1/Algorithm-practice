
import sys
from collections import deque

input=sys.stdin.readline         # 반복문으로 여러줄 입력 받을때 사용하면 시간을 줄일 수 있다. / 입력받을때 str 형태로 개행문자(\n)이 포함해서 받아져서 처리할때 생각을 해야한다.

t=int(input())            # int로 형변환을 해주면 개행문자는 사라지고 정수형태로만 남게된다.

for _ in range(t):                       # for문을 돌때 따로 인덱스가 사용될 일이 없기 때문에 언더스코어로 표기하여 무시하는 값으로 사용 가능.
    n,m=map(int,input().split())               # 입력되는 두번째 줄의 값들을 동시에 받아 split()으로 나눈뒤 map으로 각자 int화 시켜준다 여기서 n의 값은 queue의 길이, m은 보고싶은 값의 번호다.
    lst=deque(map(int,input().split()))             #n개의 문서의 중요도가 순서대로 queue에 들어감 이것도 위와 마찬가지로 int화 시켜서 split해서 담아준다.
    q=deque(range(n))                        # n개의 항목을 가지고 있는 리스트 생성
    count=0
    while q:
        if lst[q[0]]==max(lst):              # lst의 첫번째 항목이 lst에서 가장 클때
            if q[0]==m:                     # 그 항목이 보고싶은 값이라면
                print(count+1)                  # 카운터를 1 올리고 break해서 종료
                break
            lst[q[0]]=0                     #첫번째 항목이 가장 크지만 m은 아닐때 인쇄되기 때문에 값을 0으로 변경하고
            q.popleft()                     #pop 해서 제거
            count+=1                        #한개가 인쇄 됐기 때문에 카운터 1추가
        else:
            q.append(q.popleft())           # 맨앞 항목이 젤 크지 않다면 왼쪽에서 빼서 오른쪽으로 다시 집어넣기
            #q.rotate(-1)                   # 내장함수로 로테이트 시켜서 왼쪽항목으로 오른쪽으로 보낼 수 있지만 시간이 조금 더 느렸음 양수를 집어 넣으면 오른쪽에서 왼쪽으로 들어감


