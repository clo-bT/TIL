for tc in range(1, 11):
    N = int(input()) # 회문의 길이 4
    arr = [input() for _ in range(8)]
    print(arr)
    cnt = 0
    for i in range(8):
        line = arr[i] # 한줄
        for j in range(8-N+1):
            word = line[j:j+4]
            if  word == word[::-1]: # 단어 거꾸로 읽어들인 거랑 같으면
                cnt += 1
        
    for i in range(8):
        line = arr[i] # 한줄
        for j in range(8-N+1):
            word = line[j:j+4]
            if  word == word[::-1]: # 단어 거꾸로 읽어들인 거랑 같으면
                cnt += 1

'''
for i in range(N):  # arr 가로 수만큼 돌릴거야
        clm_word = ''
        for j in range(N):
            clm_word += arr[j][i]
        for j in range(N - M + 1):
            new_word = clm_word[j:j + M]  # new_word는 단어중에 13개만
            if new_word == new_word[::-1]:  # 단어 거꾸로 읽어들인 거랑 같으면
                print(f'#{tc}', new_word)  # 출력
'''