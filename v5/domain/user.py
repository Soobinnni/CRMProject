from datetime import datetime
class User() :
    def __init__(self, name, gender, birthdate, address) :
        self.login_id = ""
        self.login_pwd = ""
        self.id = ""
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = self.cal_age(birthdate)
        self.address = address

    @property
    def login_id(self):
        return self.__login_id

    @login_id.setter
    def login_id(self, login_id):
        self.__login_id = login_id

    @property
    def login_pwd(self):
        return self.__login_pwd

    @login_pwd.setter
    def login_pwd(self, login_pwd):
        self.__login_pwd = login_pwd

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