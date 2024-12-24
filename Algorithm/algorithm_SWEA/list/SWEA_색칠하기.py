T = int(input()) #3
for tc in range(1, T+1):
    cnt = 0
    N = int(input()) #2
    emp = [[0] * 10 for i in range(10)]
    # 입력을 리스트로 받지 않고 하나의 값으로 받기
    for _ in range(N):
        r1, c1, r2, c2, color = map(int,input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                emp[i][j] += color
                if emp[i][j] == 3:
                    cnt += 1

    print(f'#{tc} {cnt}')