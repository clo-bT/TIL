T = int(input()) #1
for tc in range(1, T+1):
    N, Q = map(int,input().split()) # 5 2
    lrarr = [list(map(int,input().split())) for _ in range(Q)]
    box = [0] * N
    for i in range(Q):
        left = lrarr[i][0] - 1
        right = lrarr[i][1] - lrarr[i][0] + 1
        for j in range(left,left+right):
            box[j] = i+1
    print(f'#{tc}',*box)
