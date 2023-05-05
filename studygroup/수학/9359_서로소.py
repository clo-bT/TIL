'''
서로소
포함배제의 원리
N = A^i *  B^j * C^k ...
에라토스테네스의 체로 소수배열을 만들어놓고
N을 검정. A로 나누어떨어지면 넘기고 해서 A, B, C 를 찾고
(Y이하의 서로소가 아닌 수) - (X미만의 서로소가 아닌 수)를 구할거야
res = Y - (Y//A) - (Y//B) - (Y//C) 
+ (Y//(A*B)) + (Y//(A*C)) + (Y//(B*C)) 
- Y//(A*B*C) 
하고 res1해서 두개 구해서 빼
'''
T = int(input()) #2
for tc in range(T):
    A, B, N = map(int,input().split())
    