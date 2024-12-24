'''
def f(i, k):
    if i == k:
        return
    else:
        for j in range(k):
            if used[j] == 0:
                used[j] = 1
                p[i] = A[j]
                f(i+1,k)
                used[j] = 0
'''

T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #3
    arr = [list(map(int,input().split())) for _ in range(N)]
    a, b = map(int,input().split())
    li = [0, a, b, 0]
    if abs(a-b) == 1:
        ans = 0
        for i in range(len(li) - 1):
            ans += arr[li[i]][li[i + 1]]
    else:
        A = []
        if a < b:
            for i in range(a,b+1):
                A.append(i)
        else:
            for i in range(a,b-1,-1):
                A.append(i)
        # used = [0] * len(li)
        # p = [0] * N
        # f(0,N-1)
        A = [0] + A + [0]
        ans1, ans2 = 0,0
        for i in range(len(A)-1):
            ans1 += arr[A[i]][A[i+1]]
        for i in range(len(li) - 1):
            ans2 += arr[li[i]][li[i + 1]]
        ans = min(ans1, ans2)
    print(f'#{tc} {ans}')