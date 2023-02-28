def postorder(i):
    if tree[i] in ['+','-','*','/']:
        r1 = postorder(i*2)
        r2 = postorder(i*2+1)
        if tree[i] == '-':
            tree[i] = r1-r2
            return tree[i]
        elif tree[i] == '+':
            tree[i] = r1+r2
            return tree[i]
        elif tree[i] == '*':
            tree[i] = r1*r2
            return tree[i]
        elif tree[i] == '/':
            tree[i] = r1/r2
            return tree[i]
    else:
        return tree[i]


for tc in range(1,11):
    N = int(input()) #5 정점
    arr = [list(input().split()) for _ in range(N)]
    tree = [0] * (N+1)
    
    for i in arr:
        if len(i) == 2: # 피연산자
            tree[int(i[0])] = int(i[1])
        else:   # 연산자
            tree[int(i[0])] = i[1]
    # tree = [0, '-', '-', 10, 88, 65]
    postorder(1)
    print(f'#{tc}',int(tree[1]))


