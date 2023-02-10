class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()

print(p1.name)





class person:
    def talk(self): # 인스턴스 메서드야. 인스턴스가 쓸거고 인스턴스가 필요해
        print('안녕')
    def eat(self,food):
        print(f'{food}를 냠냠')

person1 = person # person1이라는 인스턴스
person1.talk() #안녕
person1.eat('피자') #피자를 냠냠
person1.eat('치킨') #치킨을 냠냠




class Person:
    count = 0
    def __init__(self,name):
        self.name = name
        Person.count += 1
    
    @classmethod
    def number_of_population(cls):
        print(f'인구수는 {cls.count}입니다')

person1 = Person('박승희')
Person.number_of_population() # 클래스의 메서드를 호출 (인스턴스랑 관련 x)
person1.number_of_population() # 인스턴스 입장에서 함수 호출


# 오후수업

#클래스 정의
class Singer():
    name = '박승희'
    # self = 인스턴스 내부 namespace
    # self.name = 인스턴스 변수 정의
    def __init__(self, name):
        self.name = name

#인스턴스 정의
아이유 = Singer('아이유')
#접근은
print(아이유.name)
박치언 = Singer('박치언')


# 오후수업

def get_population():
    pass
# 클래스 메서드
# 인스턴스 변수 사용하면 에러 남
@classmethod
def get_count(cls):
    print(f'전체 나라 수는 {cls.count} 입니다')

# 스태틱 메서드 인스턴스,클래스 변수 사용 안함
# 변수는 안 써도 문맥상 해당 클래스에 포함된다고 판단될 때
@staticmethod
def print_test():
    print('print_test')

def __del__(self):
    print('소멸자')

