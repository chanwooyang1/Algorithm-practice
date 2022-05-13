
class Solution:                                               # i와 두개의 포인터 left right를 하나하나 이동시켜 모든 값들을 비교하고 답을 구하는 문제,
    def threeSum(self, nums=list):
        results = []                                              #결과값이 리스트로 나와야 하기에 빈 리스트를 먼저 선언해주고
        nums.sort()                                              #크기별로 정렬될 경우 시간이 줄기 때문에 미리 sort해놓기

        for i in range(len(nums) -2):                       #세팅이 끝났으면 i의 범위를 정해줘야 하는데 포인터 두개의 자리인 2를 전체 길이에서 뺀만큼 설정해준다
            if i > 0 and nums[i] == nums[i - 1]:                     #i의 값을 0으로 정해주고 이전 i의 값과 같으면 넘어가고 아니면 진행한다
                continue
            left, right = i + 1, len(nums) -1                         #  left랑 right 값 설정 right값은 전체 길이에서 1을 뺀 값 ( 시작이 0이기 때문에) = 마지막 자리
            while left < right:
                sum = nums[i] + nums[left] + nums[right]              #i 와 left right 값을 더해서 조건 판별
                if sum < 0:
                    left += 1                                                #원하는 조건이 없으니 left 한칸 이동
                elif sum > 0:
                    right -= 1                                                  #원하는 조건이 없으니 right 한칸 이동
                else:
                    results.append([nums[i], nums[left], nums[right]])          # 조건에 맞을때 리스트에 저장

                    while left < right and nums[left] == nums[left + 1]:      # left의 값이 다음과 같은지 비교해서 같으면 오른쪽으로 한칸 이동
                        left += 1
                    while left < right and nums[right] == nums[right -1 ]:   # right의 값이 이전과 같은지 비교해서 같으면 왼쪽으로 한칸 이동
                        right -= 1
                    left += 1                                                   #포인터들의 값이 전이나 후와 같지 않다면 한칸씩 움직이기
                    right -= 1
        return results

j = Solution()
print(j.threeSum([-1, 0, 1, 2, -1, -4]))







