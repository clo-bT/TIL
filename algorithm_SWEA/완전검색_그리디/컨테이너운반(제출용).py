T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 2 컨테이너 트럭
    weight = sorted(map(int,input().split())) #1 5 3 컨테이너
    truck = sorted(map(int, input().split())) #8 3 트럭
    ans = 0
    while weight and truck:
        w = weight.pop()
        t = truck.pop()
        if t >= w:
            ans += w
        else:
            truck.append(t)
    print(f'#{tc} {ans}')