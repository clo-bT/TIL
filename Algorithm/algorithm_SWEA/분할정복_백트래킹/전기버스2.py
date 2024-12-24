def f(i, k, e, c):
    global minC
    if c >= minC:
        return
    if i == k:
        if minC > c:
            minC = c
    else:
        f(i+1, k, arr[i]-1, c+1)
        if e>0:
            f(i+1, k, e-1, c)

T = int(input()) #3
for tc in range(1, T+1):
    arr = list(map(int,input().split())) #5 2 3 1 1
    N = arr.pop(0)
    minC = N
    f(0,N-1,arr[0],0)
    print(f'#{tc} {minC}')