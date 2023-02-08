T = int(input()) #3
for tc in range(1,T+1):
    w = list(input())
    copyw = w[:]
    w.reverse()
    if copyw == w:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)