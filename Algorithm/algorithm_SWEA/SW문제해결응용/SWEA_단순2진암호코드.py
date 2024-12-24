T = int(input()) #2
code = {'0001101':0,
        '0011001':1,
        '0010011':2,
        '0111101':3,
        '0100011':4,
        '0110001':5,
        '0101111':6,
        '0111011':7,
        '0110111':8,
        '0001011':9}
for tc in range(1,T+1):
    N, M = map(int,input().split()) # 16 80
    arr = [input() for _ in range(N)]
    
    for i in range(N):
        for j in range(M-1, 54, -1):    # 가장 왼쪽에 치우친 패턴이 0 - 55일테니까
            if arr[i][j] == '1':
                line = arr[i][j-55:j+1]
                break                   # 누구를 빠져나오는 break인지 주석사용하기
        if line != '':
            break   # for i
        
    mycode = ''
    ans = 0
    for i in range(0,56,7):
        mycode += str(code[line[i:i+7]]) #75755027
        ans += code[line[i:i+7]] #38
    
    even, odd = 0,0
    for i in range(0,8,2):
        even += int(mycode[i])
    for i in range(1,9,2):
        odd += int(mycode[i])

    if (even*3 + odd) % 10 == 0:
        print(f'#{tc}', ans)
    else:
        print(f'#{tc}',0)