## 교수님 풀이
def f(i, k):
    global minV
    if i == k:
        s = 0
        for j in range(N):
            s += arr[j][p[j]] # j행에서 고른 열 p[j]
        if minV > s:
            minV = s
        return
    else:
        for j in range():               # p[i]의 숫자를 자신부터 오른쪽과 교환
            p[i], p[j] = p[j], p[i]
            f(i+1, k)                   # return하고
            p[i], p[j] = p[j], p[i]     # 원상복귀해줄래

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [list(map(int,input().split())) for _ in range(N)]

    p = [ i for i in range(N)] # p[i] i행에서 선택한 열
    minV = 100                 # 자연수
    f(0,N)                     # 0부터 시작해서 N개 행 고르면 돼
    print(f'{tc} {minV}')

'''
# 교수님 풀이2
# elif 로 조건들 쪼개주면 시간이 더 작게 걸림

def f(i, k, s):         # s 앞에서 선택한 원소의 합
    global minV
    global cnt
    cnt += 1
    if i==k:    # 순열 완성
        if minV > s:
            minV = s
        return
    elif s >= minV:
        return
    else:
        for j in range(i, N):   # p[i]의 숫자를 자신부터 오른쪽과 교환해봄
            p[i], p[j] = p[j], p[i]
            f(i+1, k, s+arr[i][p[i]])
            p[i], p[j] = p[j], p[i]
    return
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
 
    p = [ i for i in range(N)]  # p[i] i행에서 선택한 열
    minV = 100                    # 10이하 자연수 10개 이하
    cnt = 0
    f(0, N, 0)
    print(f'#{tc} {minV}')
'''