def bfs(s):
    # q, v 필요한 flag 생성
    q = []
    v = [0]*101
    ans = s
    # q에 초기데이터 삽입, v표시
    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)
        # q에서 한개 꺼냄 + 필요시 정답처리
        if v[ans]<v[c] or v[ans] == v[c] and ans<c:
            ans = c

        # 4/8 연결방향 등 반복처리
        for n in adj[c]:
            if v[n] == 0:
                q.append(n)
                v[n] = c[n] + 1
    return ans


T = 10
for tc in range(1, T+1):
    N, S = map(int,input().split())
    lst = list(map(int,input().split()))
    # 인접리스트에 연결 저장
    adj = [[] for _ in range(101)]
    for i in range(0, len(lst), 2):
        s, e = lst[i], lst[i+1]
        adj[s].append(e)
    ans = bfs(S)
    print(f'#{tc}', ans)