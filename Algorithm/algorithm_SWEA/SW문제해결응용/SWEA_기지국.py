d = [[-1,0],[0,1],[0,-1],[1,0]]
T = int(input()) #2
for tc in range(1,T+1):
    N = int(input()) #9
    arr = [list(input()) for _ in range(N)]
    H = 0
    # visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                H += 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    di, dj = d[k][0], d[k][1]
                    if 0<=i+di<N and 0<=j+dj<N:
                        if arr[i+di][j+dj] == 'H':
                            arr[i+di][j+dj] = 'X'
                            H -= 1
            elif arr[i][j] == 'B':
                for k in range(4):
                    di, dj = d[k][0], d[k][1]
                    for r in range(1,3):
                        if 0<=i+di*r<N and 0<=j+dj*r<N:
                            if arr[i+di*r][j+dj*r] == 'H':
                                arr[i+di*r][j+dj*r] = 'X'
                                H -= 1
            elif arr[i][j] == 'C':
                for k in range(4):
                    di, dj = d[k][0], d[k][1]
                    for r in range(1,4):
                        if 0<=i+di*r<N and 0<=j+dj*r<N:
                            if arr[i+di*r][j+dj*r] == 'H':
                                arr[i+di*r][j+dj*r] = 'X'
                                H -= 1
    print(f'#{tc}', H)

