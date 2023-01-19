# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

'''
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

temp1 = []
temp2 = []
temp3 = []
cnt = 0
# 소금물의 퍼센트 농도와 양 받기
while True:
    salt = list(map(str,list(input('소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ').split())))
    if (salt[0] == 'Done') :
        break
    else :
        salt = int(salt[1].replace('g', '')) * int(salt[0].replace('%', '')) / 100 #소금의 양 계산
        temp1.append(int(salt[0].replace('%', ''))) # 농도
        temp2.append(int(salt[1].replace('g', ''))) # 소금물의 양
        temp3.append(salt)
    cnt += 1
    if (cnt >= 5):
        break
# 전체 합의 소금물의 농도와 양 구하기
salt_all = sum(temp3)
saltwater_all = sum(temp2)
salt_con_all = salt_all / saltwater_all * 100
print('소금물의 양 : {}g 소금물의 농도 : {}%'.format(saltwater_all, round(salt_con_all, 2))) #결과 출력
