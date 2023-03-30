def f(i, k, s):# i, k물건개수, s i-1상품까지의 생산비용
    global maxV

    if i == k:
        if maxV > s:
            maxV = s
    elif maxV >= s:
        return
    else:
        for j in range(k):
            if u[j] == 0:
                u[j] = 1    #j공장 생산
                if arr[i][j] != 0:
                    f(i+1, k, s+arr[i][j])
                    u[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #[[13, 0, 50], [12, 70, 90], [25, 60, 100]]
    p = [0] * N  # p[i] i상품을 생산하는 공장 인덱스
    u = [0] * N  # u[j] 공장을 이미 사용했으면 1
    maxV = 0
    cnt = 0
    f(0, N, 0)
    print(f'#{tc} {maxV}')
