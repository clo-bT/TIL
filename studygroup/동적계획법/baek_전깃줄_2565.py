

# 풀이 2
# A전봇대 기준으로 정렬하고, B전봇대에서 가장 긴 증가하는 부분 수열을 구해서 빼주면 된다.
n = int(input())
a = sorted([list(map(int, input().split())) for _ in range(n)])

dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[i][1] > a[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

