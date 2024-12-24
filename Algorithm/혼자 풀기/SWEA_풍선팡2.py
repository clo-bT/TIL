T = int(input()) #3
for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(M):
            summ = arr[i][j]
            for di,dj in [[-1,0],[1,0],[0,1],[0,-1]]:
                if 0<=i+di<N and 0<=j+dj<M:
                    summ += arr[i+di][j+dj]
            if mx < summ:
                mx = summ
    print(f'#{tc}',mx)
