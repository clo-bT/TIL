def dfs(n, sm):
    global ans
    # [3] 가지치기 : 더이상 정답 갱신 가능성 없을 때
    # 가장 마지막에, 가장 위쪽에
    if K < sm:
        return

    if n == N:  # [1] 종료조건(n에 관련):반드시 정답처리는 이곳에서만!
        if sm == K:
            ans += 1
        return
    # [2] 하부호출
    dfs(n+1,sm+arr[n]) # 포함
    dfs(n+1,sm)     # 포함X

T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int,input().split()))

    ans = 0
    dfs(0,0)
    print(f'#{tc} {ans}')


'''
# 내가 푼 거
def dfs(n,summ):
    global ans
    if n == N:
        if summ == K:
            ans += 1
        return
    dfs(n+1,summ + A[n])
    dfs(n+1,summ)

T = int(input()) #1
for tc in range(1, T+1):
    N, K = map(int,input().split()) #4 3
    A = list(map(int,input().split())) #[1, 2, 1, 2]
    ans = 0
    dfs(0,0)
    print(f'#{tc} {ans}')

'''