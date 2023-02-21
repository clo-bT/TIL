N, M = map(int,input().split()) #8 8 가로 세로
arr = [input() for _ in range(N)]
arr_ans = ['BW' * 4,'WB' * 4] *4 
arr_ans1 = ['WB' * 4,'BW' * 4] *4 
c = 64
for i in range(N-8+1):
    for j in range(M-8+1):
        cnt = 0
        cnt2 = 0
        for k in range(8): # 8*8 찾기
            for l in range(8):
                if arr[i+k][j+l] != arr_ans[k][l]:
                    cnt += 1
                if arr[i+k][j+l] != arr_ans1[k][l]:
                    cnt2 += 1
        if min(c,cnt,cnt2) != c:
            c = min(c,cnt,cnt2)
print(c)
        

