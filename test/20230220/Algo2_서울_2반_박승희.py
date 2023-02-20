T = int(input())#3
# d = [[0,1],[1,0],[0,-1],[-1,0]] #우 하 좌 상
di = [0,1,0,-1]
dj = [1,0,-1,0]
for tc in range(1,T+1):
    N = int(input()) #3
    dir = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]       # 방문한 곳은 다시 방문 안함
    ans = []
    i, j = 0, 0                               # 시작은 항상 0,0 지점
    while True:
        visited[0][0] = 1                     # 시작점 방문했다 찍어놓고
        if dir[i][j] == 0:                    # 방향이 0(우)이면
            visited[i][j] = 1                 # 방문했다 찍고
            i, j = i + di[0], j + dj[0]       # 우방향에 맞춰 이동
            if len(ans) == 0 or ans[-1] != 0: # ans가 비어있었거나 마지막이 자신이 아니면(중복방향없애기위해)
                ans.append(0)
        elif dir[i][j] == 1:                  # 모든 방향 탐색(하)
            visited[i][j] = 1
            i, j = i + di[1], j + dj[1]
            if len(ans) == 0 or ans[-1] != 1:
                ans.append(1)
        elif dir[i][j] == 2:                  # 모든 방향 탐색(좌)
            visited[i][j] = 1
            i, j = i + di[2], j + dj[2]
            if len(ans) == 0 or ans[-1] != 2:
                ans.append(2)
        elif dir[i][j] == 3:                  # 모든 방향 탐색(상)
            visited[i][j] = 1
            i, j = i + di[3], j + dj[3]
            if len(ans) == 0 or ans[-1] != 3:
                ans.append(3)
        if visited[i][j] == 1:                # 이동한 자리가 이미 방문했던 곳이면 break
            break
    print(f'#{tc}',*ans)



