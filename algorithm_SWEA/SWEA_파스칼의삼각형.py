'''
민석님 코드
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
 
    for i in range(n):
        for j in range(i+1):
            if j == 0 or j == i:    # 배열의 첫번째와 마지막이라면
                arr[i][j] = 1       # 1로 고정
 
            else:                   # 배열의 중간자리들
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]     # 이전 배열의 합
 
    print(f'#{tc}')
    for li in arr:      # 리스트의 0을 제거하기위해
        ans = []
        for num in li:
            if num:     # 0이면 False 이므로
                ans.append(num)
        print(*ans)
    '''


T = int(input()) #1
for tc in range(1, T+1):
    N = int(input()) #4
    arr = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(i+1):
            if j == 0 or j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    print(f'#{tc}')
    for a in range(N):
        real_a = arr[a][:a+1]
        print(*real_a)