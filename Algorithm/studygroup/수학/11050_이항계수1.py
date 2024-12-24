import sys
input = sys.stdin.readline
N, K = map(int,input().split())
R = N-K
ans = 1
for i in range(1,N+1):
    ans *= i
for i in range(1,K+1):
    ans //= i
for i in range(1,R+1):
    ans //= i
print(ans)