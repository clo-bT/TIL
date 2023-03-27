def perm(i, k):
    global minV, ans
    if i == k:
        ans = 0
        for i in range(len(p) - 1):
            a = p[i] - 1
            b = p[i + 1] - 1
            ans += arr[a][b]
        if ans < minV:
            minV = ans
        return
    else:
        for j in range(k):      # 사용하지 않은 숫자를
            if used[j] == 0:    # used에서 순서대로 검색
                p[i+1] = A[j]     # 복사해놓고
                used[j] = 1     # 사용했다고 표시
                perm(i+1, k)
                used[j] = 0     # j번 자리 숫자를 다른 자리에서 쓸 수 있게

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [list(map(int, input().split())) for _ in range(N)]
    A = []
    for i in range(2, N+1):
        A.append(i) #[2, 3]
    used = [0] * (len(A))
    t = []
    p = [1] + [0]*len(A) + [1] #[1, 2, 3, 1]
    minV = 10000
    perm(0,len(A))
    print(f'#{tc} {minV}')



