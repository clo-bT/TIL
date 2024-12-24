T = int(input())
 
# 순서대로 우, 하, 좌, 상
pop_move = [(0,1), (1,0), (0,-1), (-1,0)]
 
for test in range(T):
    N, M = map(int, input().split())        # 기본 입력값
    arr_all = [list(map(int, input().split())) for _ in range(N)]
 
    count_max_flower = 0
    for i in range(N):                      # N줄만큼 반복
        for j in range(M):                  # M번 반복
            count_flower = arr_all[i][j]    # 기준점의 꽃잎
            for k in range(4):              # 상하좌우의 꽃잎 수를 더함
                if 0 <= i + pop_move[k][0] <= N-1 and 0 <= j + pop_move[k][-1] <= M-1:
                    count_flower += arr_all[i + pop_move[k][0]][j + pop_move[k][-1]]
                else:
                    pass
            if count_flower > count_max_flower:
                count_max_flower = count_flower
 
    print(f'#{test+1} {count_max_flower}')