def bfs(i,j):
    queue = [(i,j)]
    while queue:
        i,j = queue.pop(0)
        if arr[i][j] == 3:
                return 1
        for di, dj in [[0,-1],[0,1],[-1,0],[1,0]]:
            if 0<=i+di<16 and 0<=j+dj<16 and visited[i+di][j+dj] == 0 and arr[i+di][j+dj] != 1:
                queue.append((i+di,j+dj))
                visited[i+di][j+dj] = visited[i][j] + 1
            
    return 0


for _ in range(10):
    T = int(input()) #testcase
    arr = [list(map(int,input())) for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]
    print(f'#{T}',bfs(1,1))