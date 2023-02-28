T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 5
    arr = [list(map(int,input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            mx = 0
            summ = arr[i][j]
            for _ in range(arr[i][j]):
                for di, dj in [[-1,0],[0,-1],[0,1],[1,0]]:
                    if 0<=i+di<N and 0<=j+dj<M:
                        summ += arr[i+di][j+dj]
            if summ >= mx:
                mx = summ
                
    print(f'#{tc}', mx)
                    