
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