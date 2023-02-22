'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''

M, N = map(int,input())
arr = [[0,0]]+[list(map(int,input().split())) for _ in range(M)]
dp = [[0]*(N+1) for _ in range(M+1)]
for i in range(M):
    for j in range(N):
        for di, dj in [[1,0],[0,1],[0,-1]]:
            if 0<=i+di<M and 0<=j+dj<N:
                pass
