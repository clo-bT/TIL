def f(i, k, s):     # i물건공장결정, k물건개수, s i-1상품까지의 생산비용
    global minV
    global cnt
    cnt += 1
    if i == k:
        if minV > s:
            minV = s
    elif minV <= s:
        return
    else:
        for j in range(k):
            if u[j] == 0:
                u[j] = 1    #j공장 생산
                f(i+1, k, s+arr[i][j])
                u[j] = 0

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [list(map(int,input().split())) for _ in range(N)]
    #[[73, 21, 21], [11, 59, 40], [24, 31, 83]]
    p = [0] * N     #p[i] i상품을 생산하는 공장 인덱스
    u = [0] * N     #u[j] 공장을 이미 사용했으면 1
    minV = 1500
    cnt = 0
    f(0, N, 0)
    print(f'#{tc} {minV}')