from collections import deque
import sys
input = sys.stdin.readline

def bfs(n,i):
    q = deque([n])
    while q:
        tmp = q.popleft()
        if tmp == i:
            return visited[tmp]
        for k in (tmp+1, tmp-1, 2*tmp):
            if 0 <= k < 100000 and visited[k] == 0:
                visited[k] = visited[tmp] + 1
                q.append(k)

N, K = map(int,input().split()) #5 17
visited = [0] * 100001
print(bfs(N,K))

'''
bfs는 visited 쓰는 게 훨씬 좋음
dfs는 재귀
깊이 구할 때 dfs를 비재귀로 풀 때 parent배열 son 탐색할 때 
par[son]=node 로 넣어놓고
par[node]+1 = par[son]으로 해놓으면 깊이를 알 수 있다?
'''