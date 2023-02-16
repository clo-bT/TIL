op = {'+':1, '-':1, '*':2, '/':2}
 
def postfix(li):
    stack = [0]*len(li)
    top = -1
    pfix = ''
 
    for t in li:
        if '0' <= t <= '9':                             # 피연산자인 경우
            pfix += t
        elif t in op:                                   # 연산자인 경우
            if top == -1 or op[stack[top]] < op[t]:     # 스택이 비어있거나 토큰의 우선순위가 높으면
                top += 1
                stack[top] = t
            else:
                while top > -1 and op[stack[top]] >= op[t]: # 스택이 남아있고 토큰의 우선순위가 높을 때 까지
                    top -= 1
                    pfix += stack[top + 1]
                top += 1
                stack[top] = t
    while top > -1:
        top -= 1
        pfix += stack[top+1]
 
    return pfix
 
def postfix_eval(text):
    stack = []
    o_li = list(map(str, text))
    for i in range(len(o_li)):
        if o_li[i].isdigit():                           # 숫자
            stack.append(int(o_li[i]))
        else:                                           # 연산자
            if len(stack) > 1 and type(stack[-1]) == int:   # 연산 가능
                a = stack.pop()
                b = stack.pop()
                if o_li[i] == '+':
                    stack.append(b+a)
                elif o_li[i] == '-':
                    stack.append(b-a)
                elif o_li[i] == '*':
                    stack.append(b*a)
                else:
                    stack.append(b//a)
 
    return stack
 
 
for tc in range(1, 11):
    N = int(input())
    op_li = list(map(str, input()))
    stack = []
 
    post = postfix(op_li)
    result = postfix_eval(post)
    print(f'#{tc} {result[0]}')