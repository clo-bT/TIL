# DFS 이용한 교수님 코드

def dfs(i, j, N):
    stack = []              # 스택생성
    while True:
        if maze[i][j]==3:   # 방문한 칸이 목적지면
            return 1            # 성공
        maze[i][j] = 1      # 통로면, 다시 탐색할 일이 없으므로 벽으로 바꿈
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj] != 1: # '벽이 아니면'으로 검사해야함
                stack.append((i,j))         # 벽이 아니면
                i, j = ni, nj               # 이동
                break
        else:
            if stack:                       # 갈곳이 없고, 스택에 이전 칸이 있으면
                i, j = stack.pop()              # 이전 칸에서 다시 다른 방향 검색 시도
            else:                           # 출발점이면
                break                           # 검색 실패
    return 0                                # while을 빠져나오면 검색 실패
 
def dfs2(i, j, N):
    stack = [(i, j)]    # 이동할 칸 후보
    while stack:        # 출발까지 돌아오기 전이면
        i, j = stack.pop()  # 후보군 중 마지막 원소를 꺼내서 방문
        if maze[i][j] == 3:     # 출구
            return 1
        maze[i][j] = 1
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1:  # '벽이 아니면'으로 검사해야함
                stack.append((ni, nj))  # 탐색할 곳 추천. 벽이 아니면 모두 탐색할 칸 후보임
    return 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]   # 숫자로 저장
 
    # 출발 좌표 찾기
    si = sj = -1
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j
                break           # 그냥 계속 돌아도 됨...
        if si != -1:
            break
 
    #ans = dfs(si, sj, N)
    ans = dfs2(si, sj, N)
    print(f'#{tc} {ans}')
