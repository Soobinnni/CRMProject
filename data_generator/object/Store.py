from object.Generator import Generator
import random

class StoreGenerator(Generator):
    def __init__ (self):
        self.store_place_list = []
        self.id = ""
        self.name = ""
        self.type = ""
        self.address = []
    
    def generate_info(self, num) :
        info = []
        for _ in range(0, num) :
            name, type_ = self.mk_name_type()
            info_list = [self.mk_uuid(), name, type_, self.mk_address()]           
            info.append(info_list)
        return info

    def mk_name_type(self) :
        type_ = self.mk_type()
        store_num = random.randint(1, 10)
        store_place = random.choice(self.store_place_list)
        name = type_ + ' ' + store_place + str(store_num) + '호점'

        return name, type_
    
    def mk_type(self) :
        type_list = ['투썸', '이디야', '스타벅스', '커피빈']
        type_ = random.choice(type_list)

        return type_
