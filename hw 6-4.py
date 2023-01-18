# A.    입력 예시 
# eat,tea,tan,ate,nat,bat

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

#입력을 받고 리스트로 만들고 
wordlist = list(map(str,input().split(',')))
a = []
#함수 만들어볼게 얍
def func1():
    #list 안에 단어 개수만큼
    for j in range(len(wordlist)):
        word = wordlist[j]
        # print(word)
        # s = sorted(word) 하면 ['a','e','t']
        s = ''.join(sorted(word))  # 하면 aet
        a.append(str(s))
        
func1()


def mat():
    for j in range(len(a)):
        f = a[j]
        b = [i for i in range(len(wordlist)) if f in wordlist[i]]
    print(b)

# 정렬시키는 함수

mat()
# print(wordlist[0][0])
# print(wordlist[0][1])
# print(wordlist[0][2])
# 1. 정렬시켜서 비교하기
# for i in range (len(wordlist)):
#     print(wordlist[i][0],wordlist[i][len()],wordlist[i],[i+2])
    #if len(wordlist[i][i])


# 2. 아스키코드 이용하기





