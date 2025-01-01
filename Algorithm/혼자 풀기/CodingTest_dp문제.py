# 10 5
# 1 2
# 5 6
# 1 3
# 1 4
# 5 3

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [0] * (N+1)

for i in range(K):
  V, S = map(int, input().split())
  for j in range(N, 0, -1):
    if j - V >= 0:
      dp[j] = max(dp[j], dp[j-V] + S)
  print(dp[N])
  
''' 이차배열로 풀었을 경우
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (N + 1) for _ in range(K + 1)]

for i in range(1, K + 1):
    V, S = map(int, input().split())
    for j in range(N + 1):
        if j >= V:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - V] + S)
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[K][N])

'''