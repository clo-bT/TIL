'''
T = int(input())  # 4
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # N명 M초 K개 #2 2 2
    P = sorted(list(map(int, input().split())))  # [3, 4]
    mx = max(P)
    bread = [0] * (mx + 1)
    for i in range(mx//M+1):
        bread[M * i] = K
    # for i in range(len(bread)):
    #     if bread[i] == 0:
    #         bread[i] = bread[i//M*M]
    cnt = 1
    for i in range(N):
        if (P[0]//M)*M <= P[i] < (P[0]//M)*M+1:
            bread[(P[0]//M)*M] -= 1
            cnt += 1
        if bread[(P[0]//M)*M] < 0:
            break

    if cnt != N:
        print(f'#{tc} Impossible')
    else:
        print(f'#{tc} Possible')
'''
## 민석님 코드
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    P = sorted(list(map(int, input().split())))
    

    ans = "Possible"

    for i in range(N):
        bread = (P[i] // M) * K - (i + 1)
        if bread < 0:
            ans = "Impossible"
            break

    print(f'#{tc} {ans}')