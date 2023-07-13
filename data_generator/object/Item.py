from object.Generator import Generator
import random

class ItemGenerator(Generator):
    def __init__ (self):
        self.id = ""
        self.name = ""
        self.type = ""
        self.unit_price = ""
        
    def generate_info(self, num) :
        info = []
        for _ in range(0, num) :
            name, type_ = self.mk_name_type()
            info_list = [self.mk_uuid(), name, type_, self.mk_unit_price()]           
            info.append(info_list)
        return info

    def mk_name_type(self) :
        detail_list = ['Americano', 'Strawberry', 'Watermelon', 'Red Velvet', 'Espresso', 'Vanilla', 'Moca', 'Pineapple', 'Cappuccino', 'Mango']
        detail = random.choice(detail_list)
        type_ = self.mk_type()

        name = detail + ' ' + type_
        return name, type_
    
    def mk_type(self) :
        type_list = ['Cake','Juice','Coffee']
        type_ = random.choice(type_list)
        return type_
    
    def mk_unit_price(self) :
        price = (random.randint(10,99)) * 100
        return price   