N, K = map(int,input().split()) #4개, 7kg
arr = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]
for i in range(N):
    dp[1][arr[i][0]] = arr[i][1]
for i in range(N):
    for j in range(N):
        if arr[i][0]+arr[j][0]<=K:
            dp[2][arr[i][0]+arr[j][0]] = arr[i][1] + arr[j][1]

## 세번째줄부터 아예 일반화 고!
        
Wmax = 1
for line in dp: #dp 한줄
    for w in line:#W 하나
        if Wmax <= w:
            Wmax = w
print(Wmax)
