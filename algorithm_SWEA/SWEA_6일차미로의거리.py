def bfs(i, j, N):
    queue = [(i, j)]                # 처음 좌표값 저장
    visited[i][j] = 1
    while queue:                    
        i, j = queue.pop(0)         # 제일 앞에꺼 빼

        if board[i][j] == 3:        # 3 만나면 경로 출력
            return visited[i][j] - 2    # 출발, 도착 제외
        
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and board[ni][nj] != 1 and visited[ni][nj] == 0:  
                queue.append((ni, nj))                              
                visited[ni][nj] = visited[i][j] + 1
    return 0

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #5
    board = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    # 출발 좌표
    si = sj = -1
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:        # 2 찾으면
                si, sj = i, j           # 그때의 좌표값 저장
                break           
        if si != -1:
            break
    ans = bfs(si, sj, N)
    print(f'#{tc} {ans}')
