def f(i):
    global cnt
    if i:
        cnt += 1
        f(left[i])
        f(right[i])
    else:
        return

T = int(input()) #3
for tc in range(1,T+1):
    E, N = map(int,input().split()) #5 1
    V = E + 1   #정점
    cnt = 0
    arr = list(map(int,input().split())) #[2 1 2 5 1 6 5 3 6 4]
    left = [0] * (V+1)
    right = [0] * (V+1)
    for i in range(E):
        p, c = arr[i*2],arr[i*2+1] # 부모, 자식 읽어와서
        if left[p] == 0:           # c1이면 왼쪽에
            left[p] = c
        else:                      # c1에 이미 누가 있으면 오른쪽에
            right[p] = c
    f(N)
    print(f'#{tc}',cnt)