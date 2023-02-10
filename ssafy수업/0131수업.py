
def ko_hello(name):
    print(f'안녕하세요 {name}님!')

def en_hello(name):
    print(f'Hello {name}!')

ko_hello('amy')
en_hello('amy')

# 각 함수 뒤에 ^~^// 를 붙이고 싶다 하면 따로따로 추가할 필요 없이
def add_emoji(name, func):
    func(name)
    print('^~^//')

add_emoji('amy', ko_hello)
add_emoji('amy', en_hello)



# 이모지 데코레이터
def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')

    return wrapper

emoji_decorator(ko_hello)('amy')



## class
class Person:
    def __init__(self):
        self._age = 0

    @property
    def age(self): # getter
        return self._age

    @age.setter
    def age(self,age): #seter
        self._age = age
    

p1 = Person()
p1.age = 25
print(p1.age)



#예제
#배그
#공통적인부분 부모
#장르별 자식
class BattleGround():
    def __init__(self, damage):
        self.damage = damage
        pass
    def kill(self):
        if self.damage >= 100:
            return 'kill'
        else:
            return 'not kill'

class bullet5(BattleGround):
    # 여기서 데미지변수는 BattleGround랑은 다른 데미지
    def __init__(self, damage, bullet):
        super().__init__(damage) # self.damage = damage랑 같은말. 
        # 재정의긴 한데 정의가 안 되어있으면 부모꺼 씀.
        # 위에 거를 쓰려면 damage변수가 없어야 함
        # 근데 그러면 변수를 아예 못 받음
        self.bullet = bullet

    def bag(self):
        if self.bullet >= 300:
            return 'full'
        else:
            return self.bullet

class bullet7(BattleGround):
    def __init__(self, damage, bullet):
        super().__init__(damage)
        self.bullet = bullet

    def bag(self):
        if self.bullet >= 100:
            return 'full'
        else:
            return self.bullet

m4 = bullet5(100,400)
beryl = bullet7(80, 80)
print(m4.kill())
print(beryl.bag())
print(m4.bag())
print(beryl.kill())