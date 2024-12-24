sample_list = [11,22,33,44,55]

# 주어진 리스트의 3번 index에 있는 항목을 제거하고 변수에 할당해 주세요
print("original list: ",sample_list)
elem = sample_list.pop(3)

print('list after: ',sample_list)
print('elem: ',elem)

# sample_list 의 가장 뒤에 77을 추가해보세요
sample_list.append(77)

# 할당해 놓은 변수의 값을 sample_list의 2번 index에 추가해보세요

print(sample_list)
sample_list.insert(2,elem)
print(sample_list)





my_tuple = (11, 22, 33, 44, 55, 66)

#주어진 튜플에서 44와 55의 값을 새로운 튜플에 할당해보세요.
new_tuple = my_tuple[3: -1]
print(new_tuple)


a = [1, 2, 3]
b = a[:] # 전체 다
print(a, b)
b[0] = 5
print(a, b)

a = [1, 2, ['a', 'b']]
b = a[:] # 전체 다
print(a, b)
b[2][0] = 0
print(a, b)

import copy
a = [1, 2, ['a', 'b']]
b = copy.deepcopy(a)
print(a, b)
b[2][0] = 0
print(a, b)


test_list = [1, 2, 3, 7, 4, 6, 5]
test_list.sort()
print(test_list)

scores = [('eng', 88),('sci',90),('math',95)]
# 정렬. 기준이 없으면 sort는 앞에 있는 게 기준
def check(x):
    return x[1]
print(scores)
scores.sort(key = check) # check함수 썼을 때

scores.sort(key = lambda x : x[1])
print(scores)


