T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #10
    C = input() #[0011001110]
    cnt = 0
    li = []
    for i in range(N-1):
        if (int(C[i]) + int(C[i+1])) > 1:
            cnt += 1
        else:
            cnt = 0
        li.append(cnt)
    maxV = li[0]
    for i in range(len(li)):
        if maxV < li[i]:
            maxV = li[i]
    print(f'#{tc} {maxV+1}')
