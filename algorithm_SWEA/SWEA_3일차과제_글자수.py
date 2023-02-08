T = int(input()) #3
for tc in range(1, T+1):
    str1 = list(input()) #XYPV
    str2 = list(input()) #EOGGXYPVSY
    di ={}
    for i in str1:
        di[i] = 0
        for j in str2:
            if i == j:
                di[i] += 1

    print(f'#{tc}',max(di.values()))



