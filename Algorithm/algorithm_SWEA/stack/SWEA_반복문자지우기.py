'''
혜진쓰 코드
T = int(input())
for test_case in range(1, T+1):
    arr = input()
    stack = [0] * len(arr)          # arr 크기 만큼의 저장소
    top = -1
    for x in arr:
        top += 1
        stack[top] = x              # 문자 하나씩 넣어줌
        if top > -1:                
            if x == stack[top-1]:   # 그 전에 넣은 문자와 같다면 두 칸 아래로
                top -= 2
    print(f'#{test_case}', top+1)
'''

T = int(input()) #3
for tc in range(1, T+1):
    word = input()
    stack = [0] * len(word)
    top = 0
    for i in word:
        stack[top] = i
        if top > -1:
            if i == stack[top-1]: # 이해 하다 말았음
                top -= 2
        top += 1
    print(f'#{tc}',top)
