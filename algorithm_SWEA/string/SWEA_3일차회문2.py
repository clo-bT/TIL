import sys
sys.stdin = open("input.txt", "r")


for tc in range(1, 11):
    T = int(input()) #1-10
    arr = [input() for _ in range(100)]
    N= 100
    li= []
    for i in range(100):
        line = arr[i] # 한줄
        for M in range(100, 1, -1): # M이 회문구간길이. 제일 긴애 찾을거니까 길게 돌려
            for j in range(N-M+1): # 회문 M짜리 한줄 안에서 계속 찾기
                word = line[j:j+M] #단어 슬라이싱해서 비교할건데
                if  word == word[::-1]: # 단어 거꾸로 읽어들인 거랑 같으면
                    li.append(M) # 회문길이 몇일때였는지 저장
    # 세로도 똑같이 
    for i in range(100):
        arr_t = list(zip(*arr)) # 행열 바꾸기
        line_t = arr_t[i] #한줄
        for M in range(100, 1, -1): # M이 회문구간길이. 제일 긴애 찾을거니까 길게 돌려
            for j in range(N-M+1): # 회문 M짜리 한줄 안에서 계속 찾기
                word_t = line_t[j:j+M] #단어 슬라이싱해서 비교할건데
                if  word_t == word_t[::-1]: # 단어 거꾸로 읽어들인 거랑 같으면
                    li.append(M) # 회문길이 몇일때였는지 저장
    print(f'#{T}',max(li))

        
