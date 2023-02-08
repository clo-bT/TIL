T = int(input()) #2
for tc in range(1,T+1):
    N = list(input())
    N.reverse()
    for i in range(len(N)):
        if N[i] == 'p':
            N[i] = 'q'
        elif N[i] == 'q':
            N[i] = 'p'
        elif N[i] == 'b':
            N[i] = 'd'
        elif N[i] == 'd':
            N[i] = 'b'
    print((f'#{tc}'),''.join(N))
