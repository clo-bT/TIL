#재귀함수
def sum_of_digit(a):
    #만약에 a를 몫이 0이면 a
    if a // 10 == 0:
        return a
    
    return sum_of_digit(a // 10) + (a % 10)


print(sum_of_digit(3904)) # 16