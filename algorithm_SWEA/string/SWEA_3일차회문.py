T = int(input()) #3

for tc in range(1, T+1):
    N, M = map(int,input().split()) #10 10, 20 13
    arr = [input() for _ in range(N)]

    for i in range(N): # arr 세로 수만큼 돌릴거야
        word = arr[i]
        for j in range(N-M+1):
            pal_word = word[j:j+M]
            if  pal_word == pal_word[::-1]: # 단어 거꾸로 읽어들인 거랑 같으면
                print(f'#{tc}', pal_word) # 출력

    for i in range(N):  # arr 가로 수만큼 돌릴거야
        clm_word = ''
        for j in range(N):
            clm_word += arr[j][i]
        for j in range(N - M + 1):
            new_word = clm_word[j:j + M]  # new_word는 단어중에 13개만
            if new_word == new_word[::-1]:  # 단어 거꾸로 읽어들인 거랑 같으면
                print(f'#{tc}', new_word)  # 출력



'''
    for i in range(N): # arr 가로 수만큼 돌릴거야
        new_word = ''
        for j in range(N):
            new_word += arr[j][i]
        for j in range(N - M + 1):
            if new_word[j:] == new_word[j + M - 1::-1]:  # 단어 거꾸로 읽어들인 거랑 같으면
                print(f'#{tc}', new_word)  # 출력
'''



