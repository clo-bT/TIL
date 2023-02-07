# A. 입력예시
# print(de_identify('970103-1234567'))
# print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 


def de_identify(id):
    cut = id[0:6]
    out = cut + '*' * 7
    return out

print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))
