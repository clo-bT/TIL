T = int(input()) #3
for tc in range(1, T+1):
    N = int(input())#3
    hi = [list(map(int,input().split())) for _ in range(N)]
    ans = []
    for i in range(1,N-1):
        for j in range(1,N-1):
            cnt = 0                 # 높은 봉우리 개수 세기 위한 변수
            for di, dj in ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)):  # 8개 방향 탐색
                if 0<=i+di<N and 0<=j+dj<N and hi[i][j] > hi[i+di][j+dj]:   # 범위 벗어나지 않고, 비교해서 가운데가 높으면
                    cnt += 1                    # 개수 세고
            if cnt == 8:                        # 가운데가 주위 여덟개보다 높으면
                ans.append(hi[i][j])            # 가운데 봉우리를 답 리스트에 넣어놓고
    if len(ans) == 1 or len(ans) == 0:          # 한 개이거나 없으면 -1 출력
        print(f'#{tc}',-1)
    else:                                       # 여러개면 (가장 높은 봉우리) - (가장 낮은 봉우리)
        print(f'#{tc}', max(ans)-min(ans))