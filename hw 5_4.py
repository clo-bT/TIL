# fn_d(91) 
# 출력 예시 
# 101
a = input()
def fn_d(n):
    d = len(a) + int(a)
    return(d)
def is_selfnumber(m):
    
    
'''
ori_number =[]
gen_number =[]
for number in range(1,5001):
    ori_number.append(number)

for number in range(0,5000):
    temp_sum = 0 # 부분합 계산을 위함
    i = ori_number[number] # i 는 자릿수 계산을 위함
    temp_sum = temp_sum + i # 현재 수인 n(i)는 무조건 더함
    temp = 0 # temp 는 오리지널 숫자를 나누는 중간 값을 보관하기 위함
    while i > 9 : # 10보다 작으면 마지막 자리수만 (i)를 더하고 종료할 것임
        temp = i # 나누어진 값을 계산하기 위한 용
        i = (int)(i/10) # 첫번째 자리수 빼고 나머지 값을 저장함
        #print("next i",i)
        while temp > 9:
            temp = (int)(temp%10) # 10보다 작을때 까지 나눠서 첫번째 자리수를 구함
        temp_sum = temp_sum + temp

    temp_sum = temp_sum + i # 10보다 작으면 마지막 자리수만 (i)를 더하고 종료할 것임

    gen_number.append(temp_sum)

gen_number.sort()
sum = 0
ori_number_pivot = 0
gen_number_pivot = 0


# 오리지널 넘버와 제너레이트 된 숫자를 피벗으로 비교하여 self sumber인지 아닌지 판단할 거임
# 파이썬 자체에 간결한 코드로도 쉽게 해결가능 아래 예시는 좋은 코드는 아님



while ori_number_pivot < 5000:
    if ori_number[ori_number_pivot]< gen_number[gen_number_pivot]:
        #print ("self number",ori_number[ori_number_pivot])
        sum = sum + ori_number[ori_number_pivot];
        #print (sum)
        ori_number_pivot = ori_number_pivot + 1

    elif ori_number[ori_number_pivot]>gen_number[gen_number_pivot]:
        gen_number_pivot = gen_number_pivot + 1
    else:
        ori_number_pivot = ori_number_pivot + 1
        gen_number_pivot = gen_number_pivot + 1

print(sum)
'''


    
