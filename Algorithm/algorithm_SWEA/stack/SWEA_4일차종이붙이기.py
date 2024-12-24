def f(n):
    if n == 0 or n == 1:
        return 1
    if  n == 2:
        return 3
    if n >= 3:
        return f(n-1) + 2*f(n-2)

def f2(n):
    arr = [0] * (n+1)
    arr[0] = 1
    arr[1] = 1
    for i in range(2, (N//10)+1):
        arr[i] = arr[i-1] + 2 * arr[i-2]
    return arr[n]


T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #30
    print(f'#{tc}',f2(N//10))


