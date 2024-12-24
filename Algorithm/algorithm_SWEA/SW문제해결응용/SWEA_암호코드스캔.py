# 2단계 + 하나 안에 여러코드 찾기까지 함

dicc = {'0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9}

T = int(input()) #2
for tc in range(1, T+1):
    N, M = map(int,input().split()) #16 26
    arr = [input() for _ in range(N)]
    realans = []

    while True:
        # 종료 조건
        if arr == ['0'*M]*N:
            break

        # 코드 찾기
        for i in arr:
            if i != '0' * M:
                line = i #000000001DB176C588D26EC000
                break                   # for i
        # print('line',line)

        # 16진수 -> 2진수
        code = ''
        for x in line:
            num = int(x, 16)
            for j in range(3, -1, -1):
                bit = 1 if num&(1<<j) else 0 
                code += str(bit) 

        # 2진수 코드 -> 뒤에서 1찾아서 56개 잘라
        for i in range(len(code)-1,0,-1):
            if code[i] == '1':
                code = code[i-55:i+1] #01110110110001011101101100010110001000110100100110111011
                break
        # print('code',code)

        # 2진수 7비트씩 -> 10진수 바꿔 
        mycode = ''
        ans = 0
        for i in range(0,len(code),7):
            mycode += str(dicc[code[i:i+7]]) #75755027
            ans += dicc[code[i:i+7]] #38

        # 암호 해독
        even, odd = 0,0
        for i in range(0,8,2):
            even += int(mycode[i])
        for i in range(1,9,2):
            odd += int(mycode[i])

        # 판독해서 맞는 것만 넣기
        if (even*3 + odd) % 10 == 0:
            realans.append(ans)
    
        # 코드 찾은 이후에 그 코드를 '0'으로 고치기 위함
        lcnt = 0    # 코드 길이 파악 위함
        s = ''
        for i in range(M):
            if line[i] != '0': # line은 000000001DB176C588D26EC000
                lidx = i #22
                lcnt += 1 #15
                s += line[i] #1DB176C588D26EC
        for i in range(N):
            if s in arr[i]:
                arr[i] = str(arr[i][:lidx-lcnt+1] + '0' * (lcnt) + arr[i][lidx+1:])
                # 00000000 + 0*15 + 000 로 교체
             
    print(f'#{tc}',sum(realans))