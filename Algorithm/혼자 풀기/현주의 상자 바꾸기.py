'''
1
5 2
1 3
2 4
#1 1 2 2 2 0
'''

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    box = [0] * (N+1)
    for i in range(1, Q+1):
        Li, Ri = map(int, input().split())
        for j in range(Li, Ri+1):   # Li <= Ri 문제의 조건..
            box[j] = i
    print(f'#{tc}', *box[1:])