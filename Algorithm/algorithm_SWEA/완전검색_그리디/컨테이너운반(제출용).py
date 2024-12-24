T = int(input()) #3
for tc in range(1, T+1):
    N, M = map(int,input().split()) #3 2 컨테이너 트럭
    weight = sorted(map(int,input().split())) #1 3 5 컨테이너
    truck = sorted(map(int, input().split())) #3 8 트럭
    ans = 0
    while weight and truck:
        w = weight.pop()
        t = truck.pop()
        if t >= w:
            ans += w
        else:
            truck.append(t)
    print(f'#{tc} {ans}')
    
    
'''
input
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13

output
#1 8
#2 45
#3 84
'''