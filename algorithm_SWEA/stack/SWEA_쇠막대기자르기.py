'''T = int(input())
for test_case in range(1, T + 1):
    st = input()
    ans = cnt = 0
    for i in range(len(st)):
        if st[i]=='(':      # 막대기 시작 또는 레이저표시
            cnt += 1
        else:               # ')'  바로 앞의 기호를 확인해야 함
            if st[i-1]=='(':# 레이저
                cnt -= 1
                ans += cnt
            else:           # 막대기의 끝
                cnt -= 1
                ans += 1
 
    print(f'#{test_case} {ans}')

'''




T = int(input()) #2
for tc in range(T):
    cnt = 0
    ans = 0
    a = input()
    for i in range(len(a)):
        if a[i:i+2] == '()':
            ans += cnt
        elif a[i] == '(':
            cnt += 1
        elif a[i] == ')':
            

