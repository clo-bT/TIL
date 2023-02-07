T = int(input()) #3
for tc in range(1, T+1):
    summ = 0
    N = int(input()) #5
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < N:
                    summ = summ + abs(arr[i][j] - arr[ni][nj])
   
    print(f'#{tc} {summ}')