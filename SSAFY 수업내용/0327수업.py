def perm(i, k):
    if i == k:
        print(*p)
    else:
        for j in range(k):      # 사용하지 않은 숫자를
            if used[j] == 0:    # used에서 순서대로 검색
                p[i] = A[j]     # 복사해놓고
                used[j] = 1     # 사용했다고 표시
                perm(i+1, k)
                used[j] = 0     # j번 자리 숫자를 다른 자리에서 쓸 수 있게

A = [1, 4, 5]
p = [0] * 3
used = [0] * 3
perm(0, 3)



def f(i, n, k):
    if i == k:
        print(*p)
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = A[j]
                f(i+1, n, k)
                used[j] = 0
A = [1, 2, 3, 4, 5]
N = 5
K = 3
