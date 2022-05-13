import collections


class Solution:
    def groupAnagrams(self, strs: [str]):
        anagram = collections.defaultdict(list)

        for word in strs:
            anagram[''.join(sorted(word))].append(word)
        return anagram.values()

j = Solution()
print(j.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    # word에 eat가 들어가면 sorted(word)를 통해 순서가 재배치되어 'aet' 가 되고 이건 key값으로 되면서 기존에 있던 word에 들어간 eat는 aet를 키값으로 가지는 딕셔너리 벨류로 들어감.
    # 이 단계를 반복하면서 같은 키값을 가진것 끼리 모이게 되면서 애너그램끼리 그룹화 하게 된다.