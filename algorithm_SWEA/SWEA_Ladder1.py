'''
di = [0, 1, 0, -1] #우 하 좌 상
dj = [1, 0, -1, 0]
dir = 0 # 진행방향
    i = j = 0 # 숫자를 쓸 칸의 인덱스
    for k in range(1, N*N+1):
        arr[i][j] = k
        ni, nj = i + di[dir], j + dj[dir] # 다음 숫자를 쓸 좌표
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 : # 숫자를 쓸 수 있으면
            i, j = ni, nj
        else: # 배열을 벗어나거나 이미 숫자가 있으면
            dir = (dir+1) % 4 # 다음 방향으로 전환
            i, j = i+di[dir], j+dj[dir]
    print(f'#{tc}')
    for x in arr:
        print(*x)
'''
di = [-1,0,0] #상 좌 우
dj = [0,-1,1]
for tc in range(10):
    T = int(input()) # 그냥 번호 1-10
    a = [[0] + list(map(int,input().split())) +[0] for _ in range(100)] # 옆에 0짜리 만들기
    for i in range(101,0,-1):
        for j in range(101,0,-1):
            if a[99][j] == 2 :
                for
                si = i
                sj = j
                i = i-1
                if a[i][j-1] == 1:
                    j = j-1
                elif a[i][j+1] == 1:
                    j = j+1



                


