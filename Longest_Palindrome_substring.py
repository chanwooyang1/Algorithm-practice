def solution(s):

    def expand(left: int, right: int):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]

    if len(s) < 2 or s == s[::-1]:
        return len(s)
    result = ''
    for i in range(len(s) -1):
        result = max(result, expand(i , i+1), expand (i ,i +2), key=len)
    return len(result)

print(solution("adccccdd"))

#
# 함수에 s값이 들어감
# 내부함수는 일단 지나치고 if 조건 탐색해서 s의 길이가 2보다 작거나 거꾸로 배열이 같으면 리턴 (x)
# result에 공백칸 삽임
# i의 범위를 len(s)-1 로 잡은뒤 포문
# 일단 i에 0이 들어가고 익스펜드 함수 첫번째(짝수)실행 left 0 right 1
# 조건에 맞게 while문 left가 0 이상이고 right가 s의 길이보다 작고 s[0]과 s[1]이 같은 값을 가진다면 진행(x)
# 조건에 맞지 않아서 return s[0+1 : 1]
# 두번째 expand 함수 실행 left 0 right 2
# while 조건 안맞음으로 return s[0+1 : 2] -> max(expand(i, i+2)) = d = result
# 다시 for문 i+1 해서 돌기
# left 1 right 2 while 조건 안맞음 return s[2:2] -> 없음
# expand 두번째 함수 실행 조건에 안맞음 return s [2:3] 한칸이니까 이전 d 유지
# i + 1 해서 또 포문 돌기
# expand 첫번째 함수 실행조건에 맞아서 left -1 right +1 후 다시 while 조건 안맞아서 리턴 s[2:4]
# expand 두번째 함수 실행조건에 맞아서 left -1 right +1 후 다시 while 조건 안맞아서 리턴 s[2:5] result ccc
# i+1하고 또 포문
# expand첫번째 left 3 right 4 조건에 맞아서 2 5 또 조건에 맞아서 1 6 또 맞아서 0 7 조건 안맞아서 s[1:7]  = "dccccd"
# expand 두번째 left 3 right 5  조건 맞아서 2 6 안맞아서 s[3:6] = "ccc"
# result = "dccccd"
# i= 4 포문 돌리면
# expand 첫번째 left 4 right 5 조건 맞아서 3 6 조건 안맞아서 4 6
# expand  두번째 left 4 right 6 안맞아서 5 6
# i= 5 포문 돌리지만 의미없음
# i = 6 돌리지만 의미없음 결과는 6














