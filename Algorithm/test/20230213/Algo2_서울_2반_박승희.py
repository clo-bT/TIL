T = int(input()) #3
board = [[0]*10 for _ in range(10)]
di = []
dj = []
for tc in range(1,T+1):
    cnt = 0
    N = int(input()) #2
    r, c = map(int,input().split()) #망치의 시작위치 3 3
    for _ in range(N): #N줄에 걸쳐서 두더지 좌표 나와 1 2 2
        A,B,K = map(int,input().split())
        if abs(A-r) + abs(B-c) <= K: #갈 수 있는 크기면 점수획득
            cnt += 1
        else: # 다 못갈거야
            if abs(B-c)<K: #가로먼저
                c = B
            else: #가로가고 남은만큼

                if A<=r:#위로가야되면
                    r = r - (K-abs(B-c))
                else: #아래로가야되면
                    r = r + (K-abs(B-c))


