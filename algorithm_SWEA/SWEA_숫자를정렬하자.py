T = int(input()) #10
for tc in range(1, T+1):
    N = int(input()) #5
    a = list(map(int, input().split()))
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    print(f'#{tc}', *a)
