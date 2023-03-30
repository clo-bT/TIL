def promising(i, j):
    for di, dj in [[-1,-1],[-1,0],[-1,1]]:
        ni, nj = i + di, j + dj
        while 0<=ni<N and 0<=nj<N:
            if board[ni][nj]:   # 다른 퀸이 있으면
                return 0        # 실패
            ni, nj = ni+di, nj+dj
    return 1                    # i, j에 퀸을 놓을 수 있음


def f(i, N): #i번행이라고 놓고 N번행까지 가야돼
    global cnt
    if i == N: #N개의 퀸을 놓은 경우
        cnt += 1
    else:
        #첫번째꺼를 어디다 놓을 수 있을까
        for j in range(N):
            if promising(i, j):
                board[i][j] = 1
                f(i+1, N) #다음행에 놓기로 해
                # 갔다 오면
                board[i][j] = 0 #원래 다른 자리에 놓기로 하겠어


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [[0]*N for _ in range(N)]
    cnt = 0
    f(0, N)
    print(f'#{tc} {cnt}')