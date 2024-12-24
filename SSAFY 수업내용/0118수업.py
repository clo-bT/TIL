#음식을 먹는 과정
#X를 먹는다 ->반복
foods = ['찜닭', '김치','콩자반', '계란후라이']

'''
함수설명

특정동작

'''
def eat(pre_action, anything, after_action):
    '''
    무언가를 먹는 것을 표현하는 함수
    pre_action: 입에 넣기 전 사전 동작
    anything: 무언가
    after_action: 무언가를 삼키기 위한 사후 동작
    '''
    print(pre_action)
    print(f'{anything}')
    print(after_action)


def eat_food(food):
    '''
    파라미터로 음식 종류를 받아 "먹는다"를 표현하는 함수
    '''
    eat('수저를 집는다', food, '냠냠')
    
    
