#words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

# 이미 입력한 단어이거나 끝말잇기 실패하면 
# -> 몇번째 사람이 틀렸다 출력, 다시 게임시작
# done 입력하면 게임 끝
'''

#첫 단어 입력받아서 리스트 저장
i = 0
list1 = []
a = input('게임 종료는 "done" 입력\n끝말잇기 시작 !: ')
if a =='done':
    print('게임이 종료되었습니다')
else:
    list1.append(a)
    i = i + 1
    
#두번째 단어부터 비교 시작
while a != 'done':
    s = input('\n끝말잇기를 이어가주세요: ')
    list1.append(s)
    b = list1[i]

    #입력한 글자가 done이면 끝남
    if s == 'done':
        print('게임이 종료되었습니다.')
        break

    #받은 끝글자랑 첫글자가 다르거나 같은 거 말하면 지금이 몇번째인지 출력, 다시 게임시작 continue 
    elif (s.strip()[-1] != b.strip()[0]) or (set(list1) != list1):
        print(f'{len(list1)}번째 사람이 졌습니다\n 다시 시작해주세요.')
        i = 1
        continue

    #받은 끝글자랑 첫글자가 같으면 통과 pass
    elif s.strip()[-1] == b.strip()[0]:
        i += 1
        pass

'''

before_words = []

while True:
    word = input('단어입력 : ')
    #만약 첫번째 단어라면
    if len(before_words) == 0:
        before_words.append(word)
        continue
    #끝말잇기를 틀리거나 이전에 특장했던 단어를 사용한 경우
    if before_words[-1][-1] != word[0] or (word in before_words):
        print(f'{len(before_words + 1)}번째 사람이 틀렸다')
        break
    #잘 말한 경우
    else:
        print('다음 글자 입력!')
        before_words.append(word)


    
