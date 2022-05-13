class Solution:
    def longestPalindrome(self, s: str) -> int:
        def expand(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        if len(s) < 2 or s == s[::-1]:
            return len(s)
        result = ''
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
        return len(result)


j = Solution()

print(j.longestPalindrome('abccccdd'))

# 팰린드롬은 거꾸로 해도 똑같아야 하니까 우선조건 0번과 끝이 철자가 같아야 한다. 디버깅 해봐도 원리를 모르겠음 나중에 다시봐야겠음