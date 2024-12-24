def f(i, k, p):
    global maxP

    if i == k:          # 모든 직원이 일을 맡으면
        if maxP < p:    
            maxP = p
        return
    elif maxP >= p:
        return
    for j in range(k):
        if u[j] == 0:   # j번 업무를 맡은 사람이 없으면
            u[j] = 1
            f(i+1, k, p*arr[i][j]/100)
            u[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    #[[13, 0, 50], [12, 70, 90], [25, 60, 100]]
    u = [0] * N  # u[j] 공장을 이미 사용했으면 1
    maxP = 0
    cnt = 0
    f(0, N, 1)
    print(f'#{tc} {maxP*100:.6f}')  # 소수점 아래 6자리까지
