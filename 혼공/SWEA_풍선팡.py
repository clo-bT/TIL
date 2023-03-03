T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 5
    arr = [list(map(int,input().split())) for _ in range(N)]
    mx = 0
    for i in range(N):
        for j in range(M):
            summ = arr[i][j]
            for k in range(1,arr[i][j]+1):
                for di, dj in [[-1,0],[0,-1],[0,1],[1,0]]:
                    if 0<=i+di*k<N and 0<=j+dj*k<M:
                        summ += arr[i+di*k][j+dj*k]
            if summ >= mx:
                mx = summ
                
    print(f'#{tc}', mx)