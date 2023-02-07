# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

'''내가 해볼게
salt = []
mul = []
i, n = 1 ,0

while True:
    while True:
        a,b = input(f'{i}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오:').split()
        if a == 'Done':
            break

        salt.append((int(a) / 100) * int(b))
        mul.append(int(b))
        n += 1
        i += 1
    salt_all = sum(salt)
    mul_all = sum(mul)
    nongdo = round(((salt_all /  mul_all) * 100), 2)
    
    if n == 5:
        break
    break

        

print(f'{nongdo}% {mul_all}g')
'''

nongdo = []
saltwater = []
s = []
c = 0
# input 받기
while True:
    salts = list(map(str,input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split()))
    if salts[0] == 'Done':
        break
    
    else:
        salt = int(salts[1]) * (int(salts[0]) / 100)
        nongdo.append(int(salts[0]))
        saltwater.append(int(salts[1]))
        s.append(salt)
    c += 1
    if c == 5:
        break

salt_all = sum(s)
saltwater_all = sum(saltwater)
salt_con_all = salt_all / saltwater_all * 100
print(f'{round(salt_con_all, 2)}%, {saltwater_all}g ')


'''
# 보석님 코드 변수명만 바꾼 거 

nongdo = []
saltwater = []
s = []
cnt = 0
# 소금물의 퍼센트 농도와 양 받기
while (True) :
    salts = list(map(str,list(input('소금물의 퍼센트 농도와 소금물의 양을 입력하세요.: ').split())))
    if (salts[0] == 'Done') :
        break
    else :
        salt = int(salts[1].replace('g',''))*int(salts[0].replace('%',''))/100 #소금의 양 계산
        nongdo.append(int(salts[0].replace('%',''))) # 농도
        saltwater.append(int(salts[1].replace('g',''))) # 소금물의 양
        s.append(salt)
    cnt += 1
    if (cnt >=5) :
        break
# 전체 합의 소금물의 농도와 양 구하기
salt_all = sum(s)
saltwater_all = sum(saltwater)
nongdo_all = round(salt_all / saltwater_all * 100, 2)
print(f'{nongdo_all}%, {saltwater_all}g') #결과 출력

'''