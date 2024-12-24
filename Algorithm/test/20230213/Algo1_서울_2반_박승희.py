T = int(input()) #3
for tc in range(1, T+1):
    N,M = map(int,input().split()) #N=도화지크기=5,M=도장찍은 횟수=1
    board = [[0]*N for _ in range(N)] #N*N 정사각형 배열
    for i in range(M): #M번 도장 찍을거야
        p,c,w,h = map(int,input().split()) # 1행,1열,3너비,2높이
        for j in range(w):
            for k in range(h):
                board[p+k][c+j] = 1 #1,1에서 너비, 높이 하나씩 늘려가며 좌표 찍기
        cnt = 0 # 몇개가 찍혀있는지 세기
        for j in range(N):
            for k in range(N):
                if board[j][k] == 1:
                    cnt += 1
    print(f'#{tc}',cnt)
