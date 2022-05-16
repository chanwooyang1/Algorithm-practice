class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i, cur in enumerate(temperatures):
            while stack and cur >temperatures[stack[-1]]:
                last = stack.pop()
                answer[last]= i - last
            stack.append(i)
        return answer

# input [73,74,75,71,69,72,76,73]
# answer에 리스트안에 0이 temperature의 개수만큼 들어가는 리스트를 우선 생성
#스택들을 담을 리스트도 미리 선언

#i는 0 cur은  73, 처음엔 스택에 아무것도 없기 때문에 while 문을 돌지 않고 stack에 i가 들어간다
#이제 i는 1 cur은 74, 조건에 만족하기 때문에 last에는 스택에 들어있던 i값인 0이 pop된다
#answer[last]는 answer[0] 이므로 리스트 0번째항에 i-last 값 즉 1-0값인 1이 들어간다. (73의 하나 다음이 더 온도가 높으므로 1이 출력되어야 한다)
#이런식으루 계속 while문이 돌다 보면 조건에 만족하지 못해 3번 넘어가게 되고 스택에도 마찬가지로 2,3,4 총 3개의 항목이 쌓이게 된다
#다시 while문 조건에 맞을때 stack에 가장 위에 있던 4가 last로 pop되고  answer[last] 값인 answer[4]의 값은 현재 i의 값인 5- 4 이므로 1이된다
# 아직 계속 while 문의 조건을 만족하므로 i값은 증가하지 않고 while문을 돈다, 그 다음은 i의 값인 5에 stack의 최고값인 3이나오고 last[3]의 값에 5-3인 2가 들어가게 된다
#while 문 조건이 끝나서 for문으로 돌아가 i의 값이 증가하고 stack의 맨 윗부분인 2가 나오게 되며 answer[2]의 값에 6-2인 4를 넣게 된다


















# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         counter, stack = 0, []
#
#         for i in range(len(temperatures)):
#             if counter is None:
#                 stack.append(int(i))
#                 continue
#
#             while stack and i > stack[-1]:
#                 counter = counter + 1
#
#             stack.append(counter)
#             return stack
