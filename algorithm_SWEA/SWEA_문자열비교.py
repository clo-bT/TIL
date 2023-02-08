T = int(input()) #3
for tc in range(1, T+1):
    str1 = input() #XYPV
    str2 = input() #EOGGXYPVSY
    if str1 in str2:
        print(f'#{tc}',1)
    else:
        print(f'#{tc}',0)