T = int(input()) #3
for tc in range(1, T+1):
    N = int(input()) #5
    C = list(map(int,input().split())) #[1,2,3,4,5]
    cnt = 1
    li = []
    for i in range(len(C)-1):
        if C[i+1] > C[i]:
            cnt += 1
        else:
            cnt = 1
        li.append(cnt)
    maxV = li[0]
    for i in range(len(li)):
        if maxV < li[i]:
            maxV = li[i]
    print(f'#{tc} {maxV}')

