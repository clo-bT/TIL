from sys import stdin
# input 자리에다가 stdin.readline() 쓰면 시간 줄어듦

queue = []
T = int(stdin.readline())

for i in range(T):
    X = stdin.readline().split() # 이렇게만 써도 push 1이 자동으로 리스트로 저장
    if X[0] == 'push':
        queue.append(X[1])

    if X[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else: 
            po = queue.pop(0)
            print(po)

    if X[0] == 'size':
        print(len(queue))

    if X[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if X[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if X[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
