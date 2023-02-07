grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

# print(type(grain_lst[0][1]))은 int
def high_price():
    li = []
    for i in range(len(grain_lst)):
        # 가격들 모아서 리스트로 묶어
        li.append(grain_lst[i][1])
    # 최대값 구하고
    m = max(li)
    # 얘가 누구 가격이었는지 찾기
    ind = 0
    for i in range(len(grain_lst)):
        if grain_lst[i][1] != m:
            ind += 1
        else:
            ind -= 1
    print(grain_lst[ind][0])
    
    
high_price()