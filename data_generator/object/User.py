from object.Generator import Generator
import random
import datetime

class UserGenerator(Generator):
    def __init__ (self):
        self.first_name_list = []
        self.last_name_list = []
        self.id = ""
        self.name = ""
        self.gender = ""
        self.age, self.birthdate = 0, ""
        self.address = ""

    def generate_info(self, num) :
        info = []
        for _ in range(0, num) :
            age, birthdate =  self.mk_age_birthdate()
            info_list = [self.mk_uuid(), self.mk_name(), self.mk_gender(), age, birthdate, self.mk_address()]           
            info.append(info_list)
        return info

    def mk_name(self) :
        first_name = random.choice(self.first_name_list)
        last_name = random.choice(self.last_name_list)
       
        name = first_name + last_name
        return name
    
    def mk_gender(self) :
        return random.choice(['Female','Male'])

    def mk_age_birthdate(self) :
        current_year = datetime.datetime.now().year
        birthdate = self.mk_birthdate()
        age =  current_year - int(birthdate[0:4]) + 1

        return age, birthdate
    
    def mk_birthdate(self) :
        while True:
            year = random.randint(1950, 2023)
            month = random.randint(1, 12)
            day = random.randint(1, 31)

            try:
                date = datetime.datetime(year, month, day)
                birth = date.strftime('%Y-%m-%d')  # 날짜 포맷
                return birth
            except ValueError:
                continue