import sys
input = sys.stdin.readline
T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y):
  stack = [[x, y]]
  while stack:
    a, b = stack.pop()
    for i in range(4):
      x = a + dx[i]
      y = b + dy[i]
      if 0 <= x < N and 0 <= y < M and arr[x][y]==1:
        arr[x][y] = 0
        stack.append([x, y])
for _ in range(T):
  ans = 0
  M, N, K = map(int, input().split()) # 10 8 17
  arr = [[0] * M for _ in range(N)]
  # graph 만들기
  for _ in range(K):
    x, y = map(int, input().split())
    arr[y][x] = 1
  # graph 읽기
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1:
        arr[i][j] = 0
        ans += 1
        dfs(i, j)
  print(ans)
    
    
''' 
# dfs 풀이 -> 런타임 에러
import sys
input = sys.stdin.readline
T = int(input())
def dfs(x, y):
  if x <= -1 or y <= -1 or x >= N or y >= M:
    return False
  if arr[x][y] == 1:
    arr[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  return False
for _ in range(T):
  ans = 0
  M, N, K = map(int, input().split()) # 10 8 17
  arr = [[0] * M for _ in range(N)]
  for _ in range(K):
    x, y = map(int, input().split())
    arr[y][x] = 1
  # print(arr)
  for i in range(N):
    for j in range(M):
      if dfs(i, j) == True:
        ans += 1
  print(ans)
'''
