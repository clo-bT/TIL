T = int(input()) #1
for tc in range(1,T+1):
    D, A, B, F = map(int,input().split())
    t = D/(A+B)
    print(f'#{tc}',F*t)