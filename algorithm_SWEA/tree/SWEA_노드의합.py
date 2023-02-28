'''
상미언니 코드
def postorder(i):             # 후위순회
    if i <= N:
        if tree[i] == 0:        # leaf가 아니면
            r1 = postorder(i*2, N)
            r2 = postorder(i*2 + 1, N)
            tree[i] = r1 + r2
        return tree[i]
    else:
        return 0
'''
def postorder(i):
    if tree[i] == 0:
        r1 = r2 = 0
        if i*2 <= N:
            r1 = postorder(i*2)
        if i*2+1 <= N:
            r2 = postorder(i*2+1)
        tree[i] = r1 + r2
    return tree[i]

T = int(input()) #3
for tc in range(1,T+1):
    N, M, L = map(int,input().split()) #5 3 2
    tree = [0] * (N+1)
    for _ in range(M):
        leaf, num = map(int,input().split())
        tree[leaf] = num
    if N % 2 == 0:
        tree.append(0)
    # print(tree) #[0, 0, 0, 3, 1, 2]
    postorder(1)
    print(f'#{tc}',tree[L])
