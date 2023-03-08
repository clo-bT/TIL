from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)       
  visited[v] = 1   
  
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, N + 1):
      if visited[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visited[i] = 1

def dfs(v):
  visited1[v] = 1    #방문    
  print(v, end = " ")
  for i in range(1, N + 1):
    if visited1[i] == 0 and graph[v][i] == 1:   #방문 안했고 이어져있으면
        dfs(i)

N, M, V = map(int,input().split()) #4 5 1
graph = [[0] * (N + 1) for _ in range(N + 1)] 
visited = [0] * (N + 1)
visited1 = [0] * (N + 1)

for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1
# print(graph) 
#[[0, 0, 0, 0, 0], 
# [0, 0, 1, 1, 1], 
# [0, 1, 0, 0, 1], 
# [0, 1, 0, 0, 1], 
# [0, 1, 1, 1, 0]]

dfs(V)
print()
bfs(V)

'''
1 2
1 3
1 4
2 4
3 4
'''
