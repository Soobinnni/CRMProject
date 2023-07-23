from datetime import datetime
from flask_login import UserMixin

class AuthUser(UserMixin):
    def __init__(self, uuid, id, name, gender, birthdate, age, address, user_auth):
        self.uuid = uuid
        self.id = id
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = age
        self.address = address
        self.user_auth = user_auth

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"USER: {self.id} = {self.name}"
    
class User() :
    def __init__(self, login_id, login_pwd, name, gender, birthdate, address, user_auth_id) :
        self.login_id = login_id
        self.login_pwd = login_pwd
        self.id = ""
        self.name = name
        self.gender = gender
        self.birthdate = birthdate
        self.age = self.cal_age(birthdate)
        self.address = address
        self.user_auth_id = user_auth_id

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

    @property
    def user_auth_id(self):
        return self.__user_auth_id

    @user_auth_id.setter
    def user_auth_id(self, user_auth_id):
        self.__user_auth_id = user_auth_id
    
    def cal_age(self, birthdate) :
        cur_year = datetime.today().year   
        age = int(cur_year) - int(birthdate[0:4]) + 1
        return age