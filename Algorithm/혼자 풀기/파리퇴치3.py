'''
2
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3
6 3
29 21 26 9 5 8
21 19 8 0 21 19
9 24 2 11 4 24
19 29 1 0 21 19
10 29 6 18 4 3
29 11 15 3 3 29

#1 64
#2 157
'''


di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, -1, 1]

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0  # 모든 중심에 대한 고려가 끝났을때의 최대 파리 퇴치
    for i in range(N):
        for j in range(N):
            s = arr[i][j]  # i, j를 중심으로 퇴치되는 파리수
            for k in range(4):  # k 방향으로 +
                for p in range(1, M):  # p칸 옆에
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]  # 퇴치되는 파리수 누적
            if maxV < s:  # 이전의 촤대 퇴치수보다 더 많으면
                maxV = s
            s = arr[i][j]  # i, j를 중심으로 퇴치되는 파리수
            for k in range(4, 8):  # k 방향으로 X
                for p in range(1, M):  # p칸 옆에
                    ni = i + di[k] * p
                    nj = j + dj[k] * p
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]  # 퇴치되는 파리수 누적
            if maxV < s:  # 이전의 촤대 퇴치수보다 더 많으면
                maxV = s
    print(f'#{tc} {maxV}')


'''
di = [0, 1, 0, -1, 1, 1, -1, -1]
dj = [1, 0, -1, 0, 1, -1, -1, 1]
 
def f(i, j, N, M, k):
    s = arr[i][j]               # 중심에서 퇴치되는 파리 수
    for dir in range(k, k+4):
        for p in range(1, M):
            ni = i+di[dir]*p
            nj = j+dj[dir]*p
            if 0<=ni<N and 0<=nj<N:
                s += arr[ni][nj]
            # else:           # 영역을 벗어나는 경우뿌릴 수 없는 경우
            #     return 0
    return s
 
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxV = 0  # 모든 중심에 대한 고려가 끝났을때의 최대 파리 퇴치
    for i in range(N):
        for j in range(N):
            result = f(i, j, N, M, 0) # +
            if maxV < result:  # 이전의 촤대 퇴치수보다 더 많으면
                maxV = result
            result = f(i, j, N, M, 4)   # X
            if maxV < result:
                maxV = result
    print(f'#{tc} {maxV}')
'''