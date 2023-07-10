from datetime import datetime
class User() :
    def __init__(self, name, gender, birthdate, address) :
        self.id = ""
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = self.cal_age(birthdate)
        self.address = address

    # getter를 만들기 위해 @property 데코레이터를 사용한다. 함수 이름은 변수명과 동일하게 작성하는 관례가 있다. 
    # 그리고 setter를 만들기 위해 @변수.setter를 사용한다. 
    # 마찬가지로 변수명과 동일한 함수명을 사용하는 관례가 있다.

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender
        
    @property
    def birthdate(self):
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate):
        self.__birthdate = birthdate

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
        
    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address
    
    def cal_age(self, birthdate) :
        cur_year = datetime.today().year   
        age = int(cur_year) - int(birthdate[0:4]) + 1
        return age