def dfs(adjL,R):
    visited[R] = cnt
    






N, M, R = map(int,input().split()) #5 5 1
adjL = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for _ in range(M):
    u, v = map(int,input().split()) #1 4
    adjL[u].append(v)
    adjL[v].append(u)
