## 어디에 단어가 들어갈 수 있을까

T = int(input())

def count(arr):
    ans = 0 
    for lst in arr:
        cnt = 0
        for n in lst:
            if n == 1: # 단어를 넣을 수 있는 공백
                cnt += 1
            else: # 칸 없음
                if cnt == K:
                    ans += 1
                cnt = 0 # 다 끝나고 cnt 다시 초기화
    return ans

for tc in range(T, T+1):
    N, K =map(int,input().split())
    arr = [list(map(int, input().split())) [0] for _ in range(N)] + [[0]*(N+1)]

    #arr 와 arr_t로 각각 개수를 계산
    arr_t = list(map(list(zip(*arr))))
    # list(zip(*arr))는 현재 튜플. zip으로 받은 걸 list(map())으로 
    # 각각 리스트 적용
    ans = count(arr) + count(arr_t)
    print(f'#{tc} {ans}')



## 스도쿠 검증

def solve(arr):
    for lst in arr:             # 행을 체크
        if len(set(lst))!=9:    # 스도쿠 실패
            return 0
 
    arr_t = list(zip(*arr))
    for lst in arr_t:           # 열을 체크
        if len(set(lst))!=9:    # 스도쿠 실패
            return 0
 
    for i in (0,3,6):
        for j in (0,3,6):       # 3*3 격자
            lst = arr[i][j:j+3]+arr[i+1][j:j+3]+arr[i+2][j:j+3]
            if len(set(lst))!=9:
                return 0
    return 1
 
T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
 
    ans = solve(arr)
    print(f'#{test_case} {ans}')



## 숫자 배열 회전

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    arr_t = list(map(list,zip(*arr)))
    a1 = [[0]*N for _ in range(N)]  # 90도
    a2 = [[0]*N for _ in range(N)]
    a3 = [[0]*N for _ in range(N)]
 
    # [2] 전치배열과 읽는 방향에 따른 처리
    print(f'#{test_case}')
    for i in range(N):
        print(f'{"".join(arr_t[i][::-1])} {"".join(arr[N-1-i][::-1])} {"".join(arr_t[N-1-i])}')
 
 
    # [1] 회전각도에 따른 위치값을 저장
    for i in range(N):
        for j in range(N):
            a1[i][j] = arr[N-1-j][i]
            a2[i][j] = arr[N-1-i][N-1-j]
            a3[i][j] = arr[j][N-1-i]
    print(f'#{test_case}')
    for a,b,c in zip(a1,a2,a3):
        print(f'{"".join(a)} {"".join(b)} {"".join(c)}')




## Ladder2

T = 10
for test_case in range(1, T + 1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    mn = 100*100
    for sj in range(1, 101):
        # [1] 시작지점 찾기
        si = 0
        if arr[si][sj]!=1:
            continue
        cnt, dj = 0, 0
        ci, cj = si, sj
        while ci<99:
            cnt+=1
            if dj==0:
                if arr[ci][cj-1]==1:    #좌측
                    dj=-1
                    cj-=1
                elif arr[ci][cj+1]==1:  #우측
                    dj=1
                    cj+=1
                else:
                    ci+=1
            else:
                if arr[ci][cj+dj]==1:
                    cj+=dj
                else:   # 진행방향이 막힌경우 아래로
                    dj=0
                    ci+=1
        if mn>=cnt:
            mn, ans = cnt, sj-1
 
    print(f'#{test_case} {ans}')