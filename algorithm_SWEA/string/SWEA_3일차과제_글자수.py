T = int(input()) #3
for tc in range(1, T+1):
    str1 = input() #XYPV
    str2 = input() #EOGGXYPVSY
    di = {}
    for i in str1: 
        # 이렇게 읽어오는 거면 input을 list로 받지 않아도 돼. 
        # str1이 문자열이라도 가능.
        di[i] = 0
        for j in str2:
            if i == j:
                di[i] += 1

    print(f'#{tc}',max(di.values()))

# 교수님 코딩리뷰
# str1 = AAA
# str2 = AAA 라면?
# 답은 나오는데
# di[i] = 0 부분에서 계속 날라가. 굉장히 억울한 코드,,
# 시간이 오래 걸린다..
# 날라가지 않게 하는 방법 찾아봐.

'''
T = int(input()) #3
for tc in range(1, T+1):
    str1 = input() #XYPV
    str2 = input() #EOGGXYPVSY

'''