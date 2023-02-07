# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 
# 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력 
# 10

# 출력
# 3628800
a = int(input())

def packtori(a):
    if a == 1:
        return a
    elif a == 0:
        return 1
    return a * packtori(a-1)

print(packtori(a))