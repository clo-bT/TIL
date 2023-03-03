
T = int(input()) #4
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)] #['....o', '...o.', '..o..', '.o...', 'o....']
    ans = ''
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                
                for di, dj in [[1,-1],[1,0],[0,1],[1,1]]:
                    ni, nj = i+di, j+dj
                    cnt = 1
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj] == 'o':
                        cnt += 1
                        ni,nj = ni+di, nj+dj
                        if cnt == 5:
                            ans = 'YES'
                            break   # while문 나감
    if ans == 'YES':
        print(f'#{tc}', ans)
    else:
        print(f'#{tc} NO')









'''

## 박영준 교수님 코드
def solve(N):
    # 시작 돌 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    # 돌을 만나면
                for di, dj in [[0,1],[1,1],[1,0],[1,-1]]:
                    cnt = 1  # 돌의 개수
                    ni, nj = i+di, j+dj
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                        cnt += 1
                        ni, nj = ni+di, nj+dj
                        if cnt == 5:
                            return 'YES'
    return 'NO'
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
 
    ans = solve(N)
    print(f'#{tc} {ans}')




## 박영준 교수님 코드 2
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
 
    # 시작 돌 찾기
    ans = 'NO'
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':    # 돌을 만나면
                for di, dj in [[0,1],[1,1],[1,0],[1,-1]]:
                    cnt = 1  # 돌의 개수
                    ni, nj = i+di, j+dj
                    while 0<=ni<N and 0<=nj<N and arr[ni][nj]=='o':
                        cnt += 1
                        ni, nj = ni+di, nj+dj
                        if cnt == 5:
                            ans = 'YES'
                            break   # while 0<=ni<N...
                    if ans == 'YES':
                        break    # for di, dj ...
            if ans == 'YES':
                break  # for j
        if ans == 'YES':
            break  # for i
    print(f'#{tc} {ans}')
'''