import sys
input = sys.stdin.readline

N = int(input())  # 7
road = [list(map(int, input().strip())) for _ in range(N)]

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
block = 0
block_count = []

def dfs(i, j):
    # (i, j) 위치에서 상하좌우로 dfs 탐색
    road[i][j] = 0  # 방문한 곳을 0으로 변경
    count = 1  # 현재 위치도 하나의 블록에 포함되므로 count 1로 시작
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < N and road[ni][nj] == 1:
            count += dfs(ni, nj)  # 연결된 블록에 대해 재귀적으로 count
    return count

for i in range(N):
    for j in range(N):
        if road[i][j] == 1:  # 장애물이 있고 아직 방문하지 않은 곳
            block += 1
            block_count.append(dfs(i, j))  # 새로운 블록을 찾고 dfs로 연결된 부분을 모두 방문 처리

print(block)  # 블록의 개수
for count in block_count:
    print(count)
