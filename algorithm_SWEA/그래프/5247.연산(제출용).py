'''
## 민석님 코드
def bfs():
    visited = [0 for _ in range(1000001)]
    que = []
    que.append(N)
    cnt = 0  # 연산 횟수
    while que:
        for i in range(len(que)):
            v = que.pop(0)
            if v == M:
                return cnt

            for j in range(len(cal)):
                if not (0 < v + cal[j] <= 1000000) or visited[v + cal[j]]:
                    continue
                visited[v + cal[j]] = 1
                que.append(v + cal[j])

            if not (0 < v * 2 <= 1000000) or visited[v * 2]:  # 곱하기는 따로 작성.
                continue
            else:
                visited[v * 2] = 1
                que.append(v * 2)
        cnt += 1

T = int(input())
cal = [1, -1, -10]
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f'#{tc} {bfs()}')
'''


## 치훈님 코드 참고
from collections import deque

def bfs():
    q = deque([N])
    visited = [0] * 1000001
    visited[N] = 1
    while q:
        v = q.popleft()
        if v == M:
            return visited[v] - 1

        for i in [-1, +1, -10, v]:
            w = v + i
            if 0 < w <= 1000000 and visited[w] == 0:
                visited[w] = visited[v] + 1
                q.append(w)

T = int(input()) #3
for tc in range(1, T + 1):
    N, M = map(int, input().split()) #2 7 3 15
    ans = bfs()
    print(f'#{tc} {ans}')