import collections

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                countinue

            while stack and char < stack[-1] and counter[stack[-1]] > 0:  # 만약 char가 스택에 이미 쌓여있는 문자이거나 뒤에 다시 붙일 문자가 남아있다면 (카운터가 0 이상이라면) 쌓아둔걸 없앤다.
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)


    # #seen 을 사용하지 않고
    #     # for char in s:
    #         counter[char] -= 1
    #         if char in stack:
    #             countinue
    #
    #         while stack and char < stack[-1] and counter[stack[-1]] > 0:
    #             stack.pop()
    #         stack.append(char)
    #         이런 식으로 in 을 이용한 검색연산도 가능하지만 스택에는 없는 것이기 때문에 스택으로만 만들자면 seen을 검색 기능으로 사용해서 풀이할 수 있다.