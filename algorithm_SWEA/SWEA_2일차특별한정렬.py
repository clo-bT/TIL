'''
T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #10
    a = list(map(int, input().split()))
    for i in range(N-1):
        minIdx = i
        for j in range(i+1, N):
            if a[minIdx] > a[j]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    # ----리스트 오름차순으로 된 상태-----
    print(f'#{tc}',a[N-1], a[0],a[N-2], a[1],a[N-3], a[2],a[N-4], a[3],a[N-5], a[4])
'''

## 민석님 코드
T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #10
    a = list(map(int, input().split()))
    for i in range(N-1):
        mIdx = i
        if i % 2 == 0:
            for j in range(i+1, N):
                if a[mIdx] < a[j]:
                    mIdx = j
            a[i], a[mIdx] = a[mIdx], a[i]
        else:
            for j in range(i+1, N):
                if a[mIdx] > a[j]:
                    mIdx = j
            a[i], a[mIdx] = a[mIdx], a[i]
    print(f'#{tc}',*a[:10])