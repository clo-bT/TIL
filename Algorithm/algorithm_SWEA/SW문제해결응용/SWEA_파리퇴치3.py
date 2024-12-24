dplus=[[0,-1],[0,1],[-1,0],[1,0]]
dmult=[[-1,-1],[-1,1],[1,-1],[1,1]]
T = int(input()) #2
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    plus, mult = 0, 0
    for i in range(N):
        for j in range(N):
            splus = arr[i][j]
            smult = arr[i][j]
            for k in range(4):
                for r in range(1,M):
                    if 0<=i+dplus[k][0]*r<N and 0<=j+dplus[k][1]*r<N:
                        splus += arr[i+dplus[k][0]*r][j+dplus[k][1]*r]
                    
                    if 0<=i+dmult[k][0]*r<N and 0<=j+dmult[k][1]*r<N:
                        smult += arr[i+dmult[k][0]*r][j+dmult[k][1]*r]
            if plus<splus:
                plus = splus
            if mult<smult:
                mult = smult
    print(f'#{tc}',max(plus,mult))
                    
