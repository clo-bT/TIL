# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g
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
    
