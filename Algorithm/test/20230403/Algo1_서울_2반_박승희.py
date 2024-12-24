T = int(input()) #3
dic = {'1': '0001', '2':'0010', '3':'0011','4':'0100', '5':'0101', '6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1111'}
for tc in range(1, T+1):
    N = int(input()) #3 len(A)
    A = input() #E6D
    tmp = ''
    for i in range(N):
        tmp += dic[A[i]]
    #print(tmp) #111001101101
    cnt = 0
    maxC = 0
    for i in tmp:
        if int(i):
            cnt += 1
            if maxC <= cnt:
                maxC = cnt
        else:
            cnt = 0
    print(f'#{tc} {maxC}')