import collections

#
# class Solution:                   # 문자열 배열을 받아 애너그램 단위로 그룹핑하라
#     def groupAnagrams(self, strs: [str]):                      #애너그램은 sorted 했을때 같은 값을 가지고 있음 그걸로 분리
#         anagram = collections.defaultdict(list)
#
#         for word in strs:
#             anagram[''.join(sorted(word))].append(word)
#         return anagram.values()





class Solution:
    def groupAnagrams(self, strs):
        anagram = collections.defaultdict(list)
        a = 'kimchi'
        for word in strs:

            anagram[''.join(sorted(word))].append(word)

        return anagram.values()



j = Solution()
print(j.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

    # word에 eat가 들어가면 sorted(word)를 통해 순서가 재배치되어 'aet' 가 되고 이건 key값으로 되면서 기존에 있던 word에 들어간 eat는 aet를 키값으로 가지는 딕셔너리 벨류로 들어감.
    # 이 단계를 반복하면서 같은 키값을 가진것 끼리 모이게 되면서 애너그램끼리 그룹화 하게 된다.

    # collection.defaultdict은  key값이 없는 경우도 null 로 출력이 가능 기본 dictionary 는 key 값이 없을 시 keyerror exception이 뜬다
    #defaultdict은 default_factory, key1 = value1 이런 식으루 인자를 받기때문에 default_factory에 인자를 넣어주지 않으면 오류가 뜬다
    #인자값을 예로 들면  list() 를 인자에 넣으면 'key' =[value], set()을 넣으면 'key' = {value}, int()를 넣으면 'key' = value 이런식이다.
    #sorted() 는 문자열을 정렬하여 리스트로 리턴 eat -> ['a','e','t']
    #'구분자'.join(리스트)   ''.join() -> aet
    # anagram['aet'].append(word) 이렇게 되면 aet는 키값으로 append.word된 값은 벨류값으로 들어가게 된다다


