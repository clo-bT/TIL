T = int(input()) #3

for tc in range(1, T+1):
    N, M = map(int,input().split()) # 3 5
    arr = [list(map(int,input().split())) for _ in range(N)]
    #[[2, 3, 1, 8, 9], [7, 6, 2, 2, 6], [5, 7, 3, 8, 7]]
    ans = 0
    for i in range(N):
        for j in range(M):
            cnt = 0
            for di,dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):
                if 0<=i+di<N and 0<=j+dj<M and arr[i][j] > arr[i+di][j+dj]:
                    cnt += 1
                # else:
                #     break
            if cnt >= 4:
                ans += 1
    print(f'#{tc}',ans)



