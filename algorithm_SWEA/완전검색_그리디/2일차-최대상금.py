def f(arr, n):
    if n == 1:
        mx = max(arr)

T = int(input()) #3
for tc in range(1, T+1):
    a, n = input().split()
    arr = list(map(int,a))

