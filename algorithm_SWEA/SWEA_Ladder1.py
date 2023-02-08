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
                pass
                si = i
                sj = j
                i = i-1
                if a[i][j-1] == 1:
                    j = j-1
                elif a[i][j+1] == 1:
                    j = j+1

'''
연주님 코드
for tc in range(1, 11):
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(100)]
 
    di = 99  # 도착점
    dj = li[99].index(2)
 
    while di >= 0: # 0행에 도달할때까지
        if di == 0:
            break
        if dj >=1 and li[di][dj - 1]: # 왼쪽에 사다리 있으면
            while dj > 0:
                if li[di-1][dj-1]:
                    di -= 1
                    dj -= 1
                    break
                else:
                    dj -= 1
        elif dj <=98 and li[di][dj + 1]: # 오른쪽에 사다리 있으면
            while dj < 99:
                if li[di-1][dj+1]:
                    di -= 1
                    dj += 1
                    break
                else:
                    dj += 1
        else:
            li[di][dj] = 0
            di -= 1 # 좌우에 사다리 없으면(혹은 양쪽 끝이면) 올라가
    print(f'#{tc}', dj)

'''
'''
치훈님 코드
di = [0, -1, 0]
dj = [-1, 0, 1]
 
for _ in range(1, 11):
    tc = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    i = 99
    j = board[99].index(2) # 현재 위치 i,j
    dir = 1
    while i > 0:
        if dir == 1:
            i, j = i + di[dir], j + dj[dir]
            if j != 0 and board[i][j-1] == 1:
                dir = 0
            elif j != 99 and board[i][j+1] == 1:
                dir = 2
        else:
            i, j = i + di[dir], j + dj[dir]
            if board[i-1][j] == 1:
                dir = 1
    print(f'#{tc} {j}')
'''

                


