# SWEA 10567. 구간합

T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #N=10, M=3
    arr = list(map(int,input().split()))
    
    maxV = 0
    minV = 1000000
    for i in range(N-M+1): # M개의 이웃한 원소에서 가장 왼쪽
        s = 0 # i에서 시작하는 구간합
        for j in range(i, i+M):
            s += arr[j]
        #for j in range(M):
            #s += arr[i+j]
            
        if maxV < s:
            maxV = s
        if minV > s:
            minV = s
    print(f'#{tc} {maxV-minV}')