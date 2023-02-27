T = int(input()) #4
for tc in range(1,T+1):
    a = input()
    b, ans = 0,0
    for i in range(len(a)):
        if a[i] != '0':
            b += int(a[i])
        else:
            if b < i+1:
                ans += i+1-b
                b += i+1-b
    print(f'#{tc}',ans)