class Solution:
    def arrayPairsum(self, nums):      # n개의 페어를 이용한 min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.
        sum = 0                       # sum 은 0으로 pair는 리스트 설정 num을 오름차순으로 설정
        pair = []
        nums.sort()

        for i in nums:                        # num을 for문 돌려서
            pair.append(i)                             #append로 리스트에 하나씩 넣기
            if len(pair) == 2:                                # 리스트의 길이가 2가 됐을때 sum에 넣고 pair 리셋
                sum += min(pair)
                pair = []
        return sum                                    #sum값 업데이트 하고 다시 포문 돌아가서 똑같이 돌린 뒤 sum 값 다 합치기

j = Solution()
print(j.arrayPairsum([1, 4, 3, 2]))