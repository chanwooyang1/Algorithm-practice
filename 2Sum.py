target = 9
class Solution:

    def threeSum( self, nums:[int]):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
j = Solution()
print(j.threeSum([2, 7, 11, 15]))