N, M = map(int,input().split()) #8 8 가로 세로
arr = [input().split() for _ in range(N)]
cnt = 0
for i in range(N):
    line = arr[i]
    for j in range(M):
        if 'BW' in line or 'WB' in line:
            cnt += 1



