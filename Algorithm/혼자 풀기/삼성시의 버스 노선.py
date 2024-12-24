'''
1
2
1 3
2 5
5
1
2
3
4
5

#1 1 2 2 1 1
'''

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선수
    cnt = [0] * 5001    # cnt[i] i번 정류장에 서는 버스 노선 수
    for _ in range(N):  # N개의 노선에 대해
        A, B = map(int, input().split())    # 출발 도착, A<=B 조건
        for i in range(A, B+1):
            cnt[i] += 1 # i정류장에 멈추는 버스
    P = int(input())    # 노선수를 출력할 정류장 개수
    busstop = []
    for _ in range(P):
        number = int(input())
        busstop.append(number)
    print(f'#{tc}', end = ' ')
    for x in busstop:
        print(cnt[x], end = ' ')
    print()

'''
T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 노선수
    cnt = [0] * 5001    # cnt[i] i번 정류장에 서는 버스 노선 수
    for _ in range(N):  # N개의 노선에 대해
        A, B = map(int, input().split())    # 출발 도착, A<=B 조건
        for i in range(A, B+1):
            cnt[i] += 1 # i정류장에 멈추는 버스
    P = int(input())    # 노선수를 출력할 정류장 개수
    busstop = []
    for _ in range(P):
        number = int(input())
        busstop.append(cnt[number])
    print(f'#{tc}', *busstop)
'''