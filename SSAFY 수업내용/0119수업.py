
# 패킹 / 언패킹 1

def my_sum(a,b,c):
    return a + b + c

num_list = [10,20,30]

rst = my_sum(num_list[0],num_list[1],num_list[2],)
rlt = my_sum(*num_list) 
# rst == rlt 인건데 더 간단함
# 뭔가 뭉탱이 앞에 *붙어있으면 언패킹한거야
print(rst)
print(rlt)


# 패킹 / 언패킹 2

def test(values):
    for value in values:
        print(value)
        
test(1)
test(1, 2)
test(1, 2, 3, 4)


# 패킹 / 언패킹 positional

def test(*agrs):
    rlt = 0
    for value in agrs:
        rlt += value
    return rlt

my_sum() # 0
my_sum(1, 2, 3) # 6

# 패킹 / 언패킹 keyword

def test1(**kwagrs):
    print(kwagrs, type(kwagrs))
    kwagrs['name']
    return kwagrs

test(name = 'aiden', age = 21)
# 몇개가 들어오든 다 받아줘. 다 안쪽에서 접근할 수 있게

# 둘 다 쓸 수 없을까? 있음

def test2(*argss,**kwagrs):
    test2(1,2,3,4,name = 'aiden', age = 21)
    print(argss, kwagrs)
    return kwagrs
# positional과 keyword 둘 다 되게 이렇게 바뀌면 
# 1,2,3,4가 *argss로 들어가고 name age가 kwagrss로 들어가


# 모듈과 패키지

import random

num_list1 = [1,2,3,4]
random.shuffle(num_list1)
print(num_list1)
# 저는 셔플만 쓸건데 랜덤 다 가져오는 거 좀 그래요 하면
# from random import shuffle 이렇게 쓰면 돼

